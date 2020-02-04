import os,time

op_wget = os.system('rpm -qa | grep wget')
if op_wget == 0:
	print("installed")
else:
	print("not installed")
	os.system('sudo yum -y install wget')

op_nfs = os.system('rpm -qa | grep nfs-utils')
if op_nfs == 0:
	print("nfs installed")
else:
	print("nfs not installed..so installing")
	os.system('sudo yum -y install nfs-utils')

op_curl = os.system('rpm -qa | grep curl')
if op_curl == 0:
	print("nfs installed")
else:
	print("curl not installed..so installing")
	os.system('sudo yum -y install curl')


op_rpm = os.system('rpm -qa | grep rpm')
if op_rpm == 0:
	print("nfs installed")
else:
	print("rpm not installed..so installing")
	os.system('sudo yum -y install rpm')

op_scp = os.system('rpm -qa | grep scp')
if op_scp == 0:
	print("nfs installed")
else:
	print("scp not installed..so installing")
	os.system('sudo yum -y install scp')

op_ssh = os.system('rpm -qa | grep ssh')
if op_ssh == 0:
	print("nfs installed")
else:
	print("ssh not installed..so installing")
	os.system('sudo yum -y install ssh')


op_tar = os.system('rpm -qa | grep tar')
if op_tar == 0:
	print("nfs installed")
else:
	print("tar not installed..so installing")
	os.system('sudo yum -y install tar')

op_zip = os.system('rpm -qa | grep zip')
if op_zip == 0:
	print("nfs installed")
else:
	print("zip not installed..so installing")
	os.system('sudo yum -y install zip')

op_unzip = os.system('rpm -qa | grep unzip')
if op_unzip == 0:
	print("nfs installed")
else:
	print("unzip not installed..so installing")
	os.system('sudo yum -y install unzip')

op_awk = os.system('rpm -qa | grep awk')
if op_awk == 0:
	print("nfs installed")
else:
	print("awk not installed..so installing")
	os.system('sudo yum -y install awk')

op_ntp = os.system('rpm -qa | grep ntp')
if op_ntp == 0:
	print("nfs installed")
else:
	print("ntp not installed..so installing")
	os.system('sudo yum -y install ntp')

op_lsof = os.system('rpm -qa | grep lsof')
if op_lsof == 0:
	print("nfs installed")
else:
	print("lsof not installed..so installing")
	os.system('sudo yum -y install lsof')

op_mount = os.system('rpm -qa | grep mount')
if op_mount == 0:
	print("nfs installed")
else:
	print("lsof not installed..so installing")
	os.system('sudo yum -y install mount')

op_rsync = os.system('rpm -qa | grep rsync')
if op_rsync == 0:
	print("nfs installed")
else:
	print("rsync not installed..so installing")
	os.system('sudo yum -y install rsync')

op_nettools = os.system('rpm -qa | grep net-tools')
if op_nettools == 0:
	print("nfs installed")
else:
	print("net-tools not installed..so installing")
	os.system('sudo yum -y install net-tools')

op_kerneldevel = os.system('rpm -qa | grep kernel-devel')
if op_kerneldevel == 0:
	print("nfs installed")
else:
	print("kernel-devel not installed..so installing")
	os.system('sudo yum -y install kernel-devel')

op_kernelheaders = os.system('rpm -qa | grep kernel-headers')
if op_kernelheaders == 0:
	print("nfs installed")
else:
	print("kernel-headers not installed..so installing")
	os.system('sudo yum -y install kernel-headers')

op_openssl = os.system('rpm -qa | grep openssl')
if op_openssl == 0:
	print("nfs installed")
else:
	print("openssl not installed..so installing")
	os.system('sudo yum -y install openssl')

op_pDevel = os.system('rpm -qa | grep python-devel')
if op_pDevel == 0:
	print("nfs installed")
else:
	print("openssl not installed..so installing")
	os.system('sudo yum -y install python-devel')

op_pLibs = os.system('rpm -qa | grep python-libs')
if op_pLibs == 0:
	print("nfs installed")
else:
	print("openssl not installed..so installing")
	os.system('sudo yum -y install python-libs')



op_allRpms = os.system('sudo rpm -q curl rpm scp ssh tar zip unzip awk ntp wget lsof rsync net-tools openssl | grep not')
print(op_allRpms)


##############################################################################################################
#### Create mount on Domain and Hadoop machines
##############################################################################################################

if(os.path.exists('$HOME/SATSBuild')):
	print('folder exists')
	os.system('sudo mount -t nfs inkr73dsg679:/blddmp $HOME/SATSBuild')
	time.sleep(20)
else:
	os.system('mkdir $HOME/SATSBuild')
	os.system('sudo mount -t nfs inkr73dsg679:/blddmp $HOME/SATSBuild')
	time.sleep(20)
op_libtirpc = os.system('rpm -qa | grep libtirpc')
if op_libtirpc == 0:
	print("installed")
else:
	print("installing")
	os.system('sudo yum -y install $HOME/SATSBuild/Others/libtirpc-0.2.4-0.10.el7.x86_64.rpm')

op_devel = os.system('rpm -qa | grep libtirpc-devel')
if op_devel == 0:
	print("installed")
else:
	print("installing")
	os.system('sudo yum -y install $HOME/SATSBuild/Others/libtirpc-devel-0.2.4-0.10.el7.x86_64.rpm')




