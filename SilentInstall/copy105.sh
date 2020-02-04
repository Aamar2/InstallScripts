BuildLocation=$1
BUILD_LOCATION=$2
Export_Location=/root/export
if [ -d ${BUILD_LOCATION} ]; then
      echo Removing ${BUILD_LOCATION}
      chmod -R 777 ${BUILD_LOCATION}
      rm -rf ${BUILD_LOCATION}
fi
mkdir ${BUILD_LOCATION}
if [ -d ${Export_Location} ]; then
      echo Removing ${Export_Location}
      chmod -R 777 ${Export_Location}
      rm -rf ${Export_Location}
fi
mkdir ${Export_Location}
#cp /data1/ora12c/Builds/build.${BUILD_NO}/lin-x64/informatica_10202_server_linux-x64.tar ${BUILD_LOCATION}
cp ${BuildLocation}/informatica_1050_server_linux-x64.tar ${BUILD_LOCATION}

cd ${BUILD_LOCATION}
sleep 100  
tar -xvf informatica_1050_server_linux-x64.tar
rm -r ${BUILD_LOCATION}/informatica_1050_server_linux-x64.tar