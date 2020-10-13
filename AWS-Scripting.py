import boto3

ec2= boto3.resource('ec2')
'''
instance= ec2.create_instances (
    ImageId='ami-0eb7fbcc77e5e6ec6',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')

print(instance[0].id)

'''

instance_id="i-0c01ed6083926e70c"
instance=ec2.Instance(instance_id)
response=instance.terminate()

print(response)
