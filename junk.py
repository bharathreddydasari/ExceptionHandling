# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql import Row
from pyspark.sql.functions import split
import sys
import os
import re 
import logging
from datetime import datetime
import collections
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.sql.types import *
from py4j.protocol import Py4JJavaError
from pyspark.sql.functions import lit
from pyspark.sql.functions import col

LocationMasterList = sys.argv[1]


spark = SparkSession.builder.\
    appName("LocationMasterRQ4Parquet").getOrCreate()


dfLocationMaster = spark.read.format("com.databricks.spark.csv").\
        option("header", "true").\
        option("treatEmptyValuesAsNulls", "true").\
        option("inferSchema", "true").\
        load(LocationMasterList)



for i in list(dfLocationMaster['City']):
    match = re.search(i,"/^[A-Za-z]/")
    if not match:
     print("i is a number")
    else:
     print("encountered a problem like numeric value in place of string")






spark.stop()
