import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def check_aws_connection():
    try:
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print("✅ Connected to AWS as:", identity['Arn'])
    except NoCredentialsError:
        print("❌ No AWS credentials found.")
    except PartialCredentialsError:
        print("⚠️ Incomplete AWS credentials.")
    except Exception as e:
        print("❌ Connection failed:", str(e))

if __name__ == "__main__":
    check_aws_connection()