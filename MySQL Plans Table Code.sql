use tele_dbms;

create table plans
( Plan_No char(3) primary key,
  Price char(10),
  Data char(10),
  Calls char(15),
  SMS char(20),
  Validity char(10),
  Other_benefits char(30) );

insert into plans
values("P1","Rs 409","4 GB/Day","Unlimited","100 SMS/Day","56 Days","Binge all night offer");

insert into plans
values("P2","Rs 559","1.5 GB/Day","Unlimited","100 SMS/Day","84 Days","Weekend data rollover");

insert into plans
values("P3","Rs 149","2 GB","Unlimited","100 SMS","28 Days","Null");

insert into plans
values("P4","Rs 761","3 GB/Day","Unlimited","100 SMS/Day","84 Days","1 Year hotstar VIP");

insert into plans
values("P5","Rs 1157","1.5 GB/Day","Unlimited","100 SMS/Day","180 Days","Zee5 premium-1 year");

insert into plans
values("P6","Rs 1499","24 GB","Unlimited","100 SMS","365 Days","Null");

insert into plans
values("P7","Rs 2359","1.5 GB/Day","Unlimited","100 SMS/Day","365 Days","Zee5 premium-1 year");

insert into plans
values("P8","Rs 499","1.5 GB/Day","Unlimited","100 SMS/Day","70 Days","Weekend data rollover");

insert into plans
values("P9","Rs 447","50 GB","Unlimited","100 SMS","60 Days","Null");

insert into plans
values("P10","Rs 16","1 GB","Null","Null","24 Hours","Null");

select*from plans;
