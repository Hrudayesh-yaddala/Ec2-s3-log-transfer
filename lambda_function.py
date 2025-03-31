import boto3
import json
from datetime import datetime

ssm = boto3.client('ssm')

# Update these Keys with actual values
instance_id = "YOUR_INSTANCE_ID"
bucket_name = "YOUR_S3_BUCKET"
# Path to the log file on EC2 instance
file_path = "Absolute/Path/To/Your/logback.xml"
# S3 key where the log file will be stored
s3_key = f"logs/logback-{datetime.now().strftime('%Y-%m-%d')}.xml"


def lambda_handler(event, context):
    try:
        # Command to copy log file from EC2 to S3
        command = f"aws s3 cp {file_path} s3://{bucket_name}/{s3_key}"

        # Send command to EC2 instance via AWS SSM
        response = ssm.send_command(
            InstanceIds=[instance_id],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': [command]}
        )

        return {
            "statusCode": 200,
            "body": "SSM command sent to EC2 to copy log file to S3."
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
