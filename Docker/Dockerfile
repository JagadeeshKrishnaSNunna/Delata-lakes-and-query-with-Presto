FROM ubuntu:20.04

# install requirements
RUN apt-get install -y wget openjdk-8-jdk
RUN rm -rf /var/lib/apt/lists/* 

ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

# work dir
RUN cd /home
RUN mkdir tools
WORKDIR /home/tools

RUN wget https://downloads.lightbend.com/scala/2.12.2/scala-2.12.2.deb
RUN dpkg -i scala-2.12.2.deb
RUN rm scala-2.12.2.deb

# SSH setup


RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-2.10.2/hadoop-2.10.2.tar.gz
RUN tar -xzf hadoop-2.10.2.tar.gz
RUN mv hadoop-2.10.2 hadoop
RUN rm hadoop-2.10.2.tar.gz
ENV HADOOP_HOME=/home/tools/hadoop
ENV PATH=${PATH}:${HADOOP_HOME}/sbin:${HADOOP_HOME}/bin


# HIVE setup 
RUN wget https://downloads.apache.org/hive/hive-2.3.9/apache-hive-2.3.9-bin.tar.gz
RUN tar -xzf apache-hive-2.3.9-bin.tar.gz
RUN mv apache-hive-2.3.9-bin hive
RUN rm apache-hive-2.3.9-bin.tar.gz
ENV HIVE_HOME=/home/tools/hive
ENV PATH=${HIVE_HOME}/bin:$PATH
COPY hive-env.sh ${HIVE_HOME}/conf/hive-env.sh
COPY hive-site.xml ${HIVE_HOME}/conf/hive-site.xml
RUN ${HIVE_HOME}/bin/schematool -dbType derby -initSchema
RUN mkdir -p ${HIVE_HOME}/hcatalog/var/log

COPY start.sh /home/tools/start.sh 
RUN chmod 777 /home/tools/start.sh

CMD ["sh","-c","/home/tools/start.sh"]
EXPOSE 9083
