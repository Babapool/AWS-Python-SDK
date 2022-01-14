import boto3

def create_instance():
    ec2 = boto3.resource('ec2')

    # create a new EC2 instance
    instances = ec2.create_instances(
         ImageId='ami-0ed9277fb7eb570c9',
         MinCount=1,
         MaxCount=2,
         InstanceType='t2.micro',
         KeyName='ec2-keypair',
         SecurityGroups=['custom-launch-wizard-2'],
         UserData='#!/bin/sh sudo yum install httpd -y service httpd start mkdir /var/www/html/images mkdir /var/www/html/videos echo "<html><head></head><body><b><h1>You are in Instance $HOSTNAME in General Target group </body></html>" > /var/www/html/index.html echo "<html><head></head><body><b><h1>You are in Instance $HOSTNAME in Images Target group </body></html>" > /var/www/html/images/index.html echo "<html><head></head><body><b><h1>You are in Instance $HOSTNAME in Videos Target group </body></html>" > /var/www/html/videos/index.html')

    for instance in instances:
        print(f'EC2 instance "{instance.id}" has been launched')
        instance.wait_until_running()
        print(f'EC2 instance "{instance.id}" has been started')


def describe_instance():
    ec2= boto3.client('ec2')
    response = ec2.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'], i['ImageId'], i['KeyName'], i['InstanceType'], i['LaunchTime'], i['PublicIpAddress'], i['PrivateIpAddress'], i['PublicDnsName'], i['PlatformDetails'], i['InstanceType'])


def stop_specific_instance():
    ec2= boto3.resource('ec2')

    print("\n All the running Instances")

    ec21= boto3.client('ec2')
    response = ec21.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'])

    id=input("\nEnter the Instance ID of the Instance you want to stop: ")
    instance = ec2.Instance(id)
    instance.stop()
    print(f'Stopping EC2 instance: {instance.id}')
    instance.wait_until_stopped()
    print(f'EC2 instance "{instance.id}" has been stopped')

def start_specific_instance():
    ec2= boto3.resource('ec2')
    print("\n All the stopped Instances")
    
    ec21= boto3.client('ec2')
    response = ec21.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["stopped"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'])

    id=input("\nEnter the Instance ID of the Instance you want to start: ")
    instance = ec2.Instance(id)
    instance.start()
    print(f'Starting EC2 instance: {instance.id}')
    instance.wait_until_running()
    print(f'EC2 instance "{instance.id}" has been started')

def terminate_specific_instance():
    ec2= boto3.resource('ec2')
    print("\n All the Instances")

    ec21= boto3.client('ec2')
    response = ec21.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running","stopped"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'])

    id=input("\nEnter the Instance ID of the Instance you want to terminate: ")
    instance = ec2.Instance(id)
    instance.terminate()
    print(f'Terminating EC2 instance: {instance.id}')
    instance.wait_until_terminated()
    print(f'EC2 instance "{instance.id}" has been terminated')

def stop_all_instances():
    ec2= boto3.client('ec2')
    response = ec2.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            n = i['InstanceId']
            res=ec2.stop_instances(InstanceIds=[n])
            

    print("\nAll running instances have been stopped")

def start_all_instances():
    ec2= boto3.client('ec2')
    response = ec2.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["stopped"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            n = i['InstanceId']
            res=ec2.start_instances(InstanceIds=[n])


    print("\nAll running instances have been stopped")

def terminate_all_instances():
    ec2= boto3.client('ec2')
    response = ec2.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running","stopped"],
        }
    ])
    for r in response['Reservations']:
        for i in r['Instances']:
            n = i['InstanceId']
            res=ec2.terminate_instances(InstanceIds=[n])


    print("\nAll instances have been terminated")



while True:
    print ("\nAWS EC2-Instances Menu")
    print ("\n1. Launch Instance")
    print ("\n2. Describe running Instances")
    print ("\n3. Stop a specific instance")
    print ("\n4. Start a specific instance")
    print ("\n5. Terminate a specific instance")
    print ("\n6. Stop all Instances")
    print ("\n7. Start all Instances")
    print ("\n8. Terminate all Instances")
    print ("\n9. Exit")
    choice = int(input("\nEnter the Choice: ")) 

    if choice==1:
        create_instance()

    elif choice==2:
        describe_instance()

    elif choice==3:
        stop_specific_instance()

    elif choice==4:
        start_specific_instance()

    elif choice==5:
        terminate_specific_instance()

    elif choice==6:
        stop_all_instances()

    elif choice==7:
        start_all_instances()

    elif choice==8:
        terminate_all_instances()

    elif choice==9:
        break

    else:
        print ("Provide a Valid Input")


