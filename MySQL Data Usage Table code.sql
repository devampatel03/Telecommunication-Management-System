use tele_dbms;

create table data_usage (Name char(20),Ph_No bigint ,Session_Start_Time char(20),
Session_End_Time char(20),Data_Usage_Gb integer,Remaining_Data_Gb integer,
constraint fk_usage1 Foreign Key (Name,Ph_No) References personal(Name,Ph_no) on update cascade on delete cascade
);

insert into data_usage
values ('Yashraj Oberoi',8570099914,'12:00','12:30',0.5,1.97);

insert into data_usage
values ('Shraddha Juneja',7400999822,'22:12','04:30',30.5,65.7);

insert into data_usage
values ('Ram Malhotra',9925678011,'09:00','11:30',12,0.56);

insert into data_usage
values ('Parth Pillai',6942000971,'03:00','12:30',223,500);

insert into data_usage
values ('Akhil Goenka',8294007000,'22:12','04:30',3,5);

insert into data_usage
values ('Riya Desai',7980428002,'23:00','12:30',0.2,1);

insert into data_usage
values ('Rahul Jain',6398728090,'10:00','12:30',4.8,6.97);

insert into data_usage
values ('Ayan Parmar',9825600071,'13:00','18:30',7.5,14.97);

select * from data_usage;
