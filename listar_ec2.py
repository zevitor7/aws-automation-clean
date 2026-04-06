import boto3

session = boto3.Session(region_name='us-east-1')
ec2 = session.client('ec2')

response = ec2.describe_instances()

for r in response['Reservations']:
    for i in r['Instances']:
        print(i['InstanceId'], i['State']['Name'])