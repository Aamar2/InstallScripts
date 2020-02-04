FROM ubuntu:latest
RUN mkdir /home/temp && mkdir /home/installerFiles
COPY /SilentInstall/*.* /home/installerFiles/
ADD <Installer>.tar /home/temp/

# Install OpenJDK-8
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install -y ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

#Install Python
RUN apt-get update && \
    apt-get install -y python && \
	apt-get install -y iputils-ping && \
	apt-get install -y rpm

ENV LANG=en_IN.UTF-8

WORKDIR /home/installerFiles

CMD [ "python", "./105Install.py" ]

