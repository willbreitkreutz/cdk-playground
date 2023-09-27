import aws_cdk as cdk
from ..stacks.vpc_stack import VpcStack
from ..stacks.rds_stack import RdsStack


class DeployStage(cdk.Stage):
    def __init__(self, scope, id, ctx, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Get a reference to our VPC
        self.vpcStack = VpcStack(
            scope=self,
            construct_id="myVpc",
            ctx=ctx,
            env=kwargs["env"],
        )

        # Create a RDS database
        self.rdsStack = RdsStack(
            scope=self,
            construct_id="myRds",
            ctx=ctx,
            vpc=self.vpcStack.vpc,
            env=kwargs["env"],
        )

        #
