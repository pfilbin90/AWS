# Download the file to a specific location 

$source = "https://s3.amazonaws.com/amazoncloudwatch-agent/windows/amd64/latest/AmazonCloudWatchAgent.zip" 
$destination = "C:\Program Files\Amazon\AmazonCloudWatchAgent\AmazonCloudWatchAgent.zip" 
$outpath = "C:\Program Files\Amazon\AmazonCloudWatchAgent" 

Split-Path $MyInvocation.MyCommand.Path 
Write-Host "InstallScript:" $MyInvocation.InstallScript 
Write-Host "Path:" $MyInvocation.MyCommand.Path 

try{  
    New-Item -ItemType directory -Path 'C:\Program Files\Amazon\AmazonCloudwatchAgent'  
    else{Write-Host "Directory already created"}  
}  

catch {Write-Host "Directory already created"} 
Invoke-WebRequest -Uri $source -OutFile $destination 

# Unzip the file to specified location 

Add-Type -AssemblyName System.IO.Compression.FileSystem 
function Unzip 
{ 
    param([string]$destination, [string]$outpath) 
    [System.IO.Compression.ZipFile]::ExtractToDirectory($destination, $outpath) 
} 
try{ 
    Unzip "C:\Program Files\Amazon\AmazonCloudWatchAgent\AmazonCloudWatchAgent.zip" "C:\Program Files\Amazon\AmazonCloudWatchAgent" 
    else{Write-Host "Files already unzipped"} 
} 
catch{Write-Host "Files already unzipped"} 

cmd.exe /C cd "C:\Program Files\Amazon\AmazonCloudwatchAgent" 
#cmd.exe /C .\amazon-cloudwatch-agent-ctl.ps1 -a fetch-config -m ec2 -c ssm:AmazonCloudwatch_Prod-Int -s 
& ((Split-Path $MyInvocation.InvocationName) + "\install.ps1") 