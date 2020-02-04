DOMAIN_NAME=$1
INFA_HOME=$2
CHECKSTOP() {
	cd ${INFA_HOME}/isp/bin
    	var=`sh infacmd.sh ping -dn ${DOMAIN_NAME} -re 180`
	echo "$var" | grep ICMD_10033
	if [[ $? -ne 0 ]] ; then
   		CHECKSTOP
	fi
}

CHECKSTART() {
	cd ${INFA_HOME}/isp/bin
    	var=`sh infacmd.sh ping -dn ${DOMAIN_NAME} -re 180`
	echo "$var" | grep INFACMD_10052
	if [[ $? -ne 0 ]] ; then
   		CHECKSTART
	fi
}

cd ${INFA_HOME}/tomcat/bin

./infaservice.sh shutdown

CHECKSTOP

sleep 120

ps -ef | grep java | grep -v slave.jar | grep -v grep | awk '{ printf  "%s ", $2  }' | xargs kill -9
sleep 5

