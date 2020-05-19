import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    
    filters = [{'Name':'tag:Backup-AMI', 'Values':['yes']}]
    
    instances = client.describe_instances(Filters=filters)
    
    if instances and instances['Reservations']:
        for i in instances['Reservations'][0]['Instances']:
            instance_id = i['InstanceId']
            name = "Image for instance {instance_id}".format(instance_id=instance_id)
            print "creating image for instance {instance_id}".format(instance_id=instance_id)
            client.create_image(InstanceId=instance_id,Name=name)
