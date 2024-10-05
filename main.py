# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:26:16 2024

@author: ytn1kor
"""
import sys
import time
import itertools
from prettytable import PrettyTable
from user import users_data
from category import categ_data
from product import prod_data
from cart import cart_data

global logged_in_user_id
global admin_login
logged_in_user_id=0
admin_login=False

def do_login(username, password):
    global __users_list
    global logged_in_user_id
    global admin_login
    is_valid_user = users_data.validate_user(username, password)
    
    if is_valid_user==2:
        admin_login=True 
        
    if is_valid_user in (1, 2):
        logged_in_user_id = users_data.get_user_id(user_name)
        return 1
    else:    
        return 0

def do_logout():
    global logged_in_user_id
    global admin_login
    logged_in_user_id=0
    admin_login=False

#Logic specific to IPython
def clear_screen():
    from IPython import get_ipython
    get_ipython().magic('clear')


def show_header(is_after_login=True):
    global users_data
    global cart_data
    print("")
    print("************************************************************* ")
    print("           Welcome to the Demo MarketPlace                    ")
    print("************************************************************* ")
    if is_after_login==True:
        if admin_login == False:
            print("User: ", str(users_data.get_user_name(logged_in_user_id)), " Items in Cart: ", cart_data.cart_count(logged_in_user_id))
        elif admin_login == True:
            print("User: ", str(users_data.get_user_name(logged_in_user_id)))

def show_cart():
    cart_option_selected1 =0;
    cart_option_selected2 =0;
    while True:
        try:
            clear_screen()
            show_header()
            print("")
            cart_data.print_cart(logged_in_user_id)
            print("[-1] Go Back [1]Remove item  [2]Clear cart")
            cart_option_selected1 = int(input("\nPlease enter your choice: "))
            
            if cart_option_selected1 == -1:
                break
            elif cart_option_selected1 == 1:
                cart_option_selected2 = int(input("Choose an item in the cart to remove: "))
                cart_data.remove_from_cart(logged_in_user_id, cart_data.get_prod_id_for_selec(cart_option_selected2, logged_in_user_id))
                print("Item removed successfully!!");
                time.sleep(1)
                if cart_data.cart_count(logged_in_user_id) == 0:
                    break
            elif cart_option_selected1 ==2:
                cart_data.clear_cart(logged_in_user_id)
                print("Cart cleared successfully!!");
                time.sleep(1)
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            input("Please press enter to try again!")  

def show_processing_symbol(message, duration=5):
    # A list of symbols to represent the spinner
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    
    # Get the start time
    start_time = time.time()

    # Run the spinner for the given duration
    while time.time() - start_time < duration:
        # Get the next symbol and print it without a newline
        sys.stdout.write(next(spinner))
        sys.stdout.flush()  # Flush the output to ensure it appears on the screen
        time.sleep(0.1)     # Sleep for a short time to control the speed of the spinner
        sys.stdout.write('\b')  # Move the cursor back so the next symbol overwrites the previous one

    print(message)
        
def check_out(user_id):
    while True:
        try:
            clear_screen()
            show_header()
            print("")
            cart_data.print_cart(user_id)
            print("Payment mode: [-1] Go Back [1]Net Banking [2]PayPal [3]UPI [4]Payment Gateway")
            option_selected = int(input("Please choose the payment mode: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            input("Please press enter to try again!")  
            
        #Cancel
        if option_selected == -1:
            break
        
        #Payment 
        if option_selected in (1, 2, 3, 4):
            total = cart_data.get_cart_total(logged_in_user_id)
            if option_selected == 1:
                pay_mode = "Net Banking merchant page is opened in another window to make a payment of "+"₹{:,.2f}".format(total)
            elif option_selected == 2:
                pay_mode = "Paypal payment link is sent to your mobile number to make a payment of "+"₹{:,.2f}".format(total)
            elif option_selected == 3:
                pay_mode = "UPI app is opened in your mobile to make a payment of "+"₹{:,.2f}".format(total)
            elif option_selected == 4:
                pay_mode = "Payment gateway is opened in another window to make a payment of "+"₹{:,.2f}".format(total)
            print("Connecting to Payment Gateway..")
            show_processing_symbol(pay_mode)
            input("Please finish the payment and press enter key.")
            show_processing_symbol("Payment Recieved.")
            input("Thanks for shopping with us. Your items will reach you soon. Press enter to go back.")
            cart_data.clear_cart(user_id, True)
            time.sleep(1)
            break

#------------------- Main Start -----------------------------#


#Login Menu
while True:
    option_selected=0
    while True:
        try:
            table = PrettyTable()
            table.field_names = ["Choice No.", "Choice Details"]
            table.align["Choice Details"] = "l"
            table.add_rows(
                            [
                                [1, "Login"],
                                [2, "Sign-Up"],
                            ]
                           )
            table.align["Choice No."]="r"
            clear_screen()
            show_header(is_after_login=False)
            print("")
            print(table)
            print("[-1] Exit")
            option_selected = int(input(" Your Choice: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            input("Please press enter to try again!")
    
    # 3 - Exit
    if option_selected == -1:
        print("Thanks, See you later!!")
        break

    # 2 - Signup
    if option_selected == 2:
        while True:                               
          username = input("Enter the username: ")
          password = input("Enter the password: ")
          if username.strip() == "":
              print("Username can't be blank!!")
              time.sleep(1)
              continue
          elif users_data.check_duplicate_user(username):
              print(" user {0} is already present. Please try some other name ".format(username))
              time.sleep(1)
              continue
          elif password.strip() == "":
              print("Password can't be blank!!")
              time.sleep(1)
              continue
          else:
              users_data.add_user(username, password, False)
              print("User is added successfully! You can login now.")
              time.sleep(1)
              break
        continue
      
    # 1 - Login        
    if option_selected == 1:
        login_status = False    
        while login_status==False:
            clear_screen()
            show_header(is_after_login=False)
            user_name = input("Please enter username: ")
            password = input("Please enter password: ")    
            if do_login(user_name, password):
                login_status = True
                print("Login Successfull!!")
                time.sleep(1)            
            else:
                login_status = False
                print("Login Failed!!")
                input("Press enter to try again!!")
                
    
    #Normal User
    if admin_login==False:    
        # Categories Menu           
        option_selected=0
        while True:
            try:
                clear_screen()
                show_header()
                print("")
                categ_data.print_categories()
                cart_count = cart_data.cart_count(logged_in_user_id)
                if cart_count == 0:
                    print("[-1] Signout")
                else:
                    print("[-1] Signout [-2] Show Cart [-3] Check out")
                option_selected=int(input("Choose a category to continue/Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                input("Please press enter to try again!")
                continue
        
            #-1 - Signout
            if option_selected == -1:
                do_logout()
                break
            #-2 -Show Cart
            if option_selected == -2:
               show_cart() 
               continue
            
            if option_selected == -3:
                check_out(logged_in_user_id)
                continue
               
            if option_selected not in (-1, -2, -3):   
                cat_selec = categ_data.get_cat_name_for_selec(option_selected)
                
             # Products Menu           
            option_selected=0
            no_of_pieces=0
            while True:
                try:
                    clear_screen()
                    show_header()
                    print("")
                    prod_data.print_prod_on_categ(cat_selec)
                    cart_count = cart_data.cart_count(logged_in_user_id)
                    if cart_count == 0:
                        print("[-1] Go back to Categories")
                    else:
                        print("[-1] Go back to Categories [-2] Show Cart [-3] Check out")
                    option_selected=int(input("Choose a product to add to cart/Enter your choice: "))
                    if option_selected not in (-1,-2, -3):
                       no_of_pieces= int(input("Please enter the number of pieces: "))
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    input("Please press enter to try again!")
                    
                # -1 - Go back to Categories
                if option_selected == -1:
                    break
                
                if option_selected == -2:
                   show_cart()
                   continue
                   
                if option_selected == -3:
                    check_out(logged_in_user_id) 
                    continue
                    
                if option_selected not in (-1, -2, -3):
                    cart_data.add_to_cart(logged_in_user_id, 
                                          prod_data.get_prod_id_for_selec(cat_selec,option_selected), 
                                          no_of_pieces) 
                    print("Added to cart successfully!!")
                    time.sleep(1)
    elif admin_login==True:
         # Categories Menu           
         option_selected=0
         while True:
             try:
                 clear_screen()
                 show_header()
                 table = PrettyTable()
                 table.field_names = ["Choice No.", "Choice Details"]
                 table.align["Choice Details"] = "l"
                 table.add_rows(
                                 [
                                     [1, "Manage Categories and Products"],
                                     [2, "Manage Admin Users "],
                                 ]
                                )
                 table.align["Choice No."]="r"
                 table.align["Choice Details"]="l"
                 print("")
                 print("******************************************") 
                 print("             Admin Menu                   ")
                 print("******************************************") 
                 print("")
                 print(table)
                 print("[-1] Signout")
                 option_selected=int(input("Your choice:"))
             except ValueError:
                    print("Invalid input. Please enter an integer.")
                    input("Please press enter to try again!")
                    continue  
                
             #-1 - Signout
             if option_selected == -1:
                do_logout()
                break
            
             #1 - Manage Categories
             if option_selected == 1:
                # Categories Menu           
                option_selected=0
                category_selected=0
                while True:
                    try:
                        clear_screen()
                        show_header()
                        print("")
                        categ_data.print_categories()
                        print("[-1] Go back [1] Add Category [2] Delete Category [3]Edit products in a category ")
                        option_selected=int(input("Your choice: "))
                        if option_selected == 2: 
                           validate = input("Deleting a category also delete all the products under that category. Can you confirm? [Y/N]: ")
                           if validate.lower()=="y":
                               category_selected=int(input("Choose a category to delete: "))
                               cat_id = categ_data.get_cat_id_for_selec(category_selected)
                               print(cat_id)
                               categ_data.delete_category(cat_id)
                               prod_data.delete_prod_on_categ(cat_id)
                               cart_data.refresh_cart()
                               print("Category and its products deleted successfully!!")
                               print("User carts updated!!")
                               time.sleep(1)
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                        input("Please press enter to try again!")
                        continue
                
                    #-1 - Signout
                    if option_selected == -1:
                        do_logout()
                        break
                    
                    # 1 - Add Category
                    if option_selected == 1:
                       category_name = input("Enter the category name: ") 
                       if category_name is not None:
                           categ_data.add_category(category_name)
                           print("Category added successfully!!")
                           time.sleep(1)
                       else:
                           print("Error!! Category Name can't be blank.")
                           
                    # 3 - Edit Product in Category
                    if option_selected == 3:
                        category_selected=int(input("Choose a category: "))
                        category_selected = categ_data.get_cat_name_for_selec(category_selected)
                        while True:
                            try:
                                clear_screen()
                                show_header()
                                print("")                                
                                prod_data.print_prod_on_categ(category_selected)
                                print("[-1] Go back [1] Add Product [2] Delete Product [3]Change Price [4]Increase/Decrease Stock")
                                option_selected=int(input("Your choice: "))
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                input("Please press enter to try again!")
                                continue   
                           
                            # -1 - Go back
                            if option_selected == -1:
                                break;
                            
                            # 1 - Add Product
                            if option_selected == 1:
                                while True:
                                    try:
                                        product_name = input("Enter the product name: ")
                                        prod_price = int(input("Enter the price: "))
                                        prod_quantity = int(input("Enter the Quantity: "))
                                        if product_name.strip() != "":                                         
                                            if  prod_data.check_duplicate_product(product_name):
                                                print("Duplicate product name. Please try some other name!!")
                                                time.sleep(1)
                                                continue
                                            elif prod_price < 0:
                                                print("Error!! Price should be greater than zero")
                                                time.sleep(1)
                                                continue
                                            elif prod_quantity < 0:
                                                print("Error!! Quantity shouldn't be less than zero")
                                                time.sleep(1)
                                                continue                                                
                                            else:
                                                prod_data.add_product(category_selected, product_name, prod_price, prod_quantity)
                                                print("Product added successfully!!")
                                                time.sleep(1)
                                                break
                                    except ValueError:
                                        print("Invalid input. Please enter an integer.")
                                        input("Please press enter to try again!")
                                        continue
                            
                            # 2 - Delete Product
                            if option_selected == 2:
                                try:                                    
                                    product_selected=int(input("Choose a product to delete: "))
                                    product_selected = prod_data.get_prod_id_for_selec(category_selected, product_selected)
                                    prod_data.delete_product(product_selected)
                                    print("Product deleted successfully!!")
                                    time.sleep(1)
                                    continue
                                except ValueError:
                                    print("Invalid input. Please enter an integer.")
                                    input("Please press enter to try again!")
                                    continue     
                                
                            # 3 - Change Price
                            if option_selected == 3: 
                                try:                                   
                                    product_selected=int(input("Choose a product to adjust price: "))
                                    prod_price=int(input("Enter the new price: "))
                                    if prod_price <= 0:
                                       print("Error!! Price should be greater than zero")
                                       time.sleep(1)
                                       continue 
                                    product_selected = prod_data.get_prod_id_for_selec(category_selected, product_selected)
                                    prod_data.change_price(product_selected, prod_price)
                                    print("Product price updated successfully!!")
                                    time.sleep(1)
                                    continue
                                except ValueError:
                                    print("Invalid input. Please enter an integer.")
                                    input("Please press enter to try again!")
                                    continue
                                
                            # 4 - Change Quantity
                            if option_selected == 4: 
                                try:                                   
                                    product_selected=int(input("Choose a product to adjust Quantity: "))
                                    prod_quan=int(input("Enter the new Quantity: "))
                                    if prod_price < 0:
                                       print("Error!! Quantity shouldn't be less than zero")
                                       time.sleep(1)
                                       continue 
                                    product_selected = prod_data.get_prod_id_for_selec(category_selected, product_selected)
                                    prod_data.change_quantity(product_selected, prod_quan)
                                    print("Product quantity updated successfully!!")
                                    time.sleep(1)
                                    continue
                                except ValueError:
                                    print("Invalid input. Please enter an integer.")
                                    input("Please press enter to try again!")
                                    continue
             elif option_selected == 2:
                  option_selected=0
                  while True:
                      try:
                          clear_screen()
                          show_header()
                          users_data.print_users(is_admin=True)
                          print("[-1] Go back [1] Add admin user [2] Delete admin user")
                          option_selected=int(input("Your choice:"))
                      except ValueError:
                        print("Invalid input. Please enter an integer.")
                        input("Please press enter to try again!")
                        continue    
                    
                      # -1 Go Back
                      if option_selected == -1:
                         break
                     
                      # 1 Add Admin User
                      if option_selected == 1:
                          while True:                               
                            username = input("Enter the username: ")
                            password = input("Enter the password: ")
                            if username.strip() == "":
                                print("Username can't be blank!!")
                                time.sleep(1)
                                continue
                            elif users_data.check_duplicate_user(username):
                                print(" user {0} is already present. Please try some other name ".format(username))
                                time.sleep(1)
                                continue
                            elif password.strip() == "":
                                print("Password can't be blank!!")
                                time.sleep(1)
                                continue
                            else:
                                users_data.add_user(username, password, True)
                                print("User is added successfully!")
                                time.sleep(1)
                                break
                    
                      if option_selected==2:
                          username=int(input("Please choose the user to delete: "))
                          user_id=users_data.get_user_id_selec(choice=username, only_admin=True)
                          username= users_data.get_user_name(user_id)
                          if user_id == logged_in_user_id:
                              print("You can't delete your own user.")
                              time.sleep(1)
                              continue
                          elif username == "Admin":
                              print("Admin is a default admin user. Deletion of this user is not allowed.")
                              time.sleep(1)
                              continue
                          else:
                              users_data.delete_user(user_id)
                              print("User deleted successfully!!")
                              time.sleep(1)
                              continue
                                  
                                  
                          
                    
                    