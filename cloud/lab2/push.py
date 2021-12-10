import boto3
from botocore.exceptions import NoCredentialsError
import time 
import csv

    
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        #print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

print("Start timer")
myfile = open('res.csv', 'a')

res ="Region;Size;0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;\n"
for k in range(3):
    if(k==0):
        bucket_name = 'generatedbucketashrom'
        region = 'Stockholm;'
    elif(k==1):
        bucket_name = 'generatedbucketashromusnorth2'
        region = 'Ohio;'
    else:
        bucket_name = 'generatedbucketashromapsoutheast2'
        region = 'Sydney;'
    for j in range(3):
        if(j == 0):
            local_file_name = './dummy_files/1MB.db'
            distant_file_name = '1MB.db'
            res += region + '1MB;'
        elif(j==1):
            local_file_name = './dummy_files/10MB.db'
            distant_file_name = '10MB.db'
            res+= region + '10MB;'
        else:                
            local_file_name = './dummy_files/100MB.bin'
            distant_file_name = '100MB.bin'
            res+= region + '100Mb;'
        for i in range(50):
            pre_upload = time.time()
            uploaded = upload_to_aws(local_file_name, bucket_name, distant_file_name)
            upload_time = time.time() - pre_upload
            res = res + str(upload_time) + ";"
            print("Uploaded file : " + region + " " + distant_file_name + " " + str(i))
        res = res + "\n"
myfile.write(res)
myfile.close()
print("Stop timer")
