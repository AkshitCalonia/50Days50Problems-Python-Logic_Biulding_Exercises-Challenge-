import mysql.connector
import time
mydb = mysql.connector.connect(host="localhost", user="root", passwd="dps123", charset="utf8")
cur = mydb.cursor()
cur.execute("Create database if not exists AKHospital")
cur.execute("use AKHospital")
cur.execute("create table if not exists Patient(PNo varchar(9) primary key, Patient_Name varchar(25), Diagnosis varchar(30), DOB date, RoomNo integer(3));")
cur.execute("create table if not exists Log(PNo varchar(20) primary key, passw varchar(20));")
mydb.commit()

def insert_data():
    while True:
        try:
            n = int(input("How many records you want to enter : "))
            break
        except Exception:
            print("*"*20, "\nError!! Try again enting data in numeric form!\n", "*"*20)
    for i in range(n):
        PNo = input("Enter a Patient ID : ")
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
        PNo = input(f"Enter Patient ID for your update No. {i} here : ")
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
        PNo = input("Enter the Patient ID to be deleted from records : ")
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



def cuslogin():
    for i in range(5, 0, -1):
        print(f"Logging in in {i}....")
            time.sleep(1)
    print("\nWelcome to the LOGIN Portal!")
    
    ps = "uk"
    while True:
        PNo = input(f"Enter the LOGIN ID :  ")
        upass = input("Enter the Password : ")
        cur.execute("select * from Log")
        m = False
        for i in cur:
            if PNo in i and upass in i:
                print("\nLOGIN Success!")
                m = True
                ps = "go"
        
        if m == False:
            print("LOGIN ID/Password didn't match. Try again or of register yourself!")
            print("Enter 1 to Try again\nEnter 2 to exit LOGIN window")
            d = input("Please tell : ")
            if d == "1":
                continue
            elif d == "2":
                break
            
        elif m == True:
            break
        
    if ps == "go":
        while True:
            print("\nWelcome to Your Portal !")
            print("Press 1 to Add Patient Details")
            print("Press 2 to Update Patient Details")
            print("Press 3 to Delete Patient Details")
            print("Press 4 to View all records in Management!")
            print("Press 0 to LOG OUT")
            r = int(input("Enter the Desired Action  :  "))
            if r == 1:
                insert_data()
            elif r == 2:
                update()
            elif r == 3:
                delete()
            elif r == 4:
                view()
            elif r == 0:
                for i in range(5, 0, -1):
                    print(f"Logging out in {i}")
                    time.sleep(1)
                print("Logged Out Success!")
                break
            else:
                print("Invalid Input Given, try again !")
        
        
    
def newreg():
    print("\nWelcome to New Patient Registration Portal!")
    n = int(input("How many patients you want to register ? : "))
    for i in range(1, n+1):
        print(f"Let's start with details for Patient No. {i}")
        nm = input("Enter the Patient Name : ")
        while True:
            PNo = input(f"Enter a unique UserID for {nm}:  ")
            cur.execute("Select * from Log")
            k = False
            for i in cur:
                if userid in i:
                    print("This ID already exists, try something else!")
                    k = True
                else:
                    print("This ID is unique! We're good to go :)")
            if k == False:
                break
        passw = input(f"Enter a password (Do not Share with anyone else) for {nm}'s account :  ")
        cur.execute("insert into Log values('"+PNo+"', '"+passw+"')")
        mydb.commit()
    print("Patient(s) added SUCCESSFULLY!")
    t = input("\nWant to proceed to LOGIN? (Y/N): ").upper()
    if t == "Y":
        cuslogin()

        

print("@"*10, "\t\tWelcome to AKHospital Management Frontdesk\t\t", "@"*10)
while True:
    print("\nPress 1 for Customer Login (If account already exists)")
    print("Press 2 to Register as a New Customer")
    print("Press 0 to Exit")
    try:
        ch = int(input("Enter your action   :   "))
    except Exception:
        print("You're requested to enter details correctly.")

    if ch == 1:
        cuslogin()
    elif ch == 2:
        newreg()
    elif ch == 0:
        print("Thank You for using the Hospital Management Desk!\nWe appreciate you seeing back!")
        break
    else:
        print("Unrognizable Input recieved, Try again ! ")








        
