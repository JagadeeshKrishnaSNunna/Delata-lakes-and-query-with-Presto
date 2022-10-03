# Simple-Delta-lake-setup

## Prerequisite
    java 1.8 (prefered)

## Hadoop Setup
    Download version : hadoop-2.10.2.tar.gz

### setup environment variables
        export HADOOP_HOME=/home/adminuser79/mystuff/tools/hadoop
        export HADOOP_MAPRED_HOME=$HADOOP_HOME
        export HADOOP_COMMON_HOME=$HADOOP_HOME
        export HADOOP_HDFS_HOME=$HADOOP_HOME
        export YARN_HOME=$HADOOP_HOME
        export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
        export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
        export HADOOP_INSTALL=$HADOOP_HOME

### install
        $ sudo apt-get install ssh
        $ sudo apt-get install pdsh

    Now check that you can ssh to the localhost without a passphrase:
        $ ssh localhost
    If you cannot ssh to localhost without a passphrase, execute the following commands:
        $ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
        $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
        $ chmod 0600 ~/.ssh/authorized_keys


### JAVA_HOME
    in etc/hadoop/hadoop-env.sh set JAVA_HOME
        export JAVA_HOME=<path to java home>

### Hadoop Config
    replace files in Hadoop-conf folder at etc/hadoop/*
        1.core-site.xml
        2.hdfs-site.xml
        3.mapred-site.xml
        4.yarn-site.xml

### HDFS setup
     Format the filesystem:
        $ bin/hdfs namenode -format

### Run Hadoop cluster
        $ sbin/start-all.sh

## Hive Setup
    Downoload apache-hive-2.3.9-bin.tar.gz

### setup environmental variables
        export HIVE_HOME=/home/adminuser79/mystuff/tools/hive
        export PATH=$HIVE_HOME/bin:$PATH
        export HIVE_CONF_DIR=$HIVE_HOME/conf

### setup HDFS for Hive
        $ $HADOOP_HOME/bin/hadoop fs -mkdir       /tmp
        $ $HADOOP_HOME/bin/hadoop fs -mkdir       /user/hive/warehouse
        $ $HADOOP_HOME/bin/hadoop fs -chmod 777   /tmp
        $ $HADOOP_HOME/bin/hadoop fs -chmod 777   /user/hive/warehouse
### set HADOOP_HOME in /conf/hive-env.sh
        HADOOP_HOME=/home/adminuser79/mystuff/tools/hadoop

### Replace files in Hive-conf
    1. hive-site.xml

### Initialize SchemaTool
        $HIVE_HOME/bin/schematool -dbType <db type> -initSchema

### run hive CLI
        $HIVE_HOME/bin/hive

### run hiveserver2
        $HIVE_HOME/bin/hiveserver2

### Running HCatalog
        $HIVE_HOME/hcatalog/sbin/hcat_server.sh







