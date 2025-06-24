# Working-with-Dataframes-instead-of-RDD-in-Spark
SparkFriends: A PySpark Example for Data Manipulation
This repository contains a PySpark script (SparkFriends.py) demonstrating fundamental data manipulation techniques using Spark SQL with a CSV dataset. The script reads a dataset of "fake friends" (similar to a social network) and performs various operations to illustrate Spark's capabilities for data filtering, aggregation, and transformation.

Key Operations Demonstrated:
Schema Inference: Automatically infers the schema of the input CSV file.
Column Selection: Selects and displays specific columns (e.g., "name").
Data Filtering: Filters records based on conditions (e.g., friends under 21).
Grouping and Counting: Groups data by a column and counts occurrences (e.g., count of friends per age).
Data Transformation: Applies transformations to existing columns (e.g., increasing everyone's age by 10).
Aggregation: Calculates aggregate functions on grouped data (e.g., average age per age group).
Dataset:
The script uses a CSV file named fakefriends-header.csv. This file is expected to have a header and columns such as "name" and "age".
