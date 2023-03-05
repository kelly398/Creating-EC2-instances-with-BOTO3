# Creating-EC2-instances-with-BOTO3
programmatically deploy EC2 resources using AWS python boto3 with python scrypt.
python script will perform the following sub-tasks:
    • The script will retrieve the identifications (subnet IDs) of the six subnets in the default virtual private cloud (VPC). 
    • Then using subnet IDs, the same script will deploy one EC2 instance per each subnet. 
    • The deployment of the EC2 will include User Data to configure httpd websites. 
    • The website landing page should say Hi from (VM’s hostname)
    • Finally, the script will list the identification of the EC2 (instance IDs), the subnet Id the instance is deployed to and instance’s private IPv4 address.
