from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()
import matplotlib.pyplot as plt

# escape from police custody

#2016 escapes
escapes_from_police_custody_top_10_states_2016=spark.read.csv('hdfs://localhost:9000/Project/EscapesfromPoliceCustody/2016_escapes_from_police_custody_top_10_states',inferSchema=True)
escapes_from_police_custody_top_10_states_2016 = escapes_from_police_custody_top_10_states_2016.selectExpr('_c0 AS category','_c1 AS state_ut','_c2 AS total_number_of_persons_escaped_from_police_custody')
escapes_from_police_custody_top_10_states_2016.show()

escapes_from_police_custody_top_10_states_2016.toPandas().plot(kind='bar', x='state_ut', y='total_number_of_persons_escaped_from_police_custody', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2016_total_number_of_persons_escaped_from_police_custody")
plt.xticks(rotation=90)
plt.legend()
plt.show()
#
# # #2017 escapes
#
escapes_from_police_custody_top_10_states_2017=spark.read.csv('hdfs://localhost:9000/Project/EscapesfromPoliceCustody/2017_escapes_from_police_custody_top_10_states',inferSchema=True)
escapes_from_police_custody_top_10_states_2017 = escapes_from_police_custody_top_10_states_2017.selectExpr('_c0 AS category','_c1 AS state_ut','_c2 AS total_number_of_persons_escaped_from_police_custody')
escapes_from_police_custody_top_10_states_2017.show()

escapes_from_police_custody_top_10_states_2017.toPandas().plot(kind='bar', x='state_ut', y='total_number_of_persons_escaped_from_police_custody', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2017_total_number_of_persons_escaped_from_police_custody")
plt.xticks(rotation=90)
plt.legend()
plt.show()
#
# #2018 escapes
escapes_from_police_custody_top_10_states_2018=spark.read.csv('hdfs://localhost:9000/Project/EscapesfromPoliceCustody/2018_escapes_from_police_custody_top_10_states',inferSchema=True)
escapes_from_police_custody_top_10_states_2018 = escapes_from_police_custody_top_10_states_2018.selectExpr('_c0 AS category','_c1 AS state_ut','_c2 AS total_number_of_persons_escaped_from_police_custody')
escapes_from_police_custody_top_10_states_2018.show()

escapes_from_police_custody_top_10_states_2018.toPandas().plot(kind='bar', x='state_ut', y='total_number_of_persons_escaped_from_police_custody', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2018_total_number_of_persons_escaped_from_police_custody")
plt.xticks(rotation=90)
plt.legend()
plt.show()

# total no of escape

total_no_escape=spark.read.csv('hdfs://localhost:9000/Project/EscapesfromPoliceCustody/total_no_escapes',inferSchema=True)
total_no_escape = total_no_escape.selectExpr('_c0 AS s_no','_c1 AS state_ut','_c2 AS total_no_escape')
total_no_escape.show()

total_no_escape.toPandas().plot(kind='bar', x='state_ut', y='total_no_escape', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("total_no_of_escape")
plt.xticks(rotation=90)
plt.legend()
plt.show()