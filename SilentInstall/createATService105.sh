INFA_HOME=$1
Machine=$2
AT_SERVICE=AT
MRS_SERVICE_NAME=MRS
DIS_SERVICE_NAME=DIS
License_Name=$3
analyst_export_files=/root/export

cd ${INFA_HOME}/isp/bin

echo Creating Analyst service

echo command to create Analyst service ./infacmd.sh as createservice -dn Domain_${Machine} -nn node01_${Machine} -sn ${AT_SERVICE} -un Administrator -pd Administrator -HttpPort 8085 -rs ${MRS_SERVICE_NAME} -ds ${DIS_SERVICE_NAME} -mm ${MM_SERVICE} -au Administrator -ap Administrator -bgefd /home/ora12c/Informatica/PC10.2/export -htds ${DIS_SERVICE_NAME}

./infacmd.sh as createservice -dn Domain_${Machine} -nn node01_${Machine} -sn ${AT_SERVICE} -un Administrator -pd Administrator -HttpPort 8085 -rs ${MRS_SERVICE_NAME} -ds ${DIS_SERVICE_NAME} -au Administrator -ap Administrator -bgefd ${analyst_export_files} -htds ${DIS_SERVICE_NAME}


echo Assign License to Analyst service

echo command is :./infacmd.sh assignLicense -dn Domain_INKR72DSG306 -un Administrator -pd Administrator -ln 10.2.0_License_INKR72DSG306.informatica.com_294 -sn AT_AUTO2

./infacmd.sh assignLicense -dn Domain_${Machine} -un Administrator -pd Administrator -ln ${License_Name} -sn ${AT_SERVICE}

echo Enable Analyst Service

./infacmd.sh EnableService -dn Domain_${Machine} -un Administrator -pd Administrator -sn ${AT_SERVICE}

echo Ping Analyst Service

./infacmd.sh ping -dn Domain_${Machine} -sn ${AT_SERVICE} -nn node01_${Machine} -re 150

export LD_LIBRARY_PATH=${INFA_HOME}/server/bin:$LD_LIBRARY_PATH
