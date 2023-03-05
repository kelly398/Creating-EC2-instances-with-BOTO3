import boto3

user_data = """#!/bin/bash
echo "Hi from $(hostname)" > /var/www/html/index.html
echo "yourkeyname" >> /var/www/html/index.html
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2
sudo yum install -y httpd mariadb-server
sudo systemctl start httpd
sudo systemctl enable httpd
"""
#replace "yourkeyname" withyour pem key

ec2 = boto3.resource('ec2')

vpc = list(ec2.vpcs.filter(Filters=[{'Name': 'isDefault', 'Values': ['true']}]))[0]

subnets = [subnet.id for subnet in vpc.subnets.all()]

sg = ec2.create_security_group(
    GroupName='security_group1',
    Description='Allow HTTP traffic',
    VpcId=vpc.id
)
sg.authorize_ingress(
    IpPermissions=[
        {
            'FromPort': 22,
            'ToPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                }
            ]
        }
    ]
)

instances = []
for subnet_id in subnets:
    instance = ec2.create_instances(
        ImageId='ami-12345689101112', # replace with your amazon AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='yourkeyname',
        SecurityGroupIds=[sg.id],
        SubnetId=subnet_id,
        UserData=user_data
    )
    instances.extend(instance)
for instance in instances:
    print(f"Instance ID: {instance.id}")
    print(f"Subnet ID: {instance.subnet_id}")
    print(f"Private IPv4 address: {instance.private_ip_address}")
