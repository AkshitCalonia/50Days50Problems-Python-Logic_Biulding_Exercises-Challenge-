import os, time
ch = input("Destroy ? (Y/N)  :  ")

def shutit():
    for j in range(10, 0, -1):
        print(f"Destroying system in {j}....")
        time.sleep(1)
    print("Goodbye! :)")
    os.system("shutdown /s /t 1")

if ch.upper() == "Y":
    shutit()
else:
    print("Really, but we'll don't let you decide anyways!!!")
    shutit()
