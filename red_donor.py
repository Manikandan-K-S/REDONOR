from csv import writer
import csv
import pandas as pd 

class Id():

    def Signup(self,name,mob,passw,typ,loc,age,add):
        add_user().new_user(name,mob,typ,loc,age,add)
        with open('login_details.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow([name,mob,passw])  
            f_object.close()

    def SignIn(self,mob,passw):
        file=open('login_details.csv', mode ='r')
        login = csv.reader(file)  
        for i in login:
            if mob==i[1]:
                if passw==i[2]:
                    file.close()
                    return "True"      
                else:
                    file.close()
                    return "Error:1"                   
        else:
            file.close()
            return "Error:2" 
    


class add_user():

    def new_user(self,name,mob,typ,loc,age,add): #gets user's value and store it in list
        with open('user_details.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow([name,mob,typ,loc,age,add])  
            f_object.close()


class view():

    def show(self,loc,typ): #gets location and type and returns a nested list containing the value
        file=open('user_details.csv', mode ='r')
        csvFile = csv.reader(file)
        a=[]
        for i in csvFile:
            if loc==i[3] and typ==i[2]:
                a.append(i) 
        file.close()
        return a


class change():

    def get_id(self,mob): #gets mobile no and returns the index of the user
        file=open('user_details.csv', mode ='r')
        lst =list(csv.reader(file))
        for i in lst:
            if i[1]==mob:
                return lst.index(i)
                
    def mob(self,indx,new_mob):#gets index and new mobile no to change the no
        file=open('user_details.csv', mode ='r')
        lst =list(csv.reader(file))
        lst[indx][1]=new_mob
        with open('user_details.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerows(lst)
        file.close()
        file=open('login_details.csv', mode ='r')
        lst =list(csv.reader(file))
        lst[indx][1]=new_mob
        with open('login_details.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerows(lst)
        file.close()
        
    def loc(self,indx,new_loc,new_add):#gets index and new location to change the location
        file=open('user_details.csv', mode ='r')
        lst =list(csv.reader(file))
        lst[indx][3]=new_loc
        lst[indx][5]=new_add
        with open('user_details.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerows(lst)
        file.close()


class redonor(add_user,view,change,Id):
    pass
