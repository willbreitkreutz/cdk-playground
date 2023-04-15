# Start up environemnt

```
docker compose up --build
```

Jump into `cdk` container if you wish to run the commands below.

<br><br>

# AWS CLI examples

## Create S3 Bucket in Localstack:

---

```
aws s3api create-bucket --bucket mybucket --region us-east-1 --endpoint http://${LOCALSTACK_HOSTNAME}:4566
```

or (use the awslocal tool)

```
awslocal s3api create-bucket --bucket mybucket --region us-east-1
```

---

## List S3 Bucket in Localstack:

```
aws s3 ls --endpoint http://${LOCALSTACK_HOSTNAME}:4566
```

or

```
awslocal s3 ls
```

<br><br>

# AWS CDK with Localstack

```
cdklocal bootstrap aws://000000000000/us-east-1
```

Notice we're using cdklocal and not cdk in the above example with localstack

Check the new S3 bucket just created:

```
awslocal s3 ls
```

It should look something like:

`cdk-hnb659fds-assets-000000000000-us-east-1`

Make a project folder and hop inside

```
mkdir testapp && cd testapp
```

Init the testapp

```
cdklocal init testapp --language python
```

<br><br>

# Localstack services status

http://localhost:4566/\_localstack/health

<br><br>

# Useful commands

Use `cdklocal` for Localstack

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation

# Packages used:

- awslocal - https://github.com/localstack/awscli-local
- cdklocal - https://github.com/localstack/aws-cdk-local

# Resources:

- Your first AWS CDK app - https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html
- Constructs Hub - https://constructs.dev/
