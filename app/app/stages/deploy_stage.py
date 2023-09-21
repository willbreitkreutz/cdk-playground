import aws_cdk as cdk
from ..stacks.vpc_stack import VpcStack

class DeployStage(cdk.Stage):
    def __init__(self, scope, id, ctx, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.vpcStack = VpcStack(scope=self, construct_id='myVpc', ctx=ctx)
