from pyspark.sql import SparkSession

# Step 1: Create a SparkSession
spark = SparkSession.builder.appName("SimpleJob").getOrCreate()

# Step 2: Create a simple dataset with 2 lines of data
data = [("Alice", 25), ("Bob", 30)]
columns = ["Name", "Age"]

# Step 3: Create a DataFrame
df = spark.createDataFrame(data, schema=columns)

# Step 4: Show the DataFrame
df.show()

# Stop the SparkSession
spark.stop()