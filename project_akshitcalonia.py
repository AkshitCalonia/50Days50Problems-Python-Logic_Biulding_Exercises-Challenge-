import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="dps123", charset="utf8")
cur = mydb.cursor()
cur.execute("Create database if not exists AKHospital")
cur.execute("use AKHospital")
cur.execute("create table if not exists Patient(PNo varchar(9) primary key, Patient_Name varchar(25), Diagnosis varchar(30), DOB date, RoomNo integer(3);")
mydb.commit()

def insert_data():
    while True:
        try:
            n = int(input("How many records you want to enter : "))
            break
        except Exception:
            print("*"*20, "\nError!! Try again enting data in numeric form!\n", "*"*20)
    for i in range(n):
        PNo = input("Enter a Patient Number : ")
        Patient_Name = input("Enter Patient Name : ")
        Diagnosis = input(f"Enter Medical Condition for {Patient_Name} : ")
        DOB = input("Enter the Date in correct format (yyyy/mm/dd) : ")
        RoomNo = input("Enter the Room Number : ")

        try:
            cur.execute("insert into Patient values('"+PNo+"', '"+Patient_Name+"', '"+Diagnosis+"', '"+DOB+"', '"+RoomNo+"')")
            mydb.commit()
            print("RECORDS ADDED SUCCESSFULLY IN SYSTEM!")

        except Exception:
            print("*"*20, "\nError!! Try again enting data in the mentioned format!\n", "*"*20)
            break



def update():
    while True:
        try:
            n = int(input("How many records to update? : "))
            break
        except Exception:
            print("*"*20, "\nError!! Try again enting data in the numeric form!\n", "*"*20)
            
    for i in range(1, n+1):
        PNo = input(f"Enter Patient Number for your update No. {i} here : ")
        print("Here are the Details\n")
        cur.execute("select * from Patient where PNo = '"+PNo+"';")
        for i in cur:
            print(i)
        Patient_Name = input("Enter Patient Updated Name : ")
        Diagnosis = input(f"Enter Updated Medical Condition for {Patient_Name} : ")
        DOB = input("Enter the Updated Date in correct format (yyyy/mm/dd) : ")
        RoomNo = input("Enter the Updated Room Number : ")
        try:
            cur.execute("update Patient set Patient_Name = '"+Patient_Name+"', Diagnosis = '"+Diagnosis+"', DOB = '"+DOB+"', RoomNo = '"+RoomNo+"' where PNo = '"+PNo+"';")
            mydb.commit()
            print("RECORDS SUCCESSFULLY UPDATED!")
        except Exception:
            print("*"*20, "\nError!! Try again enting data in the mentioned format!\n", "*"*20)
            break



def delete():
    while True:
        try:
            n = int(input("How many records to Delete ? : "))
            break
        except Exception:
            print("*"*20, "\nError!! Try again enting data in the numeric form!\n", "*"*20)
            
    for i in range(n):
        PNo = input("Enter the Patient Number to be deleted from records : ")
        try:
            cur.execute("delete from salary where PNo = '"+PNo+"';")
            mydb.commit()
            print("RECORDS DELETED SUCCESSFULLY FROM SYSTEM!")

        except Exception:
            print("*"*20, "\nError!! Try again entering valid data!\n", "*"*20)
            break

def view():
    cur.execute("Select * from Patient")
    for i in cur:
        print(i)

print("@"*10, "\t\tWelcome to AKHospital Management Frontdesk\t\t", "@"*10)
while True:
    print("")
    
            
            







        
