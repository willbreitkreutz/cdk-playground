import aws_cdk as cdk
from constructs import Construct

rds_versions = {
    "Postgres14": cdk.aws_rds.DatabaseInstanceEngine.postgres(
        version=cdk.aws_rds.PostgresEngineVersion.VER_14_9)
    
}


class RdsStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, ctx, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.rds_secret = cdk.aws_rds.DatabaseSecret(self, 'rdsSecret', username=ctx['rds_admin_username'])
        credentials = cdk.aws_rds.Credentials.from_secret(self.rds_secret)
        self.rds = cdk.aws_rds.DatabaseInstance(self, 'myDbInstance', engine=rds_versions[ctx['database_type']])