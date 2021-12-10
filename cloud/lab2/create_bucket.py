import sys
import boto3
from botocore.exceptions import ClientError

def list_my_buckets(s3):
    print('Buckets:\n\t', *[b.name for b in s3.buckets.all()], sep="\n\t")

def create_bucket(bucket_name, region):
    try:
        print('\nCreating new bucket:', bucket_name)
        s3 = boto3.resource('s3', region_name=region)
        list_my_buckets(s3)
        bucket = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    except ClientError as e:
        print(e)
        sys.exit('Exiting the script because bucket creation failed.')

    bucket.wait_until_exists()
        


    return True


create_bucket('generatedbucketashromapsoutheast2','ap-southeast-2')
