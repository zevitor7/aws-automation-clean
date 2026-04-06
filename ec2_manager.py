import boto3
import sys

ec2 = boto3.client('ec2')

action = sys.argv[1]
instance_id = sys.argv[2]

if action == "start":
    ec2.start_instances(InstanceIds=[instance_id])
    print("Instância iniciada!")

elif action == "stop":
    ec2.stop_instances(InstanceIds=[instance_id])
    print("Instância parada!")