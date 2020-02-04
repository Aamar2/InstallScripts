import os
import sys
import fileinput
from subprocess import Popen, PIPE
limits = ['*               soft    nofile          100000','*               hard    nofile          100000','*               soft    nproc           100000','*               hard    nproc           100000','*               soft    stack           25000','*               hard    stack           25000']
f = open("/etc/security/limits.conf","a+")
for x in limits:
	f.write(x)
	f.write('\n')

f.close()


#############################################################################################################
#/etc/security/limits.d/20-nproc.conf
#############################################################################################################
fileReplace = open('/etc/security/limits.d/20-nproc.conf','r+')

content = []
filename="/etc/security/limits.d/20-nproc.conf"
with open(filename, 'r') as read_file:
    content = read_file.readlines()

with open(filename, 'w') as write_file:
    for line in content:
        write_file.write(line.replace("4096", "100000"))
fileReplace.close()

#############################################################################################################
#add hostname to etc/hosts and /etc/sysconfig/network
#############################################################################################################
nodeIP = '10.65.164.22'
nodeHostName = 'invr75dsg1084.informatica.com'
nodeName = 'invr75dsg1084'

hadoopIP = '10.65.164.21'
hadoopHostName = 'invr75dsg1083.informatica.com'
hadoopName = 'invr75dsg1083'

nodeEntry = nodeIP + '\t'+ nodeHostName + '\t' + nodeName
print(nodeEntry)
hadoopEntry = hadoopIP + '\t'+ hadoopHostName + '\t' + hadoopName
print(hadoopEntry)

etcFile = open('/etc/hosts','a+')
etcFile.write('\n')
etcFile.write(nodeEntry)
etcFile.write('\n')
etcFile.write(hadoopEntry)
etcFile.close()

#################################################################################################################
#/etc/sysconfig/network should contain fully qualified host name on Hadoop machine.       /etc/sysconfig/network should have the same entry as that of hostname -f
#################################################################################################################

hostname = "HOSTNAME="+nodeHostName
networkFile = open('/etc/sysconfig/network','a+')
networkFile.write(hostname)
networkFile.close()






