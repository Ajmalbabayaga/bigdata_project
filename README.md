# Crime Analysis

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

The data is already in integer datatype, so the serde property is not used. Instead, a table is created and loaded directly into HDFS. (2016 victims of rape)

    * 2016 Victims of Rape        

![1 create table vit2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/94f58ae8-eaa2-4465-bdb4-b0740b33a9db)
![1 loaddatahsdfs2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/3ab88693-9794-43ed-9107-9a28ce2b015a)

The data is already in integer datatype, so the serde property is not used. Instead, a table is created and loaded directly into HDFS. (2017 victims of rape)

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
           
   * 2016 Victims of Rape

![30](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/5d66211d-cc3f-4901-aa05-95d642bf4cfc)
![30](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/93edac3f-cc1e-47d9-a985-02f724b7bbba)
![31](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/320d6002-873c-41ba-bd29-1d38fc514df9)

   * 2017 Victims of Rape

![33](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/049ea480-0248-42c0-a723-c04b9fb8e67d)
![31](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/b281562f-3566-4b40-9b17-068ea1518ab4)
![34](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/cbd830e2-e534-4d49-9524-c7e2c69149dc)

   * 2018 Victims of Rape                     

![36](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c155bff3-1bbc-44a9-8e42-ed17a4480138)
![33](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4acbac73-0043-429d-92f9-93941a44aea4)
![37](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/4822a82b-e01b-4543-a698-43e529288d35)

e)The result are plotted using matplotlip in pyspark.

* The files regarding the cases against police personnel escapes from police custody,and victims of rape are mentioned above as cases.py,escapes.py and victims.py respectively.

* The report are given below

I) To find the top 10 states/UT with the highest number of cases reported in the year 2016.

   ![1 2016 casestable ss](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c2b1c39d-c111-41d6-877f-f917d1f91677)
![1 cases2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/3cf4a1f0-bbb1-4191-8a7b-16a2b132f77c)

II) To find the top 10 states/UT with the highest number of cases reported in the year 2017.

![2 cases2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d910ca6c-d91c-4f7a-885f-64d8f7bdcfb9)
![2 cases2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d3af2ea6-833a-4246-97b9-dd4fec328ac2)

III) To find the top 10 states/UT with the highest number of cases reported in the year 2018.

![3 cases 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/8a19bdaa-cc23-4e77-862e-1c5ba5c703d3)
![2 cases2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c0f60218-ffe8-4c71-990b-9eb963fd07e6)

IV) To find the top 10 states/UT with the highest number of cases reported in the three years (2016,2017,2018).             

![4 cases all](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/63be52c4-1962-46c7-815a-f66b5dfce639)
![4 cases all](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/e58d3a73-8ed7-4eb6-88c8-f786cbff343e)

V) To find the top 10 states/UT with total number of persons escaped from police custody in the year 2016.

![5 escape 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d8328966-9025-4ba1-9824-80d1f8c71f03)
![5 escape2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/a91bc722-0f75-4bd0-a114-967cde65e4d6)

VI) To find the top 10 states/UT with total number of persons escaped from police custody in the year 2017.

![6 escape 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/17487396-3766-43c8-918c-b66e5c4005cd)
![6 escape2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/6f4fb151-a92e-4e55-9e83-5970fa5cb807)

VII) To find the top 10 states/UT with total number of persons escaped from police custody in the year 2018.

![7 escape 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/26aedd0f-0eee-43cf-b538-d0ed615f6b5a)
![7 escape2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/443cfe9a-cc2f-46d8-8954-22dbc26cd534)

VIII) To find the top 10 states/UT with total number of persons escaped from police custody in the three years (2016,2017,2018).

![8 escape all](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d0d5e548-e3f4-4ab7-9234-08e85838734b)
![8 escape all](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/d238e3dd-7801-4e50-8f10-02b296dd9e9b)

IX) To find the top 10 states with rape victims in india top 10 states in the year 2016.

![9 victims 2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/9c9c71ef-b0b9-48ba-933b-bbdc63e49b87)
![9 victims2016](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/ff9872ca-3f1f-4f78-9e49-240999466321)

X) To find the top 10 states with rape victims in india top 10 states in the year 2017.

![10 victims 2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/cb3c96bf-807d-423b-8609-2809b476d2b4)
![10 victims2017](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/c6b9bdc6-8a0c-4db8-877d-b4f7b330543d)

XI) To find the top 10 states with rape victims in india top 10 states in the year 2018.

![11 victims 2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/622eb0c7-b232-411d-a398-c49ee31c2619)
![11 victims2018](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/60269cbf-2322-4e41-900b-d389241d13fb)

XII) To find the top 10 states with rape victims in india top 10 states in the three years (2016,2017,2018).

![12 victims all](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/734ce868-9181-471c-ad61-21a14310d36d)
![12 victims all](https://github.com/Ajmalbabayaga/bigdata_project/assets/144656790/fab5bbce-2550-4e34-8b9e-766810c54ca6)


# Conclusion

1.The top 10 States/UTs with Highest Number of Cases Reported (2016, 2017, 2018)
   In conclusion, our analysis has revealed the top 10 states/union territories with the highest number of reported cases over the three-year period (2016-2018). This information can aid in understanding regional trends and facilitating targeted interventions.

2.The top 10 States/UTs with Total Number of Persons Escaped from Police Custody (2016, 2017, 2018)
   To summarize, our investigation has identified the top 10 states/union territories with the highest number of individuals who escaped from police custody during the three-year span (2016-2018). This data may inform efforts to enhance custodial security measures.

3.The top 10 States with Rape Victims in India (2016, 2017, 2018)
   In summary, our research has pinpointed the top 10 states in India with the highest number of reported rape cases over the three-year period (2016-2018). This insight is crucial for addressing and advocating for measures to combat sexual violence in these regions.






   

