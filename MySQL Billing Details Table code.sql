create table billing (Name char(25), Ph_No bigint unique primary key , Usage_Rs float(10,2), Fixed_Rentabl_Rs int, Total_GST float(10,2), Previous_Due float(3,2), Total_Bill float(10,2), Due_Date date);

insert into billing
values('Yashraj Oberoi',8570099914,451.29,45,570.73,004.11,574.84,"2021-06-10");

insert into billing
values('Shraddha Juneja',7400999822,250.11,50,345.12,000.99,346.11,"2020-05-10");

insert into billing
values('Parth Pillai',6942000971,401.00,40,507.15,002.85,510.00,"2021-04-11");

insert into billing
values('Riya Desai',7980428002,211.61,50,300.85,004.51,305.36,"2019-02-12");

insert into billing
values('Rahul Jain',6398728090,140.79,40,207.90,003.11,211.01,"2020-01-09");

select * from billing;
