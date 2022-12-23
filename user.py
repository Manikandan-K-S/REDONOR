from redonor import redonor

import csv

obj=redonor()

def register():
    nam=input("Enter Donor name: ")
    mob=input("Enter Mobile.No: ")
    file=open('user_details.csv', mode ='r')
    lst = csv.reader(file)
    for i in lst:
        if mob==i[1]:
            print("Mobile No is aldready registered.")
            file.close()
            return
    passw=input("Enter your Password: ")
    typ=input("Enter the Blood type: ")
    add=input("Enter your address: ")
    loc=input("Enter the City: ")
    age=input("Enter Donor age: ")
    obj.Signup(nam,mob,passw,typ,loc,age,add)
    print("\nSuccessfully! registered.\n")
    print("\n===========================================")

def view_donor():
    typ=input("Enter required Blood type: ")
    loc=input("Enter required City: ")
    lst=obj.show(loc,typ)
    if lst==[]:
        print("\nOOP! No results found.")
        print("\n===========================================")
    else:
        print('\n',len(lst),"result(s) found.\n\n")
        for x,y in enumerate(lst):
            print(x+1,')',sep='')
            print("Name:",y[0],"\nMobile No:",y[1],"\nAge:",y[4],"\nAddress:",y[5],'\n')
    print("\n===========================================")

def change_mob():
    file=open('login_details.csv', mode ='r')
    lst = csv.reader(file)  
    mob=input("Enter your current Mobile No: ")
    passw=input("Enter your Password: ")
    for i in lst:        
        if mob==i[1] and passw==i[2]:
            new_mob=input("Enter new Mobile No: ")
            obj.mob(obj.get_id(mob),new_mob)
            print("\nMobile No changed successfully.\n")
            print("\n===========================================")
            file.close()
            break
    else:
        print("\nMobile No and Password doesn't match.\n")
        print("\n===========================================")
        return

def change_loc():
    file=open('login_details.csv', mode ='r')
    lst = csv.reader(file)  
    mob=input("Enter your current Mobile No: ")
    passw=input("Enter your Password: ")
    for i in lst:        
        if mob==i[1] and passw==i[2]:
            new_add=input("Enter new address: ")
            new_loc=input("Enter new City:")
            obj.loc(obj.get_id(mob),new_loc,new_add)
            print("\nAddress changed successfully.\n")
            print("\n===========================================")
            file.close()
            break
    else:
        print("\nMobile No and Password doesn't match.\n")
        print("\n===========================================")
        return

def remove_user():
    mob=int(input('Enter User\'s Mobile Number:'))
    obj.remove(mob)
    print('User removed succesfully.')

while True:
    print("\t\t REDONOR\n")
    print("1.Register")
    print("2.View Donor")
    print("3.Change Mobile No")
    print("4.Change Address")
    print("5.Delete User")
    print("6.Exit")
    inpt=int(input("Enter your choice:"))
    if inpt==1: register()
    elif inpt==2: view_donor()
    elif inpt==3: change_mob()
    elif inpt==4: change_loc()
    elif inpt==5: remove_user()
    elif inpt==6: break
    else: print("OOPS! Wrong input!!")

