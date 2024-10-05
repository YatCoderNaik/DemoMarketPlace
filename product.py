# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:52:37 2024

@author: ytn1kor
"""
from category import categ_data
from prettytable import PrettyTable
class product():
    def __init__(self, product_id, category_id, product_name, price, quantity):
        self.product_id =product_id
        self.category_id = category_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

class products():
    global __product_list
    global __product_id
    __product_id = 0
    def __init__(self):
        global __product_list
        __product_list=[]

    def check_duplicate_product(self, product_name):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_name == product_name:                
                return True
            i+=1
        return False
    
    def add_product(self, category_name, product_name, price, quantity):
        global __product_list
        global __product_id
       # global categ_data
        __product_id += 1
        cat_id = categ_data.find_categ_id(category_name)
        if cat_id==-1:
            print("Invalid Category!!")
            return
        if self.check_duplicate_product(product_name):
            print("Duplicate Product Name: ", product_name)
            return
        prod = product(__product_id, cat_id, product_name, price, quantity)
        __product_list.append((prod))

    def delete_prod_on_categ(self, category_id):
        i=0
        while i!=len(__product_list):
            if __product_list[i].category_id==category_id:
                __product_list.pop(i) #Increment is not needed when we do pop
            else:
                i+=1

    def delete_product(self, product_id):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_id == product_id:
                __product_list.pop(i) #Increment is not needed when we do pop
                return
            else:
                i+=1
    
    def print_prod_on_categ(self, category_name):
        global __product_list
        cat_id = categ_data.find_categ_id(category_name)
        if cat_id==-1:
            print("Invalid Category!!")
            return
        print("******************************************") 
        print("             Products for {0}      ".format(category_name))
        print("******************************************") 
        table=PrettyTable()
        table.field_names=["Choice No.", "Product", "Price", "Stock Available"]
        table.align["Choice No."]="r"
        table.align["Product"]="l"
        table.align["Price"]="r"
        table.align["Stock Available"]="r"
        i=0
        j=0
        while i!=len(__product_list):
            if __product_list[i].quantity > 0 and __product_list[i].category_id == cat_id:
                j+=1
                table.add_row([j,__product_list[i].product_name, "₹{:,.2f}".format(__product_list[i].price), __product_list[i].quantity])
            i+=1
        print(table)
        if j==0:
            print("No products under this category!!")
        return j    
    
    def get_prod_id_for_selec(self, category_name, choice):
        global __product_list
        cat_id = categ_data.find_categ_id(category_name)
        if cat_id==-1:
            print("Invalid Category!!")
            return
        i=0
        j=0
        while i!=len(__product_list):
            if __product_list[i].quantity > 0 and __product_list[i].category_id == cat_id:
                j+=1
                if j==choice:
                    return __product_list[i].product_id
            i+=1
            
    def change_quantity(self, product_id, delta):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_id == product_id:
                __product_list[i].quantity += delta
                return
            i+=1
            
    def change_price(self, product_id, price):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_id == product_id:
                __product_list[i].price = price
                return
            i+=1            

    def get_product_id(self, product_name):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_name == product_name:
                return __product_list[i].product_id 
            i+=1
        
    def get_product_name(self, product_id):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_id == product_id:
                return __product_list[i].product_name
            i+=1
    
    def get_product_price(self, product_id):
        i=0
        while i!=len(__product_list):
            if __product_list[i].product_id == product_id:
                return __product_list[i].price
            i+=1
 
#Products
#global prod_data
prod_data = products()
prod_data.add_product("Boots", "Batman Boots", 599, 10)
prod_data.add_product("Boots", "Superman Limited Edition Boots", 999, 2)
prod_data.add_product("Boots", "Spiderman Boots", 599, 10)
prod_data.add_product("Boots", "Deadpool Boots", 599, 10)
prod_data.add_product("Coats", "Batman Coats", 599, 10)
prod_data.add_product("Coats", "Superman Limited Edition Coats", 999, 2)
prod_data.add_product("Coats", "Spiderman Coats", 599, 10)
prod_data.add_product("Coats", "Deadpool Coats", 599, 10)    
prod_data.add_product("Jackets", "Batman Jackets", 599, 10)
prod_data.add_product("Jackets", "Superman Limited Edition Jackets", 999, 2)
prod_data.add_product("Jackets", "Spiderman Jackets", 599, 10)
prod_data.add_product("Jackets", "Deadpool Jackets", 599, 10)    
prod_data.add_product("Caps", "Batman Caps", 599, 10)
prod_data.add_product("Caps", "Superman Limited Edition Caps", 999, 2)
prod_data.add_product("Caps", "Spiderman Caps", 599, 10)
prod_data.add_product("Caps", "Deadpool Caps", 599, 10)