# Simple-Delta-lake-setup

## Prerequisite

    java 1.8 (prefered)
    Delta Lake  - 2.0.0
    Scala  -  2.12.8
    pyspark  - 3.2.2
    delta-spark  -  2.0.0

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
        
        $ $HADOOP_HOME/bin/hadoop fs -mkdir -p /tmp
        $ $HADOOP_HOME/bin/hadoop fs -mkdir -p /user/hive/warehouse
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

## Setup spark

    Download spark-3.2.2-bin-hadoop3.2.tgz

    Set up env variable
        export SPARK_HOME=/home/adminuser79/mystuff/tools/spark
        export PATH=$PATH:$SPARK_HOME

## Setup Presto

    Download presto-server-0.276.tar.gz
    Download presto-jdbc-0.276.jar    
    Download presto-CLI-0.276.jar    

### Presto configuration files from Prsto-config folder
      
        create etc folder
            $ mkdir etc
            $ cd etc
        Add files in etc folder
         1. config.properties  
         2. jvm.config  
         3. log.properties  
         4. node.properties
        create etc/catalog folder
            $ mkdir catalog
            $ cd catalog
        Add files in catalog
         1. delta.properties
         2. hive.properties
         3. jmx.properties

### Start Presto server
        
        Start hive hcatalog server first
        $ bin/launcher start

### Start Presto-CLI

    rename presto-CLI-0.276.jar

        $ mv presto-CLI-0.276.jar presto-CLI
        $ chmod 777 presto-CLI
        $ ./presto-CLI --server localhost:8080 --catalog delta

### Access the delta table in hive/Presto

        add delta-hive-assembly_<scala_version>-<delta_connectors_version>.jar in hive lib

        create the table in hive and query it with presto delta catalog
                create table table-name(col1 type,....)
                STORED BY 'io.delta.hive.DeltaStorageHandler'
                LOCATION '/delta/table/path'

## use Script
        
        To start hadoop,hcatalog,presto and presto-cli
                $ ./start.sh
        To stop all services
                $ ./stop.sh

