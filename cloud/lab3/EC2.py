import boto3
from boto3.session import Session

#Create a Java program to manage your EC2 instance. Start with listing region names and their endpoints.
def get_all_regions(service_name='ec2'):
    '''The name of a service, e.g. "s3" or "ec2"'''
    s = Session()
    regions = s.get_available_regions(service_name)
    print(regions)
    return regions

def get_regions(service_name='ec2'):
    ec2 = boto3.client(service_name)
    response = ec2.describe_instances()
    zones = []
    for i in range(len(response['Reservations'])):
        zones.append(response['Reservations'][i]['Instances'][0]['Placement']['AvailabilityZone'])
    print(zones)
    return zones
get_regions()


#3. Write a method to run an instance from the list of regions from the previous step.
#(a) Use <keypair, security groups, number of instances, etc> as parameters to start an instance.
# Instance ID: i-0df06c8c4c55f6442
#Create instance
def create_instance(region="eu-north-1"):
    ec2_client = boto3.client("ec2", region_name=region)
    instances = ec2_client.run_instances(
        ImageId="ami-0bd9c26722573e69b",
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.micro",
        KeyName="AshmitaRomain",
        SecurityGroups=["AshmitaRomain"]
    )

    print(instances["Instances"][0]["InstanceId"])

#start existing instance
def start_instance(instance_id, region="eu-north-1"):
    ec2 = boto3.client("ec2")
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(response)

#4. Write a method to retrieve the status of your running instance(s).
def get_running_instances(region="eu-north-1"):
    ec2_client = boto3.client("ec2", region_name=region)
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
          #  public_ip = instance["PublicIpAddress"]
          #  private_ip = instance["PrivateIpAddress"]
            security_group = instance["SecurityGroups"][0]["GroupName"]
            print(f"{instance_id}, {instance_type}, {security_group}")

#get_running_instances()

#5. Write a method to stop an instance(s) that you started.
def stop_instance(instance_id, region="eu-north-1"):
    ec2_client = boto3.client("ec2", region_name=region)
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)

def terminate_instance(instance_id, region="eu-north-1"):
    ec2_client = boto3.client("ec2", region_name=region)
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)

#start_instance("i-0df06c8c4c55f6442")
#stop_instance("i-0df06c8c4c55f6442")

# instance 2
#stop_instance('i-0518dd7c007f5a2b9')
#create_instance()

#get_running_instances()