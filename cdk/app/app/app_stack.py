from constructs import Construct

# from aws_cdk.core import App, Stack, Environment
from aws_cdk import (
    Duration,
    Stack,
    Environment,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)


class AppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## Get vpc
        # Information from environment is used to get context information
        # so it has to be defined for the stack
        # stack = AppStack(
        #     self, "AppStack", env=Environment(account="account_id", region="region")
        # )
        stack = Stack(
            self, "app", env=Environment(account="0000000000", region="us-east-1")
        )
        # Retrieve VPC information
        vpc = ec2.Vpc.from_lookup(
            stack,
            "VPC",
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
            is_default=True,
        )

        print("--VPC info--")
        print(vpc.to_string())
        print(vpc.vpc_cidr_block)
        print(vpc.private_subnets)
        print(vpc.public_subnets)
        for ps in vpc.private_subnets:
            print(ps.to_string())
        for ps in vpc.public_subnets:
            print(ps.to_string())
        # Iterate the private subnets
        # selection = vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT)

        # for subnet in selection.subnets:
        #     pass

        # queue = sqs.Queue(
        #     self,
        #     "AppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(self, "AppTopic")

        # topic.add_subscription(subs.SqsSubscription(queue))
