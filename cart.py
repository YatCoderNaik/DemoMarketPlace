# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:04:21 2024

@author: ytn1kor
"""
from prettytable import PrettyTable
from category import categ_data
from product import prod_data

class cart_item:
    def __init__(self, user_id, product_id, no_of_pieces):
        self.user_id = user_id
        self.product_id = product_id        
        self.no_of_pieces = no_of_pieces

class cart:
    global __cart_items
    __cart_items=[]
    
    def __init__(self):
        global __cart_items
        __cart_items=[]
        
    def add_to_cart(self, user_id, product_id, no_of_pieces):
        global __cart_items
        global prod_data
        i=0
        #Case1: Item already present in Cart
        while i!=len(__cart_items):
            if __cart_items[i].product_id == product_id and __cart_items[i].user_id == user_id:
                __cart_items[i].no_of_pieces += no_of_pieces
                prod_data.change_quantity(product_id, -1*no_of_pieces)
                return                
            i+=1  
            
        #Case2: New item to cart
        cart_itm = cart_item(user_id, product_id, no_of_pieces)
        __cart_items.append(cart_itm)
        prod_data.change_quantity(product_id, -1*no_of_pieces)

    #Remove all the products which are deleted by Admin
    def refresh_cart(self):
        global __cart_items
        global prod_data
        i=0
        while i!=len(__cart_items):
            if  prod_data.get_product_name(__cart_items[i].product_id) is None:
                __cart_items.pop(i) #increment not needed since list has been shorten
            else:
                i+=1
        
    def remove_from_cart(self, user_id, product_id):
        global __cart_items
        global prod_data
        i=0
        while i!=len(__cart_items):
            if __cart_items[i].product_id == product_id and __cart_items[i].user_id == user_id:
                prod_data.change_quantity(product_id, __cart_items[i].no_of_pieces)
                __cart_items.pop(i) #increment not needed since list has been shorten
            else:
                i+=1                
                
    def clear_cart(self, user_id, checked_out=False):
        global __cart_items
        global prod_data
        # Items Sold
        if checked_out==True:
            __cart_items.clear()
            return
        # Items removed from cart
        i=0
        while i!=len(__cart_items):
            if  __cart_items[i].user_id == user_id:
                prod_data.change_quantity(__cart_items[i].product_id, __cart_items[i].no_of_pieces)
                __cart_items.pop(i) #increment not needed since list has been shorten
            else:
                i+=1   
                
    def get_cart_total(self, user_id):
        i=0
        total=0
        while i!=len(__cart_items):
            if __cart_items[i].user_id == user_id:
               total += __cart_items[i].no_of_pieces*prod_data.get_product_price(__cart_items[i].product_id)
            i+=1   
        return total    
                
    def print_cart(self, user_id):
        global __cart_items
        global prod_data
        table = PrettyTable()
        table.field_names = ["Item no.","Product Name", "No. of Pieces", "Price"]
        table.align["Item no."] = "r"
        table.align["Product Name"] = "l"
        table.align["No.of Pieces"] = "r"
        table.align["Price"] = "r"
        print("******************************************") 
        print("             Your Cart                    ")
        print("******************************************") 
        i=0
        total=0
        while i!=len(__cart_items):
            if __cart_items[i].user_id == user_id:
               amount = __cart_items[i].no_of_pieces*prod_data.get_product_price(__cart_items[i].product_id)
               formatted_amount = "₹{:,.2f}".format(amount)
               if i+1 != len(__cart_items):
                   table.add_row([ i+1, prod_data.get_product_name(__cart_items[i].product_id),
                                  __cart_items[i].no_of_pieces,
                                  formatted_amount])
               else:
                   table.add_row([ i+1, prod_data.get_product_name(__cart_items[i].product_id),
                                  __cart_items[i].no_of_pieces,
                                  formatted_amount], divider=True) 
               total += __cart_items[i].no_of_pieces*prod_data.get_product_price(__cart_items[i].product_id)
            i+=1   
        table.add_row(["","","Total:","₹{:,.2f}".format(total)], divider=True)
        print(table)
        
    def cart_count(self, user_id):
        global __cart_items
        i=0
        cnt=0
        while i!=len(__cart_items):
            if __cart_items[i].user_id == user_id:
                cnt+=1
            i+=1    
        return cnt
   
    def get_prod_id_for_selec(self, choice, user_id):
        global __cart_items    
        i=0
        j=0
        while i!=len(__cart_items):
            if __cart_items[i].user_id == user_id:
                j+=1
                if j==choice:
                    return __cart_items[i].product_id
            i+=1 

global cart_data
cart_data = cart()