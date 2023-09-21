# bigdata_project

"In this project, I am going to analyze crime data in India. Here, we used big data tools such as Hadoop, Hive, Spark, and Matplotlib. The data downloaded from Kaggle is loaded into Hadoop and then into a Hive table. Analysis is performed on this Hive table. In Hive, we used the SerDe method, as well as group by and order by functions for filtering the data. The output obtained is plotted in a bar graph using Matplotlib in pyspark."
![collage](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/a437104b-3989-4490-9df4-1926baf99a2c)

steps:

1. The dataset is downloaded from Kaggle and loaded into HDFS.

![1 first pic](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/ce826733-1bd6-415a-abcf-6c03b925e2f0)
![1](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/7ce85110-d339-4e4f-8a32-604e542145ce)

2. From HDFS, data is loaded into Hive.


    a) Using SerDe properties, data is loaded into a table by removing quotes. 
   
* 2016 cases against police personnels
   
![1 create normal table](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/0448646c-ca99-4af9-926c-7396ac76d625)
![1 loaddatahdfs2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/06ff6df3-7992-4719-b3e9-af6ef0a4ea8e)

   * 2017 cases against police personnels
       
![2 createnormal table 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/89ae3b96-ea49-4d40-a6cd-0c1425feb472)
![2 loaddatahdfs2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d5092086-a2d2-49f4-ae1b-1756a299baf2)

   * 2018 cases against police personnels

![3 create normal table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/2942fdf5-b44c-4ebe-9545-22875b16a47f)
![3 loaddatahdfs2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/6df09303-0687-4cd0-8941-feb3454ccbcb)

   b) From this table,data is loaded into another table
   
   * 2016 cases against police personnels
   
![1 newtable created 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/1660966a-1d72-46ba-80e4-c86a17120f8c)
![1 insert2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/1195ea50-f86d-4cc1-9f89-27f76e8f1fff)

   * 2017 cases against police personnels

![2 create newtable2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/7ec17680-1ddd-44dd-9cad-81ecee7c1457)
![2 insert2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/7c58c192-709e-418f-babd-fbb9c77f5d5c)

   * 2018 cases against police personnels     

![3 create new table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/648e59e3-f1dc-45b1-88f6-647428ce8d71)
![3 insert 2018 ](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4c12f1a0-ddc7-4da2-9a53-fde45dcd6fac)

   d)  Using the group by and order by functions in Hive, the top 10 states with the highest number of cases recorded are filtered, and this result is loaded into a table.
   
   * 2016 cases against police personnels

                    




   

