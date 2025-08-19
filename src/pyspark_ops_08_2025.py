# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('practice').getOrCreate()


# COMMAND ----------

data = [
    (1, "Alice", 25, "NY", 5000),
    (2, "Bob", None, "CA", 6000),
    (3, "Charlie", 30, "NY", None),
    (4, "David", 45, "TX", 8000),
    (5, "Eve", 35, "CA", 6000),
    (6, "Frank", None, "TX", 7000),
    (7, "Grace", 30, "NY", 5000),
    (8, "Heidi", 28, "CA", None),
    (9, "Ivan", 35, "TX", 8000),
    (10, "Judy", 25, "NY", 5000),
    (11, "Kyle", 40, "TX", 9000),
    (12, "Laura", 32, "CA", 6500),
    (13, "Mallory", 29, "NY", 5200),
    (14, "Niaj", None, "TX", None),
    (15, "Olivia", 38, "CA", 7000),
    (16, "Peggy", 30, "NY", 5000),
    (17, "Quentin", 45, "TX", 8000),
    (18, "Rupert", 35, "CA", 6000),
    (19, "Sybil", 28, "NY", 5200),
    (20, "Trent", 25, "TX", 7500)
]

columns = ["id", "name", "age", "state", "salary"]
df = spark.createDataFrame(data, columns)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## DROP DUPLICATES

# COMMAND ----------

from pyspark.sql.functions import col
df=df.dropDuplicates()
df.orderBy(col('id').desc()).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **Filter**

# COMMAND ----------

df_filter_or = df.select('*').filter((col('salary')>=6000) | (col('state')=='CA'))
df_filter_and= df.select('*').filter((col('salary')>=6000) & (col('state')=='CA'))
df_filter_and.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **GROUP BY**

# COMMAND ----------

from pyspark.sql.functions import avg,round
from pyspark.sql.types import IntegerType
df_grpby=df.groupBy('state').agg(avg(col('salary')).alias('avg_salary'))
df_grpby.select('state', 'avg_salary')
df_grpby.show()

# COMMAND ----------

df_replace_avg = df.alias('a').join(
    df_grpby.alias('b'),
    col('a.state') == col('b.state'),
    'inner'
).select(
    col('a.id'),
    col('a.salary'),
    col('b.avg_salary').cast('Int')
)

df_replace_avg.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ## **ORDERBY**

# COMMAND ----------

df_replace_avg.orderBy(col('avg_salary').desc() , col('id').asc()).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **getNumPartitions**

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

df=df.repartition(14)

# COMMAND ----------

df= df.coalesce(5)

# COMMAND ----------

# MAGIC %md
# MAGIC # **ColumnRename**

# COMMAND ----------

df_col = df.withColumnRenamed('id','emp_id')
df_col.show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **WITHCOLUMN**

# COMMAND ----------

df_withcolumn=df.withColumn('sal',col('salary')*2).withColumn('age_1',col('age')+4).drop('age')
df_withcolumn.show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **Window**

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

w = Window.partitionBy('state').orderBy('id')

df_win= df.select('id','name','state','salary', row_number().over(w).alias('rank'))

df_win.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ## **UDF**

# COMMAND ----------

from pyspark.sql.functions import udf, DataFrame,avg, round

def age_change (a):
    return a* 2

u = udf(age_change, IntegerType())

df_age = df.fillna({'age': 25}).select('id','name',u('age').alias('age'))
df_age.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **WHEN**

# COMMAND ----------

from pyspark.sql.functions import when
df_when = df.select('id','name','age', when(col('salary').isNull(),5000).otherwise(col('salary')).alias('salary'))
df_when.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **where**

# COMMAND ----------

df_where = df.where((col('salary')>5000) & (col('state')=='CA'))
df_where.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **UNION**

# COMMAND ----------

df_union = df.union(df_where).select('id','name','age','salary')
df_union.orderBy('id').show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **UNION BY NAME**

# COMMAND ----------

df_ubn = df.unionByName(df_union, allowMissingColumns=True)
df_ubn.dropDuplicates().orderBy('id').show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **joins**

# COMMAND ----------


df.show()


# COMMAND ----------

df_join = df_ubn.join(df, df_ubn['id']==df['id'] , 'outer')
df_join.select(df_ubn['id'],df_ubn['name'],df_ubn['state'],df_ubn['age'],df_ubn['salary']).show()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

df1 = spark.createDataFrame([
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie")
], ["id", "name"])

df2 = spark.createDataFrame([
    (2, "HR"),
    (3, "Engineering"),
    (4, "Finance")
], ["id", "dept"])

df_outer = df1.join(df2, "id", "outer")
df_outer.show()


# COMMAND ----------

df_outer = df1.join(df2, "id", "leftouter")
df_outer.show()

# COMMAND ----------

df_outer = df1.join(df2, "id", "leftsemi")
df_outer.show()

# COMMAND ----------

df_outer = df1.join(df2, "id", "leftanti")
df_outer.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Fillna**

# COMMAND ----------

df_fill= df.fillna({'salary':5000, 'age': 25})
df_fill.show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **DROPNA**
# MAGIC

# COMMAND ----------

df_drp = df.dropna(subset=('salary'))
df_drp.orderBy('id').show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **Broadcast joins**

# COMMAND ----------

from pyspark.sql.functions import broadcast
df_brd = df.filter(col('salary')>6000)
df_join=df.alias('a').join(broadcast(df_brd).alias('b') , df_brd['id']==df['id'], 'inner' )
df_join.select('a.id','a.name','a.salary','a.age').show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **EXPLAIN**

# COMMAND ----------

df_join.explain(True)  # Shows both logical and physical plans