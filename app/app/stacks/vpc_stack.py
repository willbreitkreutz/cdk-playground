import aws_cdk as cdk
from constructs import Construct


class VpcStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, ctx, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = cdk.aws_ec2.Vpc.from_lookup(self, id="vpc", vpc_id=ctx["vpc_id"])