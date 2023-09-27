import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_rds as rds

from constructs import Construct

# Supported RDS engines and types
rds_engines = {
    "Postgres14": {
        "engine": rds.DatabaseInstanceEngine.postgres(
            version=rds.PostgresEngineVersion.VER_14_9
        ),
        "port": 5432,
    }
}
rds_instance_types = {
    "t3.micro": ec2.InstanceType.of(
        ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO
    )
}


class RdsStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, ctx, vpc, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        subnet_ids = ctx["vpc_database_subnets"]

        self.rds_security_group = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=vpc,
            description="Allow access to the database within the VPC",
            allow_all_outbound=True,
        )

        self.rds_security_group.add_ingress_rule(
            ec2.Peer.ipv4(vpc.vpc_cidr_block),
            ec2.Port.tcp(rds_engines[ctx["rds_database_engine"]]["port"]),
            "allow db Internal VPC access",
        )

        self.rds_secret = rds.DatabaseSecret(
            self, "rdsSecret", username=ctx["rds_admin_username"]
        )

        credentials = rds.Credentials.from_secret(self.rds_secret)

        self.rds = rds.DatabaseInstance(
            self,
            "myDbInstance",
            engine=rds_engines[ctx["rds_database_engine"]]["engine"],
            instance_type=rds_instance_types[ctx["rds_instance_type"]],
            instance_identifier=f"{ctx['app_name']}DB",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnets=list(
                    map(
                        lambda x: ec2.Subnet.from_subnet_id(self, f"DBSubnet{x}", x),
                        subnet_ids,
                    )
                )
            ),
            credentials=credentials,
            security_groups=[self.rds_security_group],
        )
