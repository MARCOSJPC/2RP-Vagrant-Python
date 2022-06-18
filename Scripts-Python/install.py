#!/usr/bin/python

import os

# instalacao do java

os.system('sudo su')
os.system('yum install java-11-openjdk-devel')
os.system('yum install java-11-openjdk')
os.system('wget https://download.oracle.com/java/18/latest/jdk-18_linux-aarch64_bin.rpm')
os.system('localinstall jre-18-linux-x64.rpm')
os.system('java -version')


# instalacao do Zeppelin com docker
os.system('docker run -p 8888:8080 --rm --name zeppelin apache/zeppelin:0.10.1')
