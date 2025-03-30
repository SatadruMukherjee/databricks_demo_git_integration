from time import sleep
import sys
print(sys.argv)
print("Changes made")
print("Test Job Parameter")
table_name=sys.argv[1]
print("The input table name : ",table_name)
query = f"SELECT COUNT(1) as count FROM {table_name}"
df = spark.sql(query)
row_count = df.collect()[0]["count"]  # Store the count value in a variable
#print(f"Row count stored in variable: {row_count}")
dbutils.jobs.taskValues.set(key = "record_count", value = row_count)
