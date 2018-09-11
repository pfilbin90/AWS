#Bash script to install nrpe and nagios plugins as well as copy additional plugins from S3 bucket. This has only been tested against aws Centos7 image.
#Disable SELinux
sed -ie 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
sed -ie 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
reboot