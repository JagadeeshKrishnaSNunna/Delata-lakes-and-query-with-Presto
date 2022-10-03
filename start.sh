#!/bin/sh
echo $HADOOP_HOME
$HADOOP_HOME/sbin/start-all.sh
$HIVE_HOME/hcatalog/sbin/hcat_server.sh start
/home/adminuser79/mystuff/tools/presto/bin/launcher start
/home/adminuser79/mystuff/tools/presto-cli --server localhost:8080 --catalog delta