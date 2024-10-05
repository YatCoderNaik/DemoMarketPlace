# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:49:13 2024

@author: ytn1kor
"""
from prettytable import PrettyTable
class user:
    def __init__(self, user_id, username, password, is_admin):
        self.user_id= user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin
    
    def print_user(self):
        print("Name:",self.username,", Password:",self.password,", Is_Admin:",str(self.is_admin))

class users:
    global __users_list
    global user_id
    user_id=0
    def __init__(self):
        global __users_list
        __users_list=[]
        
    def add_user(self, username, password, is_admin):
        global user_id
        user_id+=1
        __users_list.append(user(user_id, username, password,is_admin))
        #print(username, "added successfully!! ")
    
    def delete_user(self, user_id):
        global __users_list
        i=0
        while i != len(__users_list):
            if __users_list[i].user_id == user_id:
                __users_list.pop(i)
                return
            i=i+1      

    def check_duplicate_user(self, username):
        i=0
        while i != len(__users_list):
            if __users_list[i].username == username:
                return 1 
            i+=1
        return 0       
    
    def validate_user(self, username, password):
        i=0
        while i != len(__users_list):
            if __users_list[i].username == username and __users_list[i].password == password:
                if __users_list[i].is_admin == True:
                    return 2 #Admin User
                else:
                    return 1 #Normal User
            i+=1
        return 0 # User not present   

    def get_user_id(self, username):
        global __users_list
        i=0
        while i != len(__users_list):
            if __users_list[i].username == username:
                return __users_list[i].user_id
            i=i+1        

    def get_user_name(self, user_id):
        global __users_list
        i=0
        while i != len(__users_list):
            if __users_list[i].user_id == user_id:
                return __users_list[i].username
            i=i+1

    def get_user_id_selec(self, choice, only_admin=False):
        i=0
        j=0
        if only_admin == False:
            while i != len(__users_list):
                j+=1
                if j==choice:
                    return __users_list[i].user_id
                i=i+1
        else:
            while i != len(__users_list):
                if __users_list[i].is_admin == True:
                    j+=1
                    if j==choice:
                        return __users_list[i].user_id
                i=i+1        
    
    def print_users(self,is_admin=False):
        global __users_list
        table=PrettyTable()
        print("******************************************") 
        print("             Admin Users                   ")
        print("******************************************")
        table.field_names=["Choice No.", "Username"]
        table.align["Choice No."] = "r"
        table.align["Username"]="l"
        i=0
        j=0
        if is_admin==True:
            while i != len(__users_list):
                if __users_list[i].is_admin == True:
                    j+=1                    
                    table.add_row([j,__users_list[i].username])
                i=i+1
        else:
            while i != len(__users_list):                
                j+=1
                table.add_row([j,__users_list[i].username])
                i=i+1
        print(table)    

# User Creation        
#global users_data
users_data = users()
users_data.add_user("Yathish", "Yathish_Pass", False)
users_data.add_user("Kiran", "Kiran_Pass", False)
users_data.add_user("Admin", "Admin", True)
#users_data.print_users()  