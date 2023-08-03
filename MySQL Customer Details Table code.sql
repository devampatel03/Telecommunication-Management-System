create table customer (Name char(20) not null,Ph_No bigint unique primary key ,Sim_type char(20) , Plans char(20), Fixed_rental integer);

insert into customer
values ('Yashraj Oberoi',8570099914,'Postpaid','-',45);

insert into customer
values ('Shraddha Juneja',7400999822,'Postpaid','-',50);

insert into customer
values ('Ram Malhotra',9925678011,'Prepaid','P1',50);

insert into customer
values ('Parth Pillai',6942000971,'Postpaid','-',40);

insert into customer
values ('Akhil Goenka',8294007000,'Prepaid','P7',90);

insert into customer
values ('Riya Desai',7980428002,'Postpaid','-',50);

insert into customer
values ('Rahul Jain',6398728090,'Postpaid','-',40);

insert into customer
values ('Ayan Parmar',9825600071,'Prepaid','P10',10);

select * from customer;
