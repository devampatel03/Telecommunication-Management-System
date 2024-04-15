

use tele_dbms;

create table recharge (Recharge_ID integer primary key ,Name char(20),Ph_No bigint ,
Plan_No char(3),Recharge_Date date,Due_Date date,Activation_Time char(20),Price char(10),
constraint fk_recharge1 Foreign Key (Name,Ph_No) References personal(Name,Ph_no) on update cascade on delete cascade,
constraint fk_recharge2 Foreign Key (Plan_No) references plans(Plan_No)on update cascade on delete cascade);



insert into recharge
values (203,'Ram Malhotra',9925678011,'P1','2024-01-02','2024-02-02','18:00',409);
insert into recharge
values (205,'Akhil Goenka',8294007000,'P7','2023-05-22','2024-01-01','07:30',2359);
insert into recharge
values (208,'Ayan Parmar',9825600071,'P10','2023-04-02','2026-04-02','23:34',16);

select * from recharge;
