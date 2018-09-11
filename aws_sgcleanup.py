##This script requires the AWS CLI to be installed and configured to your specific AWS Environment.  It also requires the boto3 
##library to be installed with your version of python.


import boto3
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

sgs = list(ec2.security_groups.all())
insts = list(ec2.instances.all())

all_sgs = set([sg.group_id for sg in sgs])
all_inst_sgs = set([sg['GroupId'] for inst in insts for sg in inst.security_groups])
unused_sgs = all_sgs - all_inst_sgs

print("Total SGs:", len(all_sgs))
print("SGS attached to instances:", len(all_inst_sgs))
print("Orphaned SGs:", len(unused_sgs))
print('Unattached SG names:', unused_sgs)

for group_id in unused_sgs:
	try:
		client.delete_security_group(GroupId=group_id)
		print("Deleted unused group")
	except:
		pass

print("\n \nScript completed. Orphaned SGs may be attached to Network Interfaces or they are default SGs and thus cannot be deleted.")