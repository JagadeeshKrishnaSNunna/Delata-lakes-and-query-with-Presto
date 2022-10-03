#!/bin/sh
$HADOOP_HOME/sbin/stop-all.sh
$HIVE_HOME/hcatalog/sbin/hcat_server.sh stop
/home/adminuser79/mystuff/tools/presto/bin/launcher stop