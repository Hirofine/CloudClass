import boto3
from botocore.exceptions import NoCredentialsError

def delete_from_s3(bucket, file_name):
    try:
        s3 = boto3.client("s3")
        s3.delete_object(Bucket=bucket, Key=file_name)
        print("Great Succes!")
        return True
    except Exception as ex:
        print("Great Succes! NOOOT")
        print(str(ex))
        return False
    

delete_from_s3('generatedbucketashrom', 'index.html')
