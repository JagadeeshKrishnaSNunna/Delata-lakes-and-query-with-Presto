from audioop import mul
from pickle import TRUE
from delta import *
from delta.tables import *
from pyspark.sql.functions import *
import time as t

pkg_list = []
pkg_list.append("io.delta:delta-core_2.12:2.0.0")
pkg_list.append("org.apache.hadoop:hadoop-aws:3.2.2")
packages=(",".join(pkg_list))


spark = (SparkSession
    .builder
    .appName("PySparkApp") 
    .config("spark.jars.packages", packages) 
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") 
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") 
    .config("fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") 
    .getOrCreate()) 

# choose the location to create the Schema[similar to database]

spark.sql("create schema IF NOT EXISTS delta LOCATION '/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/'")


def createTable():
    st=t.time()
    DeltaTable.createIfNotExists(spark) \
        .tableName("delta.testing") \
        .addColumn("Name", "STRING") \
        .addColumn("USN", "STRING") \
        .addColumn("SEM", "INT") \
        .location("/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing/") \
        .execute()
    ed=t.time()
    print("Table creation time is: "+str(ed-st),end='\n')

def createTableWithPartition():
    spark.sql("CREATE TABLE delta.testing(Name String,USN STRING,SEM BIGINT,Tenant STRING)USING delta PARTITIONED BY (Tenant) Location '/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing/'")


def insert(name,usn,sem):
    st=t.time()
    spark.sql("INSERT INTO delta.`/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing/` values(\""+name+"\",\""+usn+"\","+str(sem)+")")
    ed=t.time()
    print("Record insertion time is: "+str(ed-st),end='\n')

def update(data):
    st=t.time()
    table=DeltaTable.forPath(spark,"/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing")
    table.update(col("usn")==data["usn"],data)
    ed=t.time()
    print("Record update time is: "+str(ed-st),end='\n')

def parseData(jsonData):
    newData={}
    for key in jsonData.keys():
        newData[key]=lit(jsonData[key])
    return newData

def delete(usn):
    st=t.time()
    table=DeltaTable.forPath(spark,"/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing")
    table.delete(col("usn")==usn)
    ed=t.time()
    print("Record delete time is: "+str(ed-st),end='\n')

def compaction():
    st=t.time()
    table=DeltaTable.forPath(spark,"/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing")
    table.optimize().executeCompaction()
    ed=t.time()
    print("Record compation time is: "+str(ed-st),end='\n')

def getData():
    st=t.time()
    table=DeltaTable.forPath(spark,"/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing")
    data=table.toDF()
    print(data.head(10))
    ed=t.time()
    print("Record print time is: "+str(ed-st),end='\n')

def multi_thread(i):
    insert("A"+str(i),"1DS17CS00"+str(i),6 if (i%2==0) else 5)




def start():

#   create table without partition
    createTable()
    
#   create table with partition
    createTableWithPartition()

#  insert some sample records
    for i in range(1,10):
        insert("A"+str(i),"1DS17CS00"+str(i),6 if (i%2==0) else 5)

# bulk insertion of json records in file sample.json
    df=spark.read.option("multiLine", True).format('json').load("sample2.json")
    df.write.format('delta').mode('append').save('/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing')


#   Sample data to update
    data={
        "name":"A5",
        "usn":"1DS17CS005",
        "sem":5
    }
#   Update data
    update(parseData(data))
#   Delete record
    delete('1DS17CS005')

#   Bin-packing to create one large file from several small files
    compaction()
    getData()
    
#   Time Travell with time-stamp   
    print("\n"+"26-09-2022")
    df=spark.read.format("delta").option("timestampAsOf", "2022-09-26").load('/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing')
    df.head(100)

#   Time Travell with version number   
    df=spark.read.format("delta").option("versionAsOf", "59").load('/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing')
    df.show(100)

#   Check history
    table=DeltaTable.forPath(spark,"/home/adminuser79/Desktop/workspace/deltaLake/Data/DeltaSchema/testing")
    print(table.history().show(100))

    
    

start()
