#import pexpect
import os
import time


#os.putenv('INFA_JDK_HOME','/d01/oracle/openJDK1.8/java-1.8.0-openjdk-1.8.0.191.b12-0.el6_10.x86_64')
os.putenv('DB_REPO_TYPE','Oracle')
###############################################################
#		Domain Details and Variables
###############################################################
Hostname = os.uname()[1]
DomainSuffix = '104'
BuildVersion = '1040'
DomainName = 'Domain_'+DomainSuffix
NodeName = 'node01_'+DomainSuffix
Version = '10.4.0'
BuildLocation = '/home/Builds/10.4'
INFA_HOME='/home/Informatica/10.4.0'
Build_Location='/home/temp'
silentInputFileLoc=Build_Location+'/SilentInput.properties'
silentInputFileLoc_BackUp=Build_Location+'/SilentInput.properties_BackUp'
Lincense_File_Path = os.getcwd()+'/License.key'
BUILD_NO='27'
License_Name=Version+'_License_'+Hostname+'_422'
Machine = Hostname.split('.')[0]

##################################
#	DB Details -Local
##################################
HostName = 'invr70dsg952'
Port = '1521'
ServiceName = 'ora11gR2'
DBUserName = 'd102HF2'
DBPassword = 'd102HF2'
DomainUserName = 'D105_'+Machine
DomainPassword = 'D105_'+Machine
MRSUserName = 'M105_'+Machine
MRSPassword = 'M105_'+Machine

##################################
#	DB Details -Oracle18c
##################################
#HostName = 'invr75dsg997.informatica.com'
#Port = '1521'
#ServiceName = 'orcl.informatica.com'
#DomainUserName = 'DOM176'
#DomainPassword = 'DOM176'
#MRSUserName = 'MRS176'
#MRSPassword = 'MRS176'


##################################################
#    Scripts location
##################################################
currentFolder = os.getcwd()
copyFilePath = os.getcwd()+'/copy105.sh'
deletePath = os.getcwd()+'/deleteInfaHome.sh'
stopDomain = os.getcwd()+'/stopDomain.sh'
CleanRepo = os.getcwd()+'/CleanDBRepos.sh'
CreateATService = os.getcwd()+'/createATService105.sh'
CreateSearchService = os.getcwd()+'/createSearchService105.sh'

###############################################################
#		copy build to local folder
###############################################################

'''if(os.path.exists(BuildLocation)):
	print('folder exists')
	os.system('sudo umount -f /home/Builds/10.5')
	time.sleep(20)
	os.system('sudo mount -t nfs innfs1:/vol/infastore/10.4.0/build.'+BUILD_NO+'/lin-x64 '+BuildLocation)
	time.sleep(20)
'''



###############################################################
#		Remove existing infa folder
###############################################################

os.system('sh '+deletePath+' '+stopDomain+ ' '+DomainName+' '+INFA_HOME)
###############################################################
#		Copy build to temp location
###############################################################
#os.system('sh '+copyFilePath+' '+BuildLocation+' '+Build_Location+' '+BuildVersion)
#os.system('sh '+CleanRepo)
time.sleep(1)

'''
def waitForMessage(inputMessage,timeout):
    try:
    	child.expect(inputMessage,timeout=timeout)
    except pexpect.TIMEOUT :
        child.expect(inputMessage,timeout=timeout)

def enterText(inputText):
    child.sendline(inputText)

'''
#Build_Location = '/home/ora12c/jenkins_slave1/workspace/PCInstall_1022_AT/PC_Installer_Build/temp/informatica_1022_server_linux-x64.316'

#############################################################

##                Remove and Create DB users ################

#############################################################

os.system('java -jar RemoveUser.jar '+ HostName + ' ' + ServiceName + ' ' + DBUserName + ' ' + DBPassword + ' ' + DomainUserName)
os.system('java -jar AddUser.jar '+ HostName + ' ' + ServiceName + ' ' + DBUserName + ' ' + DBPassword + ' ' + DomainUserName + ' ' + DomainPassword)
os.system('java -jar RemoveUser.jar '+ HostName + ' ' + ServiceName + ' ' + DBUserName + ' ' + DBPassword + ' ' + MRSUserName)
os.system('java -jar AddUser.jar '+ HostName + ' ' + ServiceName + ' ' + DBUserName + ' ' + DBPassword + ' ' + MRSUserName + ' ' + MRSPassword)

########################################
 
 ## Updating the silentInput.properties File for Silent Installation

###############################################
os.system('cp '+silentInputFileLoc+' '+silentInputFileLoc_BackUp)

fin = open(silentInputFileLoc, "rt")
data = fin.read()
############# Update Installation details   ############

