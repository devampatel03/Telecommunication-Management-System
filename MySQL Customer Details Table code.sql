

use tele_dbms;

create table customer (Cust_ID integer primary key ,Name char(20),Ph_No bigint ,Sim_type char(20) , Plan_No char(3), Fixed_rental integer,
constraint fk_cust1 Foreign Key (Name,Ph_No) References personal(Name,Ph_no) on update cascade on delete cascade,
constraint fk_cust2 Foreign Key (Plan_No) references recharge_plans(Plan_No)on update cascade on delete cascade);

insert into customer
values (1001,'Yashraj Oberoi',8570099914,'Postpaid',null,45);

insert into customer
values (1002,'Shraddha Juneja',7400999822,'Postpaid',null,50);

insert into customer
values (1003,'Ram Malhotra',9925678011,'Prepaid','P1',50);

insert into customer
values (1004,'Parth Pillai',6942000971,'Postpaid',null,40);

insert into customer
values (1005,'Akhil Goenka',8294007000,'Prepaid','P7',90);

insert into customer
values (1006,'Riya Desai',7980428002,'Postpaid',null,50);

insert into customer
values (1007,'Rahul Jain',6398728090,'Postpaid',null,40);

insert into customer
values (1008,'Ayan Parmar',9825600071,'Prepaid','P10',10);

select * from customer;
