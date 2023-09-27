import aws_cdk as cdk
from constructs import Construct
from .stages.deploy_stage import DeployStage


class PipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, environment: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        ctx = self.node.try_get_context(environment)

        bucket = cdk.aws_s3.Bucket.from_bucket_name(
            self, "artifacts_bucket", ctx["artifact_bucket"]
        )

        # Assume github token has been set in SSM
        oauth = cdk.SecretValue.secrets_manager(
            secret_id=ctx["github_token_secret"],
            json_field=ctx["github_token_secret_key"],
        )

        pipeline = cdk.pipelines.CodePipeline(
            self,
            id=ctx["app_name"] + "Pipeline",
            artifact_bucket=bucket,
            self_mutation=True,
            synth=cdk.pipelines.ShellStep(
                id="synth",
                input=cdk.pipelines.CodePipelineSource.git_hub(
                    repo_string=ctx["pipeline_repo"],
                    branch=ctx["pipeline_branch"],
                    authentication=oauth,
                ),
                commands=[
                    "npm install -g aws-cdk cdk-assume-role-credential-plugin",
                    "pip3 install -r requirements.txt",
                    "cdk synth -v",
                ],
            ),
        )

        deployStage = DeployStage(
            scope=self,
            id="myDeployStage",
            ctx=ctx,
            env=kwargs["env"],
        )

        pipeline.add_stage(deployStage)

        pipeline.build_pipeline()
