INFA_HOME=$1
Machine=$2
SEARCH_SERVICE=SS
MRS_SERVICE_NAME=MRS
DIS_SERVICE_NAME=DIS
License_Name=$3
index_search_location=/root/export

cd ${INFA_HOME}/isp/bin

echo Creating Search service

echo commabd is : ./infacmd.sh search createservice -dn Domain_INKR72DSG306 -nn node01_INKR72DSG306 -sn SS_SER -un Administrator -pd Administrator -rsn MRS -sp 8084 -il /home/ora12c/Informatica/PC10.2/export -sun Administrator -spd Administrator -ei 60

./infacmd.sh search createservice -dn Domain_${Machine} -nn node01_${Machine} -sn ${SEARCH_SERVICE} -un Administrator -pd Administrator -rsn ${MRS_SERVICE_NAME} -sp 8084 -il ${index_search_location} -sun Administrator -spd Administrator -ei 60

echo Assign License to Search service

echo command is :./infacmd.sh assignLicense -dn Domain_INKR72DSG306 -un Administrator -pd Administrator -ln 10.2.0_License_INKR72DSG306.informatica.com_294 -sn ${SEARCH_SERVICE}

./infacmd.sh assignLicense -dn Domain_${Machine} -un Administrator -pd Administrator -ln ${License_Name} -sn ${SEARCH_SERVICE}

echo Enable Search service

echo command is like : ./infacmd.sh EnableService -dn Domain_INKR72DSG306 -un Administrator -pd Administrator -sn SS_SER

./infacmd.sh EnableService -dn Domain_${Machine} -un Administrator -pd Administrator -sn ${SEARCH_SERVICE}

echo Ping Search Service

./infacmd.sh ping -dn Domain_${Machine} -sn ${SEARCH_SERVICE} -nn node01_${Machine} -re 150

export LD_LIBRARY_PATH=$INFA_HOME/server/bin:$LD_LIBRARY_PATH

