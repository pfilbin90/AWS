#install epel release
echo -n "[-] Installing epel-release and nrpe packages: "
yum install -y epel-release
#Install nrpe packages
yum install -y nrpe
yum install -y nagios-plugins-all
#Install pip and aws cli
echo -n "[-] Installing pip and aws cli: "
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
export PATH=~/.local/bin:$PATH
source ~/.bash_profile
pip install awscli --upgrade --user
rm -rf get-pip.py
#Copy additional Nagios Plugins from S3 bucket
echo -n "[-] Copying Plugins and Config from S3: "
aws s3 cp --recursive s3://{yours3URLhere} /usr/lib64/nagios/plugins/
aws s3 cp s3://{yours3URLhere}/nrpe.cfg /etc/nagios/
#Give plugins folder proper permissions
chmod -R 775 /usr/lib64/nagios/plugins
chmod 4775 /usr/lib64/nagios/plugins/check_fping
chmod 4775 /usr/lib64/nagios/plugins/check_icmp
#Start the nrpe service
echo -n "[-] Starting NRPE service: "
systemctl start nrpe