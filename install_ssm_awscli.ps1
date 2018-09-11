#Download Install File 

$source1 = "https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe" 
$source2 = "https://s3.amazonaws.com/aws-cli/AWSCLI64.msi" 
$destination1 = "c:\awstemp\AmazonSSMAgentSetup.exe" 
$destination2 = "c:\awstemp\AWSCLI64.msi" 
  

#Create temp dir 
New-Item -ItemType directory -Path C:\awstemp 

#Download packages 
Invoke-WebRequest $source1 -OutFile $destination1 
Start-Sleep -s 4 
Invoke-WebRequest $source2 -OutFile $destination2 

#Install clients 
#SSM Agent 
Set-Location c:/awstemp 
./AmazonSSMAgentSetup.exe /S /v/qn 

#AWSCLI 
msiexec /l* C:\awstemp\clilog.txt /i c:\awstemp\AWSCLI64.msi /norestart /quiet  


#Start-Sleep -s 4 
#Clean up 

#Remove-Item -path C:\awstemp -recurse 