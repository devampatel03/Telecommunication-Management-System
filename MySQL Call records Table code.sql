create table call_records  (Name char(20),Ph_No bigint unique primary key,Call_logs_per_day char(20) , Call_received_Hour_min char(20), Call_ended_Hour_min char (20),Call_duration_Hour_min char(20),Location_of_phone_number char(20));

insert into call_records
values ('Yashraj Oberoi',8570099914,'6543209122','00:00','01:21','01:21','Tamil Nadu');

insert into call_records
values ('Shraddha Juneja',7400999822,'+4498200091','03:41','03:51','00:10','Canada');


Insert into call_records
Values ('Ram Malhotra',9925678011,'+168709240','06:03','08:09','02:06','America');


Insert into call_records
Values ('Parth Pillai',6942000971,'1800709821','06:53','07:01','00:08','Ranchi');



Insert into call_records
Values ('Akhil Goenka',8294007000,'635940001','11:34','12:09','00:35','Rajasthan');



Insert into call_records
Values ('Riya Desai',7980428002,'9924320900','14:09','16:00','02:51','Madhya Pradesh');




Insert into call_records
Values ('Rahul Jain',6398728090,'9666270801','11:00','12:21','01:21','Uttar Pradesh');

Insert into call_records
Values ('Ayan Parmar',9825600071,'','-','-','-','-');

select * from call_records;
