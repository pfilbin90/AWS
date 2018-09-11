##these libraries are used in the different functions and must be imported for the script to work.
import boto3
import requests
import json
import time

#this function will take the cloudwatch event of an instance terminating and extract the instance-id from the event
## you can view a sample cloudwatch event output by checking the Rule in cloudwatch
def get_instance_id(event):
          return event['detail']['instance-id']

#this function first authenticates to centreon, then it takes the converted instance_name and 
#plugs it into the centreon rest API to delete the host out of centreon
def centreon_api_del(cent_inst_name):
    postdata = {'username':'insert_username_here','password':'insert_password_here'}
    CentreonURL = 'http://10.10.1.220/centreon/api/index.php?action=authenticate'
    response = requests.post(CentreonURL, data=postdata)
    authData = json.loads(response.text)
    reqheaders = {'centreon-auth-token':authData["authToken"]}
    requestbody = {'action':'del', 'object':'host', 'values':cent_inst_name}
    jsonrequestbody = json.dumps(requestbody)
    CentreonURL = "http://10.10.1.220/centreon/api/index.php?action=action&object=centreon_clapi"
    response = requests.post(CentreonURL, data=jsonrequestbody, headers=reqheaders)
    error_text = response.text
    error_code = response.status_code
    print(response.text)
    print(response.status_code)
    time.sleep(5)
    
    ##This function uses AWS's EC2 Run Command feature to send the reload command to Centreon poller ##
    def ssmsendcommand():
        ssm = boto3.client('ssm')
        command = ssm.send_command( 
            InstanceIds=[
                'i-0fd2d9c2b893388ac',
            ],
            DocumentName='AWS-RunShellScript',
            Comment='Reloading Prod Centreon Poller',
            Parameters={
                'commands': [
                    'sudo ./centreon -u aws_lambda -p kibo123$ -a APPLYCFG -v "Central"',
                ],
                'workingDirectory': [
                    '/usr/share/centreon/bin', 
                ]
            },
        )
        print(command)
        return
    
    ## this function-within-a-function will notify SNS if there is a failure with the function above
    def notify_when_bad(error_code, error_text):
        sns = boto3.client(service_name="sns")
        topicArn = 'arn:aws:sns:us-east-1:812040210293:CentreonInstanceDeleted'
        
        if response.status_code == 200:
            ssmsendcommand()
            sns.publish(
                TopicArn = topicArn, 
                Message = (str("The Prod Instance ") + str(cent_inst_name) + str(" has been successfully removed from Centreon")))
        else:
            sns.publish(
                TopicArn = topicArn, 
                Message = (str("Function failed with msg:") + str(error_text) + '\n' + str("Status Code:") + str(error_code)))
        return
    print(notify_when_bad(error_code, error_text))
    return error_text
    

## This is the lambda_handler function which is required for AWS lambda.  All other functions must be called from this one.
## It also servers to extract the instance_name from it's metadata tag: Name.  Then it adds it into a variable (which 
#is called in the function at the top of this script)
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = get_instance_id(event)
    response = ec2.describe_tags(
        Filters=[
        {
         'Name': 'resource-id',
         'Values': [instance_id,]
        },
        ]
        )

    for tag in response["Tags"]:
      if tag['Key'] == 'Name':
        cent_inst_name = tag['Value']
    
    return centreon_api_del(cent_inst_name)