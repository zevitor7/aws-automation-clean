import boto3
import sys

ec2 = session.client('ec2')

action = sys.argv[1]
instance_id = sys.argv[2] if len(sys.argv) > 2 else None

if action == "start":
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Instância {instance_id} iniciada!")

elif action == "stop":
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Instância {instance_id} parada!")

elif action == "create":
    response = ec2.run_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
    print("Instância criada!", response['Instances'][0]['InstanceId'])

else:
    print("Ação inválida!")