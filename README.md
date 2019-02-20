# AWS
The scripts in this directory are mixed-use for Systems Engineering with AWS.


| Script Name   | Language      | Description  |
| ------------- |:-------------:| :-----|
| aws_sgcleanup.py | python | Finds unused and orphaned AWS security groups and lists them out by name |
| getSSLexpiring.py | python | Quick AWS Lambda function to find the expiration date of a domains SSL cert |
| centreonautomation_final.py | python | AWS Lambda function that removes a host from a Centreon (Nagios) Server after Cloudwatch Termination log entry
| download_unzip_CloudwatchAgent.ps1 | powershell | Installs AmazonCloudwatchAgent to a Windows host; for use with AWS EC2 (was deployed to production via Octopus). Cloudwatch Agent allows for more enhanced metrics (most noteably, Memory usage within EC2)
|install_ssm_awscli.ps1 | powershell | Installs AmazonSSMAgent to a Windows host; for use with AWS EC2
| step1_uninstallSELinux.sh | bash | Uninstalls SELinux on Centos machines to prep for Nagios nrpe agent
step2_prephost4centreon.sh | bash | Installs pip, AWS CLI, and nagios plugins for nrpe/nagios/centreon