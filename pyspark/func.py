from pyspark.sql.functions import when
import pandas as pd
def add(c1, c2):
    return int(c1) + int(c2)

def dealingDF(dataDF, fileinfo):
    threshold = fileinfo['threshold']
    # return dataDF
    # return dataDF.filter(dataDF.money.cast('int') > threshold)
    # df.select(when(df['age'] == 2, 3).otherwise(4).alias("age")).show()
    return dataDF.select("*", when(dataDF.money.cast('int') > 1000, '1').otherwise('0').alias("label"))
    # return dataDF.toPandas()
    # return 1 #报错

def dealingSQL(fileinfo):
    tableName = fileinfo['tableName']
    # SQL = "select * from temp"
    SQL = f"select *, if(int(money) > 1000, 1, 0) as Label from {tableName}"
    # SQL = "update temp set money = 1000"
    # SQL = "update temp set label = 1 if money > 1000 else 0, labelDetail = 1500 if money > 1000 else 0"
    return SQL