

use tele_dbms;

create table invoice (Invoice_No integer primary key ,Name char(20),Ph_No bigint ,Sim_type char(20) ,
Invoice_Date date,Total_Payment integer,Payment_Mode char(20),
constraint fk_invoice1 Foreign Key (Name,Ph_No) References personal(Name,Ph_no) on update cascade on delete cascade
);

insert into invoice
values (201,'Yashraj Oberoi',8570099914,'Postpaid','2023-11-02',2999,'Credit Card');

insert into invoice
values (202,'Shraddha Juneja',7400999822,'Postpaid','2023-12-30',3999,'UPI');

insert into invoice
values (203,'Ram Malhotra',9925678011,'Prepaid','2024-01-02',409,'Net Banking');

insert into invoice
values (204,'Parth Pillai',6942000971,'Postpaid','2024-04-15',149,'Debit Card');

insert into invoice
values (205,'Akhil Goenka',8294007000,'Prepaid','2023-05-22',2359,'Credit Card');

insert into invoice
values (206,'Riya Desai',7980428002,'Postpaid','2023-10-11',2999,'UPI');

insert into invoice
values (207,'Rahul Jain',6398728090,'Postpaid','2024-03-21',1999,'UPI');

insert into invoice
values (208,'Ayan Parmar',9825600071,'Prepaid','2023-04-02',16,'Debit Card');

select * from invoice;
	