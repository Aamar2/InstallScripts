#!/bin/bash

###This script clean repo based on repositary type 
### set the below envirnoment variables 
#####DB_REPO_TYPE
#####DBADMINUSER
#####DBADMINPSWD
#####DBSID
#####PC_REPO
#####MRS_REPO
#####MRSMS_REPO
#####PWH_REPO
#####CMS_REPO
#####PDM_REPO
#####SATS_REPO

if [ "${DB_REPO_TYPE}" == "Oracle" ]; then
  
  if [ true == true ]; then
          echo ${PC_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${PC_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1
	  echo ${MRS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${MRS_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1
	  echo ${MRSMS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${MRSMS_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1	  
	  echo ${PWH_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${PWH_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1
	  echo ${CMS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${CMS_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1  
  fi
  
  if [ "${INSTALL_TDM}" == true ]; then	 
	  echo ${PDM_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${PDM_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1	  
  fi
  
  if [ "${SATS_lNSTALL_TYPE}" == "Fresh" ]; then	 
	  echo ${SATS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} USER_NAME=${SATS_REPO} FILE_LOC="${FILELOC}" ./DropCreateOracleUser.sh
	  sleep 1  
  fi  
 
 elif [ "${DB_REPO_TYPE}" == "DB2" ]; then
 
  if [ "${INSTALL_LDM}" == true ]; then
      echo ${PC_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$PC_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1
	  echo ${MRS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$MRS_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1
	  echo ${MRSMS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$MRSMS_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1	  
	  echo ${PWH_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$PWH_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1
	  echo ${CMS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$CMS_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1
  fi

  if [ "${INSTALL_TDM}" == true ]; then	
	  echo ${PDM_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$PDM_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1
  fi
  
  if [ "${SATS_lNSTALL_TYPE}" == "Fresh" ]; then	 
	  echo ${SATS_REPO}
	  DBADMINUSER=${DBADMINUSER} DBADMINPSWD=${DBADMINPSWD} DBSID=${DBSID} DBSCHEMA=$(echo "$SATS_REPO" | tr '[:lower:]' '[:upper:]') ./DropCreateDB2Schema.sh
	  sleep 1 
  fi   
 
 elif [ "${DB_REPO_TYPE}" == "SQLServer" ]; then
  
  javac CreateDBSQLServer.java
  if [ "${INSTALL_LDM}" == true ]; then
      echo ${PC_DBSERVICENAME}
 	  java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${PC_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT}
	  echo ${MRS_DBSERVICENAME}
	  java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${MRS_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT}
	  echo ${MRSMS_DBSERVICENAME}
	  java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${MRSMS_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT}	  
	  echo ${PWH_DBSERVICENAME}
	  java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${PWH_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT}
	  echo ${CMS_DBSERVICENAME}
	  java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${CMS_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT}
  fi
  
  if [ "${INSTALL_TDM}" == true ]; then	 
	  echo ${PDM_DBSERVICENAME}
      java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${PDM_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT}
  fi
  
  if [ "${SATS_lNSTALL_TYPE}" == "Fresh" ]; then	 
	  echo ${SATS_DBSERVICENAME}
	  java -classpath "${installer_files_loc}/Common/sqlserverjar/*:." CreateDBSQLServer ${SATS_DBSERVICENAME} ${DBADMINUSER} ${DBADMINPSWD} ${DBSERVERNAME} ${DBPORT} ${SATS_SQLSERVER_SCHEMA_NAME}
  fi     
 
 else
 
  echo "No Match for the $DB_REPO_TYPE, please specify valid one"
 
 fi
 
