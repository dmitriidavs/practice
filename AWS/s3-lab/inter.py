import boto3


s3 = boto3.client("s3")


def download_file() -> None:
    s3.download_file(
        Bucket="traininig-aws-bucket",
        Key="data/Prelab-Kinesis-Real-Time-Clickstream.json",
        Filename="prelab.json"
    )


def upload_file() -> None:
    s3.upload_file(
        Bucket="traininig-aws-bucket",
        Key="data/prelab.json",
        Filename="prelab.json"
    )


upload_file()
