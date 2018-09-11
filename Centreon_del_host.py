import requests
import json
postdata = {
  'username':'aws_lambda',
  'password':'kibo123$'
  }
CentreonURL = 'http://centreon.yourdomainhere.com/centreon/api/index.php?action=authenticate'
response = requests.post(CentreonURL, data=postdata)
authData = json.loads(response.text)
reqheaders = {'centreon-auth-token':'authData'}
requestbody = {'action':'del', 'object':'host', 'values':'v1alpgsmon03'}
jsonrequestbody = json.dumps(requestbody)
CentreonURL = "http://centreon.prod.kibocommerce.com/centreon/api/index.php?action=action&object=centreon_clapi"
response = requests.post(CentreonURL, data=jsonrequestbody, headers=reqheaders)
print response.status_code
print response.text