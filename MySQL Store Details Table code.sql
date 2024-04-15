use tele_dbms;

create table store (Store_No integer primary key,Address char(20),City char(20),Contact_No bigint 
);

insert into store
values (1900,'Gujarat','Surat',7867564736);

insert into store
values (1901,'Uttar Pradesh','Lucknow',7898675643);

insert into store
values (1902,'Gujarat','Ahmedabad',9089898999);

insert into store
values (1903,'Gujarat','Rajkot',7878788987);

insert into store
values (1904,'Maharashtra','Mumbai',6767677565);

insert into store
values (1905,'Delhi','Noida',2534564534);

insert into store
values (1906,'Tamil Nadu','Chennai',3434345656);

insert into store
values (1907,'Gujarat','Surat',3435343635);

insert into store
values (1908,'Gujarat','Vadodara',6745563746);

insert into store
values (1909,'Punjab','Ludhiana',4536574836);


select * from store;
