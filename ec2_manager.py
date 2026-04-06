import boto3
import sys

session = boto3.Session(region_name='us-east-1')
ec2 = session.client('ec2')

action = sys.argv[1]

INSTANCE_ID = "SEU_INSTANCE_ID_AQUI"

if action == "start":
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("Instância iniciada!")

elif action == "stop":
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("Instância parada!")

elif action == "create":
    response = ec2.run_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
    print("Instância criada!", response['Instances'][0]['InstanceId'])

else:
    print("Ação inválida!")