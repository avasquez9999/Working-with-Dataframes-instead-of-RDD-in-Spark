from pyspark.sql import SparkSession
from pyspark.sql.functions import avg 

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("file:///SparkCourse/fakefriends-header.csv")
    
print("Here is our inferred schema:")
people.printSchema()

print("Let's display the name column:")
people.select("name").show()

print("Filter out anyone over 21:")
people.filter(people.age < 21).show()

print("Group by age")
people.groupBy("age").count().show()


print("Make everyone 10 years older:")
people.select(people.name, people.age + 10).show()

print("Group by 'age' and calculate the average 'age'")
grouped_data = people.groupBy("age").agg(avg("age").alias("average_age")).show()

spark.stop()

