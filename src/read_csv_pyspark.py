from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Start Spark
spark = SparkSession.builder \
    .appName("Generate 100 Sample Rows") \
    .getOrCreate()

# Sample schema
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("score", IntegerType(), False)
])

# Generate 100 rows of data
data = [(i, f"name_{i}", i * 10 % 95 + 5) for i in range(1, 101)]

# Create DataFrame
df = spark.createDataFrame(data, schema=schema)

# Show few rows
df.show(10, truncate=False)

# LEFT SEMI join to extract data from left table data only which are matching from second table
# Left anti join to extract data from left table data which do not have matching from second table
