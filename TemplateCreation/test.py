import os
import pexpect

hadoopIP = '10.65.164.21'
hadoopHostName = 'invr75dsg1083.informatica.com'
hadoopName = 'invr75dsg1083'

os.system('cd $HOME')
os.system('rm -rf /root/.ssh')
os.system('mkdir /root/.ssh')
os.system('chmod -R 700 /root/.ssh')
os.system('echo | ssh-keygen -t rsa -P \'\'')
#os.system('ssh-copy-id -i /root/.ssh/id_rsa.pub root@'+hadoopHostName)
print('ssh-copy-id -i /root/.ssh/id_rsa.pub root@'+hadoopHostName)
child = pexpect.spawn('ssh-copy-id -i /root/.ssh/id_rsa.pub root@'+hadoopHostName)
child.logfile = open("/root/pexpect-2.3/LDM/mylog", "w")
child.expect('Are you sure you want to continue connecting.*')
child.sendline('yes')
child.expect('password:.*')
child.sendline('Infa@123')
print(child.before)
child_ssh = pexpect.spawn('ssh root@'+hadoopHostName)
print(child.before)
