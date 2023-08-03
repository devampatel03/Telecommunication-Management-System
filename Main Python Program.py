#Connecting To MySQL Database
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="@123456",database="telecommunication")
if mycon.is_connected()==False:
    print("Error connecting to mysql database")
cursor=mycon.cursor()

#Defining functions
def Display(a):
    cursor.execute(a)
    data=cursor.fetchall()
    for i in data:
        print(i)

def Add(b):
    cursor.execute(b)
    mycon.commit()
    print("DETAILS ARE ADDED SUCCESSFULLY")

def Update(c):
    cursor.execute(c)
    mycon.commit()
    print("DETAILS ARE UPDATED SUCCESSFULLY")

def Delete(d):
    cursor.execute(d)
    mycon.commit()
    print("DETAILS ARE DELETED SUCCESSFULLY")

#Main Program
print("CUSTOMER DETAILS")
ct="select*from customer"
Display(ct)
while True :
    print('\n')
    print('PRESS 1 FOR SIM TYPE DETAILS')
    print('PRESS 2 FOR CALL RECORDS')
    print('PRESS 3 TO ADD/UPDATE/DELETE CUSTOMER DETAIL')
    print('PRESS 4 TO EXIT PROGRAM')
    choice=int(input('ENTER THE NUMBER='))
    if choice==1:
        print('\n')
        print ('PRESS 1 FOR PREPAID')
        print ('PRESS 2 FOR POSTPAID')
        print ('PRESS 3 TO GET EXIT SIM TYPE SECTION')
        simchoice=int(input('ENTER THE NUMBER='))
        if simchoice==1:
            print('\n')
            print('PRESS 1 TO GET PLAN DETAILS OF ALL CUSTOMERS ')
            print('PRESS 2 TO GET PLAN DETAILS OF A PARTICULAR CUSTOMER ')
            print('PRESS 3 TO EXIT PREPAID SECTION')
            plandetailchoice=int(input('ENTER THE NUMBER='))
            if plandetailchoice==1:
                st1="select * from recharge_plans where Plan_No in ('{}','{}','{}')".format('P1','P7','P10')
                Display(st1)
            elif plandetailchoice==2:
                plan =input('ENTER THE PLAN NUMBER OF THE PARTICULAR CUSTOMER=')
                st2="select * from recharge_plans where Plan_No = '{}' ".format(plan)
                Display(st2)
            elif plandetailchoice==3 :
                continue
        elif simchoice==2:
            print('\n')
            print('PRESS 1 TO GET ALL MONTHLY BILLING DETAILS OF ALL CUSTOMERS ')
            print('PRESS 2 TO GET ALL MONTHLY BILLING DETAILS OF A PARTICULAR CUSTOMER ')
            print('PRESS 3 TO GET TOTAL PAYMENT OF ALL CUSTOMERS')
            print('PRESS 4 TO GET TOTAL PAYMENT OF A PARTICULAR CUSTOMER ')
            print('PRESS 5 TO GET PAYMENT DUE DATE OF A PARTICULAR CUSTOMER ')
            print('PRESS 6 TO EXIT POSTPAID SECTION')
            monthlybillingchoice = int(input('ENTER THE NUMBER='))
            if monthlybillingchoice==1:
                st3="select * from  billing"
                Display(st3)
            elif monthlybillingchoice==2:
                name =input('ENTER THE NAME OF THE PARTICULAR CUSTOMER WHOSE MONTHLY BILLING YOU WANT=')
                st4="select * from  billing  where Name = '{}' ".format(name)
                Display(st4)
            elif monthlybillingchoice==3:
                st5="select Total_Bill from billing"
                Display(st5)
            elif monthlybillingchoice==4:
                name =input('ENTER THE NAME OF THE PARTICULAR CUSTOMER WHOSE TOTAL PAYMENT YOU WANT=')
                st6="select Total_Bill from  billing where Name = '{}' ".format(name)
                Display(st6)
            elif monthlybillingchoice==5:
                name =input('ENTER THE NAME OF THE PARTICULAR CUSTOMER WHOSE PAYMENT DUE DATE YOU WANT')
                st7="select Due_Date from billing  where Name = '{}' ".format(name)
                Display(st7)
            elif monthlybillingchoice==6 :
                continue
        elif simchoice==3:
            continue
    elif choice==2:
        print('\n')
        print('PRESS 1 TO GET DETAILS OF CALL RECORDS OF ALL CUSTOMERS')
        print('PRESS 2 TO GET DETAILS OF CALL RECORDS OF A PARTICULAR CUSTOMER')
        print('PRESS 3 TO EXIT CALL RECORDS SECTION')
        callrecordchoice=int(input('ENTER THE NUMBER='))
        if callrecordchoice==1:
            st8="select * from call_records"
            Display(st8)
        elif callrecordchoice==2:
            name=input('ENTER THE NAME OF THE PARTICULAR CUSTOMER WHOSE CALL RECORD YOU WANT=')
            st9="select * from call_records where Name='{}'".format(name)
            Display(st9)
        elif callrecordchoice==3:
            continue
    elif choice==3:
        print('\n')
        print('PRESS 1 TO ADD A CUSTOMER')
        print('PRESS 2 TO DELETE CUSTOMER DETAIL')
        print('PRESS 3 TO UPDATE CUTOMER DETAIL')
        print('PRESS 4 TO EXIT MODIFY SECTION')
        modifychoice=int(input('ENTER THE NUMBER='))
        if modifychoice==1:
            print('\n')
            print('PRESS 1 FOR PREPAID')
            print('PRESS 2 FOR POSTPAID')
            print('PRESS 3 TO EXIT ADD SECTION')
            addchoice=int(input('ENTER THE NUMBER='))
            if addchoice==1:
                name=input('ENTER THE NAME=')
                Ph_No=int(input('ENTER PHONE NUMBER='))
                plan=input('ENTER THE PLAN=')
                fixrent=int(input('ENTER FIXED RENTAL='))
                st10="insert into customer(Name,Ph_No,Sim_type,Plans,Fixed_rental) values('{}',{},'{}','{}',{})".format(name,Ph_No,'Prepaid',plan,fixrent)
                Add(st10)
                st11="select*from customer"
                Display(st11)
            elif addchoice==2:
                name=input('ENTER THE NAME=')
                Ph_No=int(input('ENTER PHONE NUMBER='))
                fixrent=int(input('ENTER FIXED RENTAL='))
                due_date=input('ENTER DATE IN YYYY-MM-DD=')
                st12="insert into customer(Name,Ph_No,Sim_type,Plans,Fixed_rental) values('{}',{},'{}','{}',{})".format(name,Ph_No,'Postpaid','-',fixrent)
                Add(st12)
                st13="insert into billing(Name,Ph_No,Usage_Rs,Fixed_Rentabl_Rs,Total_GST,Previous_Due,Total_Bill,Due_Date) values('{}',{},{},{},{},{},{},'{}')".format(name,Ph_No,0,fixrent,0,0,0,due_date)
                Add(st13)
                st14="select*from customer"
                Display(st14)
            elif addchoice==3:
                continue
        elif modifychoice==2:
            print('\n')
            print('PRESS 1 FOR PREPAID')
            print('PRESS 2 FOR POSTPAID')
            print('PRESS 3 TO EXIT DELETE SECTION')
            deletechoice=int(input('ENTER THE NUMBER='))
            if deletechoice==1:
                name=input('ENTER NAME THAT IS TO BE DELETED=')
                st15="delete from customer where Name='{}'".format(name)
                Delete(st15)
                st16="select * from customer"
                Display(st16)
            elif deletechoice==2:
                name=input('ENTER NAME THAT IS TO BE DELETED=')
                st17="delete from customer where Name='{}'".format(name)
                Delete(st17)
                st18="delete from billing where Name='{}'".format(name)
                Delete(st18)
                st19="select*from customer"
                Display(st19)
            elif deletechoice==3:
                continue
        elif modifychoice==3:
            print('\n')
            print('PRESS 1 FOR PREPAID')
            print('PRESS 2 FOR POSTPAID')
            print('PRESS 3 TO EXIT UPDATE SECTION')
            updatechoice=int(input('ENTER THE NUMBER='))
            if updatechoice==1:
                print('\n')
                print('PRESS 1 FOR PLAN UPDATE')
                print('PRESS 2 FOR Ph_No UPDATE')
                UPDATE=int(input('ENTER THE NUMBER='))
                if UPDATE==1:
                    rp="select*from recharge_plans"
                    Display(rp)
                    name=input('ENTER NAME OF THE CUSTOMER=')
                    plan=input('ENTER PLAN NUMBER=')
                    st20="update customer set Plans='{}' where Name='{}'".format(plan,name)
                    Update(st20)
                    st21="select*from customer"
                    Display(st21)
                elif UPDATE==2:
                    name=input('ENTER NAME OF THE CUSTOMER=')
                    Ph_No=int(input('ENTER PHONE NUMBER='))
                    st22="update customer set Ph_No={} where Name='{}'".format(Ph_No,name)
                    Update(st22)
                    st23="select*from customer"
                    Display(st23)
            elif updatechoice==2:
                print('\n')
                print('PRESS 1 FOR DUE_DATE UPDATE')
                print('PRESS 2 FOR Ph_No UPDATE')
                UPDATE=int(input('ENTER THE NUMBER='))
                if UPDATE==1:
                    name=input('ENTER NAME OF THE CUSTOMER=')
                    due_date=input('ENTER DUE DATE IN YYYY-MM-DD=')
                    st24="update billing set Due_Date='{}' where Name='{}'".format(due_date,name)
                    Update(st24)
                    st25="select*from billing"
                    Display(st25)
                elif UPDATE==2:
                    name=input('ENTER NAME OF THE CUSTOMER=')
                    Ph_No=int(input('ENTER PHONE NUMBER='))
                    st26="update customer set Ph_No={} where Name='{}'".format(Ph_No,name)
                    Update(st26)
                    st27="update billing set Ph_No={} where Name='{}'".format(Ph_No,name)
                    Update(st27)
                    st28="select*from customer"
                    Display(st28)
        elif modifychoice==4:
            continue
    elif choice==4:
        break
mycon.close()
                    
                    
                    
                    
