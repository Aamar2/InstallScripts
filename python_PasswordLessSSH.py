###################################################################################################################
## Passwordless SSH
##################################################################################################################


import os
home = os.environ['HOME']
os.system('sudo yum install python-setuptools -y')
os.system('sudo wget https://bootstrap.pypa.io/get-pip.py')
os.system('sudo python get-pip.py')
os.system('sudo yum install redhat-rpm-config gcc libffi-devel python-devel openssl-devel -y')
os.system('sudo pip install cryptography --no-binary cryptography')
os.system('sudo pip install bcrypt')
os.system('sudo pip install pynacl')
os.system('sudo pip install paramiko')
os.system('sudo pip install pexpect')
import paramiko
import pexpect

#hadoopIP = '10.xx.xxx.xxx'
#hadoopIP = '10.xx.xxx.xxx'
#hadoopHostName = 'machine1.informatica.com'
#hadoopHostName = 'machine2.informatica.com'
hadoopHostName = os.environ['Hadoop_Gateway_Host']
hadoopUserName = os.environ['Hadoop_Gateway_User']
hadoopPassword = os.environ['Hadoop_Gateway_User_Password']



hadoopName = 'machine1'

### Method for read content #################
def readFile(filename):
 fileReplace = open(filename,'r+')
 with open(filename, 'r') as read_file:
    rsaKeyValue = read_file.readlines()
 fileReplace.close()
 return rsaKeyValue


########## Disable SSH Host Key Checking #############################
accessAllHosts = 'Host *'
StrictHostKeyChecking = '   StrictHostKeyChecking no'
UserKnownHostsFile = '   UserKnownHostsFile=/dev/null'


###########################################################################################

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hadoopHostName,username=hadoopUserName,password=hadoopPassword)

###### Copy files to remote machine i.e Hadoop machine ######################################3

ftp_client=ssh.open_sftp()
ftp_client.put('remoteScriptPassWord.py','remoteScriptPassWord.py')
ftp_client.close()


################# Execute the python script on remote machine ################################

ssh.exec_command('python remoteScriptPassWord.py '+ hadoopUserName + ' ' + hadoopPassword)
ssh.close()
############# Execute ssh commands in local machine ##########################################

os.system('cd '+home)
os.system('rm -rf '+home+'/.ssh')
os.system('mkdir '+home+'/.ssh')
os.system('chmod -R 700 '+home+'/.ssh')	
os.system('echo | ssh-keygen -t rsa -P \'\'')
content_file=readFile(home+'/.ssh/id_rsa.pub')
content=content_file[0]
##################### remote content update #################################################
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hadoopHostName,username=hadoopUserName,password=hadoopPassword)
rsaText=content
print(content)
#ssh.exec_command("echo '{}' >> /export/home/oracle/.ssh/authorized_keys".format(rsaText))
#ssh.exec_command('chmod 700 /export/home/oracle/.ssh/authorized_keys')

ssh.exec_command("echo '{}' >> ~/.ssh/authorized_keys".format(rsaText))
ssh.exec_command('chmod 700 ~/.ssh/authorized_keys')

ssh.exec_command("echo '{}' >> ~/.ssh/config".format(accessAllHosts))
ssh.exec_command("echo '{}' >> ~/.ssh/config".format(StrictHostKeyChecking))
ssh.exec_command("echo '{}' >> ~/.ssh/config".format(UserKnownHostsFile))
ssh.exec_command('chmod 700 ~/.ssh/config')

ssh.close()
################## Create remote folder for test ##########################################
os.system("echo '{}' >> ~/.ssh/config".format(accessAllHosts))
os.system("echo '{}' >> ~/.ssh/config".format(StrictHostKeyChecking))
os.system("echo '{}' >> ~/.ssh/config".format(UserKnownHostsFile))
os.system('chmod 700 ~/.ssh/config')

os.system('ssh -o StrictHostKeyChecking=no '+ hadoopUserName + '@' + hadoopHostName)