data = data.replace('ENABLE_USAGE_COLLECTION=0','ENABLE_USAGE_COLLECTION=1')
data = data.replace('LICENSE_KEY_LOC=/home/license.key','LICENSE_KEY_LOC='+Lincense_File_Path)
data = data.replace('USER_INSTALL_DIR=/home/Informatica/10.4.0','USER_INSTALL_DIR='+INFA_HOME)
data = data.replace('KEY_DEST_LOCATION=/home/Informatica/10.4.0','KEY_DEST_LOCATION='+INFA_HOME)
data = data.replace('PASS_PHRASE_PASSWD=','PASS_PHRASE_PASSWD=Infa@123')


############# MRS Strings replacement  ############
data = data.replace('MRS_DB_UNAME=UserName','MRS_DataBase_UNAME=UserName')
data = data.replace('MRS_DB_PASSWD=UserPassword','MRS_DataBase_PASSWD=UserPassword')
data = data.replace('MRS_DB_SERVICENAME=DBServiceName','MRS_DataBase_SERVICENAME=DBServiceName')
data = data.replace('MRS_DB_ADDRESS=HostName:PortNumber','MRS_DataBase_ADDRESS=HostName:PortNumber')
data = data.replace('MRS_DB_TYPE=Oracle/MSSQLServer/DB2/PostgreSQL','MRS_DB_TYPE=Oracle')
############  Domain Configuration ############

data = data.replace('DB_TYPE=Oracle/MSSQLServer/DB2/Sybase/PostgreSQL','DB_TYPE=Oracle')
data = data.replace('DB_UNAME=UserName','DB_UNAME='+DomainUserName)
data = data.replace('DB_PASSWD=UserPassword','DB_PASSWD='+DomainPassword)
data = data.replace('DB_SERVICENAME=DBServiceName','DB_SERVICENAME='+ServiceName)
data = data.replace('DB_ADDRESS=HostName:PortNumber','DB_ADDRESS='+HostName+':'+Port)
data = data.replace('DOMAIN_NAME=DomainName','DOMAIN_NAME='+DomainName)
data = data.replace('DOMAIN_HOST_NAME=HostName','DOMAIN_HOST_NAME='+Hostname)
data = data.replace('NODE_NAME=NodeName','NODE_NAME='+NodeName)
data = data.replace('DOMAIN_USER=AdminUser','DOMAIN_USER=Administrator')
data = data.replace('DOMAIN_PSSWD=','DOMAIN_PSSWD=Administrator')
data = data.replace('DOMAIN_CNFRM_PSSWD=','DOMAIN_CNFRM_PSSWD=Administrator')
##############  MRS CONFIG   ############
data = data.replace('CREATE_SERVICES=0','CREATE_SERVICES=1')
data = data.replace('MRS_DataBase_UNAME=UserName','MRS_DB_UNAME='+MRSUserName)
data = data.replace('MRS_DataBase_PASSWD=UserPassword','MRS_DB_PASSWD='+MRSPassword)
data = data.replace('MRS_DataBase_SERVICENAME=DBServiceName','MRS_DB_SERVICENAME='+ServiceName)
data = data.replace('MRS_DataBase_ADDRESS=HostName:PortNumber','MRS_DB_ADDRESS='+HostName+':'+Port)
data = data.replace('MRS_SERVICE_NAME=Model_Repository_Service','MRS_SERVICE_NAME=MRS')
############   DIS CONFIG  ############

data = data.replace('DIS_SERVICE_NAME=Data_Integration_Service','DIS_SERVICE_NAME=DIS')
data = data.replace('DIS_HTTP_PORT=','DIS_HTTP_PORT=9085')
fin.close()
###################################################################################################
###############   Write to File  ############
fin = open(silentInputFileLoc, "wt")
fin.write(data)
fin.close()

os.chdir(Build_Location)
os.system('unset DISPLAY')
os.system('unset DISPLAY')
os.system('unset INFA_NODE_NAME')
os.system('unset INFA_DOMAINS_FILE')

os.system('sh silentinstall.sh')

###############  Check the Installation status  ############
files = os.listdir(INFA_HOME)
for file in files:
	if('_'+Version+'_Services_' in file):
		logFile=open(INFA_HOME+'/'+file,'rt')
		output=logFile.read()
if('Installation Status: SUCCESS' in output):
   print("installation successful")
   os.system('sh '+CreateATService+' '+INFA_HOME+' '+DomainSuffix+' '+License_Name)
   os.system('sh '+CreateSearchService+' '+INFA_HOME+' '+DomainSuffix+' '+License_Name)
else:
   print("installation failed with below error")
   print(output)



