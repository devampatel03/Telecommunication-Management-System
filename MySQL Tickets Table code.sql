use tele_dbms;

create table ticket (Ticket_No integer primary key,Issue char(20),Cust_ID integer,
Date_Raised date,Ticket_Status char(20) ,
constraint fk_ticket1 Foreign Key (Cust_ID) References customer(Cust_ID) on update cascade on delete cascade
);

insert into ticket
values (781,'Payment error',1001,'2024-04-15','Pending');

insert into ticket
values (783,'Network Issue',1003,'2024-03-23','Resolved');

insert into ticket
values (785,'Plan not activated',1005,'2024-04-03','Pending');

insert into ticket
values (786,'Refund pending',1007,'2024-04-01','Resolved');

insert into ticket
values (790,'Nework Issue',1008,'2024-04-05','Pending');

select * from ticket;
