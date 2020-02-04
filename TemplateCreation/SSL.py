import os,sys
os.system('sudo systemctl status firewalld.service')
os.system('sudo systemctl stop firewalld.service')
os.system('sudo systemctl disable firewalld.service')

###################################################################################
#Disable SELinux on Domain and Hadoop machines.
#####################################################################################

fileReplace = open('/etc/selinux/config','r+')

content = []
filename="/etc/selinux/config"
with open(filename, 'r') as read_file:
    content = read_file.readlines()

with open(filename, 'w') as write_file:
    for line in content:
        write_file.write(line.replace("SELINUX=enforcing", "SELINUX=disabled"))
fileReplace.close()

###########################################################################################
#  Start the ntpd service and Verify that the ntpstat utility reports a synchronized status on Domain and Hadoop machines.
###########################################################################################
os.system('ntpstat')
os.system('sudo systemctl restart ntpd')