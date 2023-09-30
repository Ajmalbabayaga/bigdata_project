from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()
import matplotlib.pyplot as plt


# victims of rape
# 2016 victmis
rape_victims_in_india_top_10_states_2016=spark.read.csv('hdfs://localhost:9000/Project/VictimsofRape/2016_Rape_victims_in_india_top_10_states',inferSchema=True)
rape_victims_in_india_top_10_states_2016 = rape_victims_in_india_top_10_states_2016.selectExpr('_c0 AS category','_c1 AS state_ut','_c2 AS total_victims')
rape_victims_in_india_top_10_states_2016.limit(10).show()

rape_victims_in_india_top_10_states_2016.limit(10).toPandas().plot(kind='bar', x='state_ut', y='total_victims', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2016_rape_victims_in_india_top_10_states")
plt.xticks(rotation=90)
plt.legend()

plt.show()

# 2017 victmis

rape_victims_in_india_top_10_states_2017=spark.read.csv('hdfs://localhost:9000/Project/VictimsofRape/2017_Rape_victims_in_india_top_10_states',inferSchema=True)
rape_victims_in_india_top_10_states_2017 = rape_victims_in_india_top_10_states_2017.selectExpr('_c0 AS category','_c1 AS state_ut','_c2 AS total_victims')
rape_victims_in_india_top_10_states_2017.show(10)

rape_victims_in_india_top_10_states_2017.limit(10).toPandas().plot(kind='bar', x='state_ut', y='total_victims', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2017_rape_victims_in_india_top_10_states")
plt.xticks(rotation=90)
plt.legend()
plt.show()

#2018 victmis
rape_victims_in_india_top_10_states_2018=spark.read.csv('hdfs://localhost:9000/Project/VictimsofRape/2018_Rape_victims_in_india_top_10_states',inferSchema=True)
rape_victims_in_india_top_10_states_2018 = rape_victims_in_india_top_10_states_2018.selectExpr('_c0 AS category','_c1 AS state_ut','_c2 AS total_victims')
rape_victims_in_india_top_10_states_2018.show(10)

rape_victims_in_india_top_10_states_2018.limit(10).toPandas().plot(kind='bar', x='state_ut', y='total_victims', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("2018_rape_victims_in_india_top_10_states")
plt.xticks(rotation=90)
plt.legend()
plt.show()


# #total no of victims
total_rape_victims=spark.read.csv('hdfs://localhost:9000/Project/VictimsofRape/total_rape_victims',inferSchema=True)
total_rape_victims = total_rape_victims.selectExpr('_c0 AS s_no','_c1 AS state_ut','_c2 AS total_rape_victims')
total_rape_victims.show()
total_rape_victims.toPandas().plot(kind='bar', x='state_ut', y='total_rape_victims', figsize=(20, 10),color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("total_rape_victims")
plt.xticks(rotation=90)
plt.legend()
plt.show()
