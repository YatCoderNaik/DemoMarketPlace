# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:50:37 2024

@author: ytn1kor
"""
from prettytable import PrettyTable
class category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class categories:
    global __category_list
    global category_seq
    category_seq=0
    def __init__(self):
        global __category_list
        __category_list=[]
    
    def add_category(self, category_name):
        global __category_list        
        global category_seq
        category_seq = category_seq + 1
        cat = category(category_seq, category_name)
        __category_list.append(cat)

    def delete_category(self, category_id):
        global __category_list
        i=0
        while i!=len(__category_list):
            if __category_list[i].category_id==category_id:
                __category_list.pop(i)
                return
            i+=1    
        
    def find_categ_id(self, category_name):
        global __category_list
        i=0
        while i!=len(__category_list):
            if __category_list[i].category_name==category_name:
                return __category_list[i].category_id
            i+=1    
        return -1
    
    def get_cat_name_for_selec(self, choice):
        global __category_list
        i=0
        j=0
        while i!=len(__category_list):
            j+=1
            if j==choice:
                return __category_list[i].category_name
            i+=1

    def get_cat_id_for_selec(self, choice):
        global __category_list
        i=0
        j=0
        while i!=len(__category_list):
            j+=1
            if j==choice:
                return __category_list[i].category_id
            i+=1
    
    def print_categories(self):
        global __category_list
        table = PrettyTable()
        print("******************************************") 
        print("             Categories                   ")
        print("******************************************") 
        table.field_names = ["Choice No.","Category Name"]
        table.align["Category Name"] = "l"
        table.align["Choice No."] = "r"
        i=0
        j=0
        while i!=len(__category_list):
            j+=1
            table.add_row([j, __category_list[i].category_name])
            i+=1
        #table.add_row([ "-1", "SignOut"])    
        print(table)  

#Categories
#global categ_data
categ_data = categories()
categ_data.add_category("Boots")
categ_data.add_category("Coats")
categ_data.add_category("Jackets")
categ_data.add_category("Caps") 