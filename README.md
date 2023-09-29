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
![3 victims_of_rape database](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c8a10796-c6f8-4bf7-9d51-ca2137cbb922)


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

    * 2016 Victims of Rape        

![1 create table vit2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/94f58ae8-eaa2-4465-bdb4-b0740b33a9db)
![1 loaddatahsdfs2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/3ab88693-9794-43ed-9107-9a28ce2b015a)
      
    * 2017 Victims of Rape

![2 create table vit 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/0f9dc365-eebe-4191-85ae-ed2d5ca926ad)
![2 loaddatahdfs2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/63b800b3-c4d8-49eb-8d5e-9326e9cdc3ac)

    * 2018 Victims of Rape

![3 create normal table2018 ](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/31a2db40-18f5-489a-b706-96f43dfc3398)
![3 loaddatafromhdfs2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/fc4e02b7-169d-4433-a81a-3a889d2e3e06)


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
            
   * 2016 Escape from Police Custody

![1 newtable2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4b044bd1-14f2-4562-bd04-b6450f1fa254)
![1 insert 2016 ](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/3c4def7b-b79b-433f-be66-79c4f2bcbc9d)
                 
   * 2017 Escape from Police Custody
              
![2 2017 new table create](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/da14689f-da1f-4fa2-a94a-d585b2f126a2)
![2 insert 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/6aef7155-df86-4dba-a3bb-7b2cddd89bcb)
         
   * 2018 Escape from Police Custody    

![3 create newtable 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8796582c-4406-499b-89e9-4db652f43bf7)
![3 insert 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/77427cb8-317d-43dd-afd7-b31fb970d7a8)

   * 2018 Victims of Rape                      

![3 create newtable2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8ce2ea24-c1f9-4812-8e2e-643bcd629a07)
![3 insert tble2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/5d16b588-5573-4d91-a959-db6b62459217)


   c)  Using the 'group by' and 'order by' functions in Hive, the top 10 states with the highest number of recorded cases, the most persons escaped, and the highest number of rape victims for the three years (2016, 2017, 2018) are filtered, and the results are loaded into a table.


   * Total number of cases in three years(2016,2017,2018)
       
![1 create 3 table 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/1d812e58-673d-4acb-8c13-a69f8b004c1a)
![1 3 table insert](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/78a093f3-8198-4577-ab2a-48f361f58241)
![2  3 table insert](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/08efe709-6e23-40e5-a205-e53d979f783d)
![3 3 insert table](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c48fff8f-1ea2-49c1-86be-f4c64b8873b0)

![1 total_cases  police](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/0e96d4c1-0abc-4b80-9998-c652cf976135)
![1 total_no_cases desc](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8f32c453-e436-4eec-8012-292f06010af0)
![1 total no cases insert hdfs](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/97331e9b-d1a4-436b-983b-2120780c376c)
         
   * Total number of Escape in three years(2016,2017,2018)

![1 create 3 table 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/bbd8389e-77a2-4145-b866-c9776e3481b0)
![1 insert 3 tables2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4789d4c5-df54-4d8a-8eff-578ee1e913b1)
![2 insert 3 tables2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/453a1a3c-6d6a-4d49-8bdf-ea5ffcfa80e1)
![3 insert 3 table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/b72e2918-0f0d-4d9b-a983-21f50d0fcf78)

![1 escape_cases create](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/96a4a139-7a60-4e80-8bc5-9c47e990eee7)
![1 total no escapes ](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/b2c3cbb0-f2a4-45ee-b8c0-9160b5917330)
![1 insert escapes hdfs](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4096b83f-1646-496a-b448-b160c923fa37)

   * Total number of Victims in three years (2016,2017,2018)

![1 create 3 table 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/ee705a73-6ab7-44dd-beb9-f4070744cb57)
![1 insert 3 table 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/61020473-f2fa-4626-9bad-b9d4899a37ca)
![2 insert 3 table 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/3963b36e-facf-4fc5-b788-4c29ef0eef26)
![3 insert 3 table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/e2af536a-ed00-47e7-a328-a1fda1d306f8)

![1 victims_cases create table](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/9ca33eb4-4c4b-4213-8499-43adcc91acdc)
![1 victims total rape victims](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/07a2fe18-8b07-40b5-af19-7938d762e29c)
![1  total_rape _ victims insert hdfs](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/3505215d-87ab-4ebe-b414-4c02082d13e3)


   d) From each table containing cases, escapes, and victims for the years 2016, 2017, and 2018, the top 10 states with the highest number of reported cases, the most persons escaped, and the highest number of rape victims in each year are filtered.

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
                  
   * 2016 Escape from Police Custody                  

![1 add table 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/7e2b5ca2-bb50-4f22-8f02-57b88d527651)
![20](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/1f66266a-e29e-43d9-9af8-25a31dcfc1b4)
![1 insert new hdfs 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/788ba444-952a-4b24-8267-3dc72ce397ee)

   * 2017 Escape from Police Custody

![2017 most](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/b12eddde-5c57-4f6f-bbef-a26c72cfa39d)
![21](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/dbd75549-2dbf-45ee-9a66-6baf47376ee0)
![2 new insert  hdfs2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/f33707c2-0de4-49d2-aadd-0f772a96306f)

   * 2018 Escape from Police Custody                   

![3 add table 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/6651447a-3776-40fc-b3fb-6e7c026b97bc)
![23](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/677e0332-03ed-4cd7-a591-ed9ff7af278a)
![3 new inserthdfs 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/309c74ec-09e8-442c-84c5-c6381e8c3922)


e)







                    




   

