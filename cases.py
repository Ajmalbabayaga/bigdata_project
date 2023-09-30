from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()
import matplotlib.pyplot as plt

#cases
#2016 criminal cases
most_10_criminal_cases_in_2016=spark.read.csv('hdfs://localhost:9000/Project/CasesagainstPolicePersonnels/2016_most_10_criminal_cases',inferSchema=True)
most_10_criminal_cases_in_2016 = most_10_criminal_cases_in_2016.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS total_criminal_cases')
most_10_criminal_cases_in_2016.show()
most_10_criminal_cases_in_2016.toPandas().plot(kind='bar', x='state_ut', y='total_criminal_cases', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2016 Casesagainst Police Personnels")
plt.xticks(rotation=90)
plt.show()
#
# # 2017 criminal cases
most_10_criminal_cases_in_2017=spark.read.csv('hdfs://localhost:9000/Project/CasesagainstPolicePersonnels/2017_most_10_criminal_cases',inferSchema=True)
most_10_criminal_cases_in_2017 = most_10_criminal_cases_in_2017.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS no_total_criminal_cases')
most_10_criminal_cases_in_2017.show()

most_10_criminal_cases_in_2017.toPandas().plot(kind='bar', x='state_ut', y='no_total_criminal_cases', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2017 Casesagainst Police Personnels")
plt.xticks(rotation=90)
plt.legend()
plt.show()


# 2018 criminal cases
most_10_criminal_cases_in_2018=spark.read.csv('hdfs://localhost:9000/Project/CasesagainstPolicePersonnels/2018_most_10_criminal_cases',inferSchema=True)
most_10_criminal_cases_in_2018 = most_10_criminal_cases_in_2018.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS no_total_criminal_cases')
most_10_criminal_cases_in_2018.show()

most_10_criminal_cases_in_2018.toPandas().plot(kind='bar', x='state_ut', y='no_total_criminal_cases', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2018 Casesagainst Police Personnels")
plt.xticks(rotation=90)
plt.legend()
plt.show()

# total no of cases
total_no_cases=spark.read.csv('hdfs://localhost:9000/Project/CasesagainstPolicePersonnels/total_no_cases',inferSchema=True)
total_no_cases = total_no_cases.selectExpr('_c0 AS s_no','_c1 AS state_ut','_c2 AS total_no_cases')
total_no_cases.show()

total_no_cases.toPandas().plot(kind='bar', x='state_ut', y='total_no_cases', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("total_no_of_cases")
plt.xticks(rotation=90)
plt.legend()
plt.show()
