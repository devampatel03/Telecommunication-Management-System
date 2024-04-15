use tele_dbms;

create table personal (Name char(20) not null,Ph_No bigint unique ,Alt_Ph_No bigint ,
Address char(20) , Email_ID char(20), DOB date ,Aadhaar_no bigint unique not null ,primary key (Name,Ph_No));

insert into personal
values ('Yashraj Oberoi',8570099914,8475647384,'Gujarat','yashraj@gmail.com','2002-04-15',657465746574);

insert into personal
values ('Shraddha Juneja',7400999822,7647364736,'Maharashtra','Shraddha@gmail.com','2000-12-08',345432675467);

insert into personal
values ('Ram Malhotra',9925678011,9746584673,'Rajasthan','Malhotra@gmail.com','1975-01-15',357689065435);

insert into personal
values ('Parth Pillai',6942000971,null,'Gujarat','Parth@gmail.com','1995-06-22',985674325675);

insert into personal
values ('Akhil Goenka',8294007000,null,'Tamil Nadu','Akhil@gmail.com','1998-11-30',786543215567);

insert into personal
values ('Riya Desai',7980428002,9836475837,'Punjab','Riya@gmail.com','2004-02-25',908996754342);

insert into personal
values ('Rahul Jain',6398728090,null,'Arunachal Pradesh','Rahul@gmail.com','1986-05-25',899776554654);

insert into personal
values ('Ayan Parmar',9825600071,4658363789,'Sikkim','Ayan@gmail.com','2001-07-15',879654356784);

select * from personal;


