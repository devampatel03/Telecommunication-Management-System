use tele_dbms;

create table coupon (Coupon_No integer primary key,Brand char(20),Price integer,
Valid_Upto date
);

insert into coupon
values (322,'Ajio',1000,'2025-04-03');

insert into coupon
values (342,'Puma',750,'2024-12-01');

insert into coupon
values (343,'Mamaearth',350,'2024-07-22');

insert into coupon
values (345,'Amazon Pay',150,'2025-11-14');

insert into coupon
values (356,'Cred',450,'2024-10-23');

select * from coupon;
