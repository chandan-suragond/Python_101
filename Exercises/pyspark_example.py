from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, sum as _sum, row_number
from pyspark.sql.window import Window

# Step 1: Create SparkSession
spark = SparkSession.builder \
    .appName("PySpark Basic Operations Example") \
    .getOrCreate()

# Step 2: Read CSV
df = spark.read.option("header", True).option("inferSchema", True).csv("people.csv")

# Step 3: Select specific columns
df_select = df.select("name", "age", "city")
df_select.show()

# Step 4: Rename a column
df_renamed = df.withColumnRenamed("salary", "annual_salary")
df_renamed.show()

# Step 5: Duplicate a column
df_dup = df.withColumn("salary_copy", col("salary"))
df_dup.show()

# Step 6: Create a new column with arithmetic
df_new_col = df.withColumn("monthly_salary", col("salary") / 12)
df_new_col.show()

# Step 7: Create a column using CASE statement
df_case = df.withColumn(
    "income_level",
    when(col("salary") >= 85000, "High")
    .when((col("salary") >= 70000) & (col("salary") < 85000), "Medium")
    .otherwise("Low")
)
df_case.select("name", "salary", "income_level").show()

# Step 8: Aggregate functions - average salary by city
df_agg = df.groupBy("city").agg(
    avg("salary").alias("avg_salary"),
    _sum("salary").alias("total_salary")
)
df_agg.show()

# Step 9: Window functions - rank people by salary within each city
windowSpec = Window.partitionBy("city").orderBy(col("salary").desc())

df_window = df.withColumn("rank", row_number().over(windowSpec))
df_window.select("name", "city", "salary", "rank").show()

# Stop Spark session
spark.stop()
