stopDomain=$1
DOMAIN_NAME=$2
INFA_HOME=$3

if [ -d ${INFA_HOME} ]; then
      echo Shutting down Informatica Domain
      echo sh ${stopDomain} ${DOMAIN_NAME} ${INFA_HOME}
      sleep 100	
      
      sh ${stopDomain} ${DOMAIN_NAME} ${INFA_HOME}

      #echo Running Uninstaller 
      #$INFA_HOME/Uninstaller_Server/uninstaller
fi

  
if [ -d ${INFA_HOME} ]; then
      echo Removing ${INFA_HOME}
      chmod -R 777 ${INFA_HOME}
      rm -rf ${INFA_HOME}
      #rm -rf $HOME/Informatica
fi  
