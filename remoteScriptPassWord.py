import sys
import os,time
home = os.environ['HOME']
hadoopHostName = os.uname()[1]
hadoopUserName = sys.argv[1]
hadoopPassword = sys.argv[2]

os.system('sudo yum install python-setuptools -y')
os.system('sudo wget https://bootstrap.pypa.io/get-pip.py')
os.system('sudo python get-pip.py')


os.system('sudo pip install pexpect')
import pexpect
os.system('if [ -d '+home+'/.ssh ]; then rm -rf '+home+'/.ssh; fi')
os.system('if [ ! -d '+home+'/.ssh ]; then mkdir '+home+'/.ssh; fi')
os.system('echo | ssh-keygen -t rsa -P \'\'')
os.system('chmod 700 -R '+home+'/.ssh')
child = pexpect.spawn('ssh-copy-id -i '+home+'/.ssh/id_rsa.pub '+hadoopUserName+'@'+hadoopHostName)
time.sleep(1)
child.expect('Are you sure you want to continue connecting.*')
child.sendline('yes')
child.expect('password:.*')
child.sendline(hadoopPassword)
print(child.before)
child2 = pexpect.spawn('ssh-copy-id -i '+home+'/.ssh/id_rsa.pub '+hadoopUserName+'@'+hadoopHostName)
try:
	child2.expect('Are you sure you want to continue connecting.*')
	child2.sendline('yes')
except:
 	print("cool")
try:
	child2.expect('password:.*')
	child2.sendline(hadoopPassword)
except:
	print("cool")

child_ssh = pexpect.spawn('ssh '+hadoopUserName+'@'+hadoopHostName)
try:
	child_ssh.sendline('yes')
except:
 	print("cool")

os.system('ssh -o StrictHostKeyChecking=no '+hadoopUserName+'@'+hadoopHostName)

