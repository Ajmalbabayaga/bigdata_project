# bigdata_project

"In this project, I am going to analyze crime data in India. Here, we used big data tools such as Hadoop, Hive, Spark, and Matplotlib. The data downloaded from Kaggle is loaded into Hadoop and then into a Hive table. Analysis is performed on this Hive table. In Hive, we used the SerDe method, as well as group by and order by functions for filtering the data. The output obtained is plotted in a bar graph using Matplotlib in pyspark."
![collage](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/a437104b-3989-4490-9df4-1926baf99a2c)

steps:

1. The dataset is downloaded from Kaggle and loaded into HDFS.

![1 first pic](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/ce826733-1bd6-415a-abcf-6c03b925e2f0)
![1](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/7ce85110-d339-4e4f-8a32-604e542145ce)

2. From HDFS, data is loaded into Hive by creating databases.

![1 cases_against_police_personnels database](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/78f1ab7a-5bab-4f7f-a59d-f862d8256e24)
![2 data baseescapes_from_police_custody ](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/865e0fae-e182-48c4-96f7-94d051dce012)


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

    * 2016 Escape from Police Custody

![1 create normal table2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/18f4414f-0526-4ef1-85be-9b3f2a465a14)
![1 loaddatahdfs2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/367fb431-9f8d-40ec-9c14-a1e454071f5b)

    * 2017 Escape from Police Custody

![2 create normal table 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/5bfcb7f9-1879-4c76-b622-4cd098e9e068)
![2 loaddatahdfs2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8f9805eb-ec9c-443a-8208-5161160bd023)

    * 2018 Escape from Police Custody    

![3 create noraml table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/1ab46177-e49e-4206-b1f7-70a9d17078ba)
![3 loaddata hdfs 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/98a77676-61bb-4760-aba8-b51a40007558)


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

   c)  Using the group by and order by functions in Hive, the top 10 states with the highest number of cases recorded for three years[2016,2017,2018] are filtered, and this result is loaded into a table.

![1 create 3 table 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/1d812e58-673d-4acb-8c13-a69f8b004c1a)
![1 3 table insert](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/78a093f3-8198-4577-ab2a-48f361f58241)
![2  3 table insert](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/08efe709-6e23-40e5-a205-e53d979f783d)
![3 3 insert table](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c48fff8f-1ea2-49c1-86be-f4c64b8873b0)

![1 total_cases  police](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/0e96d4c1-0abc-4b80-9998-c652cf976135)
![1 total_no_cases desc](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8f32c453-e436-4eec-8012-292f06010af0)
![1 total no cases insert hdfs](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/97331e9b-d1a4-436b-983b-2120780c376c)

   d) From each table with cases in the years 2016, 2017, and 2018, the top 10 states with the highest number of cases reported in each year are filtered.

   * 2016 cases against police personnels

![1 add table to new table2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/b47d921b-b432-465c-ad3f-a52b96d61f67)
![8](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d6c7823f-3e3a-4d18-83a9-304b90020b38)
![1 new insert table 2016 to hdfs](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/68c9630b-2eac-4c9b-8064-48a3c0b4af0f)

   * 2017 cases against police personnels

![2 add table newtable 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/0ad68906-3e01-4b48-b9d7-e67c2bb8d120)
![9](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8258ce33-7383-4457-a251-54ab43b00b17)
![2 new insert  hdfs2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/6e321fcb-fb26-428e-bee0-3e6bfc724921)

   * 2018 cases against police personnels
     
![3 add table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/df8905b8-923c-44e6-a1c4-6f01e26f3f32)
![10](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/7f4fc928-b50f-4a48-af0e-7f263e634817)
![3 new inserthdfs 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4c36562b-0bc6-43dd-9b91-b716f17bc49d)

e)







                    




   

