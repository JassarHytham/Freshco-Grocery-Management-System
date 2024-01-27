#student name: GassarHaithm Saleh Ba Hashwan
#TP No.(TP068741) 



#this will be the log ing type if you are an admin or a customer.



def login(username, password, log_in_as):
    login_file = ""
    #I have devided log_in_as into to part to define the person if he was a user or an admin
    if log_in_as == 'user': 
        try:
            login_file = open('user.txt')
        except:
            print("No such a file")
    elif log_in_as == 'admin': 
        #to login as admin these are the details
        #userame:admin
        #password:admin
        try:
            login_file = open('admin.txt')
        except:
            print("No such a file")

    file = login_file.readlines()
    login_file.close()


#this side of the program is to seperate the username and the password from each other
#and to cheak if the username and password the same as in the files
    status=True
    for userData in file:
        #I used here split function to get the username and the password from the list
        user = userData.split(',')[0]
        pwd = userData.split(',')[1].strip()
        if (user == username) and (pwd == password):
            return True
        else:
            status=False
    if status==False:
        print("Username or Password is wrong")
    login_file.close()
#note: the admin account will be made by the programmer, all the infomation for the admin account can be foun in "admin.txt" file.


#this function will creat a new account for new users.
def new_account(username,password,gender,date_of_birth,Email,phone_number,address):
    data=username+","+password+","+gender+","+date_of_birth+","+Email+","+phone_number+","+address+"\n"
    login_file=open("user.txt","a")
    login_file.write(data) #all the information for the user will be saved into user.txt file.
    login_file.close()
    return True


#this function is for the available groceries and we can add things to it later
def groceries_file():
    groceries=[] #I have declare groceries  as a lsit to save into it

    groceries_file=open("groceries.txt")
    for available in groceries_file.readline():
        available=available.split(",")
        groceries[available[0]]=int(available[1])
        groceries_file.close()
        return groceries


#this function is to let the user check his information
def information_file(username): #useing a paremeter here so the user can see his own infomation
    with open("user.txt","r")as info:
        for i in info.readlines():
            i=i.split(",")
            if (username==i[0]):#if the paremeter is the same in the list then all the information will be printed
                customer_information=[]
                count=0
                while count<len(i):
                    customer_information.append(i[count])
                    count=count+1
        print(f'your useaname is:{customer_information[0]}')
        print(f'your password is:{customer_information[1]}')
        print(f'your gender is:{customer_information[2]}')
        print(f'your birthday is:{customer_information[3]}')
        print(f'your Email is:{customer_information[4]}')
        print(f'your phone number is:{customer_information[5]}')
        print(f'your address is:{customer_information[6]}')


#this function is to add products wich will be used by the admin only.
def append_groceries(groceries_name,price):#groceries_name,price are inputs to append, can be found in the main function
    read_groceries_file()
    file=open("groceries.txt","a")
    file.write(groceries_name+","+str(price)+"\n")#here to add the name and price of grocery into the file
    print("this product was added successfully")
    file.close



#the admin can modify the products that are available in the grocery store
def modify_groceries():
    read_groceries_file()#this function to show the grocery list
    operation_num=input("enter 1 if you want to change the name\nenter 2 if you want to change the cost:")
    groceries_num=input("enter the grocery number you want to modify:")
    new_file=""
    if operation_num=="1":
        new_name=input("type the new name:")
        count = 1
        modify_groceries=open("groceries.txt","r")
        for i in modify_groceries:
            if str(count) == groceries_num: #im converting count to string because the varible groceries_num is string too.
                price = (i.split(","))[1] #I have declared the price here already because I dont want the price to be changed.
                new_file = new_file + (f'{new_name},{price}')
                count=count+1
                print("The task has been done successfully")
            else:
                new_file = new_file + i
                count=count+1
        over_write=open("groceries.txt","w")
        over_write.write(new_file)#im using .write function to overwrite the new changes.
        over_write.close()
        modify_groceries.close()
    elif operation_num=="2":
        status = 0
        while status == 0:
            try:#the new price should be only integer, thats why im using (try)
                new_price=float(input("type the new price:"))
                status = 1 #I have declared status as 1 to get out  of the loop
            except:
                print("invalid price")
        count = 1
        modify_groceries=open("groceries.txt","r")
        for i in modify_groceries:
            if str(count) == groceries_num: #im converting count to string because the varible groceries_num is string too.
                name = (i.split(","))[0]#I have declared the name here already because I dont want the name to be changed.
                new_file = new_file + (f'{name},{new_price}\n')
                count=count+1
                print("The task has been done successfully")
            else:
                new_file = new_file + i
                count=count+1
        over_write=open("groceries.txt","w")
        over_write.write(new_file)#im using .write function to overwrite the new changes.
        over_write.close()
        modify_groceries.close()



#this function is to display all the groceries when the user or admin ask for it.
def read_groceries_file():
    available_groceries = []#i have declared available_groceries as an empty list
    available_groceries_file = open('groceries.txt')
    count=1
    print("\n")
    print(f'product name:\t      cost:')#this print for the design
    for available in available_groceries_file.readlines():
        available = available.split(',')
        print(f'[ {count} ]\t{available[0]}',end='\t\t')#im printing the groceries numbers and its name
        print(f'{available[1]}',end="")#this print for the prices
        count=count+1
    available_groceries_file.close()
    return available_groceries



#this function is to make orders and to make payment.
def order(username):
    repeat=0
    total=0
    all_orders=""
    while repeat==0:
        read_groceries_file()
        groceries_number=input("enter the grocery's number:")#here to choose the grocery number
        product_file=open("groceries.txt","r")
        count=1
        for i in product_file.readlines():
            i=i.split(",")#I used here split to split i to list using (",")
            if str(count)==groceries_number:#im converting count to string because the varible groceries_num is string too.
                all_orders=all_orders+(f'{username},{i[0]},{i[1]}')
                print(f'[your order is:{i[0]}] for [{i[1]}Ringgit] \n')
                total=total+int(i[1])#here im counting the total for the orders
                if input('enter 1 if you want to continue\nenter 2 if you want to proceed to payment:')=="1": #im usnig '' fo the number 1 to avoid any error.
                    break
                else:
                    #in this block the payment will be dine here, the user will be asked to proceed using cash or cancel the order, and the total cost will be displayed.
                    payment=input(f'the total of your orders {total} RM(the payment method is in Cash only)\nDo you want to proceed?\nEnter 1 to proceed\nEnter2 to cancel payment') 
                    if payment=="1":
                        orders_file=open("orders.txt","a")
                        orders_file.write(all_orders)#the orders will be saved into orders.txt file if the user chose to procced
                        return True
                    else:
                        return False #it will be returend false if the customer chose to cancel so nothing will be saved.
            else:
                count=count+1
        product_file.close()   


#this function is to let the coustomer dispolay his own order history
#the premeter here so the customer can see his own orders only.
def View_orders(username):
    total=0
    orders_file=open("orders.txt","r")
    for i in orders_file.readlines():
        i=i.split(",")#I used here split to split i to list using (",")
        if username==i[0]:
            print(f'you orderd [ {i[1]} ] for  RM {i[2]}')
            #here I have calculate the total of the customer order history cost.
            total=total+int(i[2])
    print(f'the total of your orders [ RM {total} ]')
    orders_file.close()


#this function if for the admin to get the orders of a specific customer.
def specific_customer_orders():
    total=0
    customer_name=input("Enter the customer name:")
    orders_file=open("orders.txt","r")
    for i in orders_file.readlines():
        i=i.split(",")#I used here split to split i to list using (",")
        if customer_name==i[0]:
            print(f'the order for {customer_name} [ {i[1]} ] for  RM {i[2]} ')
            #here I have calculate the total of the customer order history cost.
            total=total+int(i[2])
    print(f'the total cost of {customer_name} is [ RM {total} ]')
    orders_file.close()

#this function to let the admin to search for specific grocery.
def specific_grocery():
    grocery_name=input("Enter the grocery name:")
    groceries_file=open("groceries.txt","r")
    for i in groceries_file.readlines():
        i=i.split(",")
        if grocery_name==i[0]:
            print('\t')
            #here the grocery name and its cot will be shown
            print(f'grocery name is:{i[0]}')
            print(f'the grocery cost is:{i[1]}')
    groceries_file.close()


#this function will allow the admin to delete products.
def delete_product():
    repeat=1
    while repeat==1:
        new_file=""
        read_groceries_file()
        groceries_number=input("enter the grocery's number:")
        product_file=open("groceries.txt","r")
        count=1
        status=False
        for i in product_file.readlines():
            if str(count)!=groceries_number:
            #if the the grocery number is equal to the the count, this line will not be saved in (new_file)
                new_file=new_file+i
                count=count+1
            else:
                print("the product was deleted")
                status=True
                count=count+1
        if status==False:
            print("your entry is wrong")
        product_file.close()
        over_write_product=open("groceries.txt","w")
        over_write_product.write(new_file)
        #here everything saved in (new_file) will be overwrite into groceries.txt file.
        over_write_product.close()
        
        if input(f"Enter 1 to continue\n Enter 2 to exit:")=="2":
            return True  

#this fucntion will show all the orders that have been made 
def all_orders():
    all_orders_file=open("orders.txt","r")
    for i in all_orders_file.readlines():
        i=i.split(",")#I used here split to split i to list using (",")
        print(f'the customer {i[0]} ordered {i[1]}')
    all_orders_file.close()

#this function will show the sign in type
def login_type():
    print("""
  __  __          _            ___                     
 |  \/  |  __ _  (_)  _ _     | _ \  __ _   __ _   ___ 
 | |\/| | / _` | | | | ' \    |  _/ / _` | / _` | / -_)
 |_|  |_| \__,_| |_| |_||_|   |_|   \__,_| \__, | \___|
                                           |___/       \n""")
    print("Please enter one number of the next operation you want \n")
    print('''
    Enter 1 to login to an existing account
    Enter 2 to login as an admin
    Enter 3 to continue as a guest
    Enter 4 to exit the store
    ''')
    try:#the input should be only an integer.
        choice=int(input("Enter the number:"))
        return choice
        
    except:
        print("please type numbers only")


#this function is for the guest, where the guest can display all the prodcts, and make a new account.
def guest_menu():
    print("""
   ___             _     ___         _        _ 
  / __|___ _  _ __| |_  | _ \___ _ _| |_ __ _| |
 | (_ / -_) || (_-<  _| |  _/ _ \ '_|  _/ _` | |
  \___\___|\_,_/__/\__| |_| \___/_|  \__\__,_|_|
                                                """)
    print("Please enter one number of the next operation you want")
    print('''
Enter 1 to view Groceries detail
Enter 2 to create an account
Enter 3 to go back to the Main Page
''')
    try:#the input should be only an integer.
        choice=int(input("Enter the number:"))
        return choice
        
    except:
        print("please type numbers only")


#this function for the admin, all the advenced options the admin can do it here
def admin_menu():
    print("""
    _      _       _        ___         _        _ 
   /_\  __| |_ __ (_)_ _   | _ \___ _ _| |_ __ _| |
  / _ \/ _` | '  \| | ' \  |  _/ _ \ '_|  _/ _` | |
 /_/ \_\__,_|_|_|_|_|_||_| |_| \___/_|  \__\__,_|_|
                                                   \n""")
    print("choose one number of the operation you want:")                                              
    print("""
    Enter 1 to upload Groceries detail in system
    Enter 2 to update/modify Groceries 
    Enter 3 to view all uploaded Groceries
    Enter 4 to view all orders of customers
    Enter 5 to search order of specific customer
    Enter 6 to delete Groceries information
    Enter 7 to search a specific grocery
    Enter 8 to go back to the Main Page""")
    try:#the input should be only an integer.
        choice=int(input("Enter the number:"))
        return choice
        
    except:
        print("please type numbers only")



#this function is for the user options 
def customer_menu():
    print("""
   ___               _                                 ___               _            _ 
  / __|  _  _   ___ | |_   ___   _ __    ___   _ _    | _ \  ___   _ _  | |_   __ _  | |
 | (__  | || | (_-< |  _| / _ \ | '  \  / -_) | '_|   |  _/ / _ \ | '_| |  _| / _` | | |
  \___|  \_,_| /__/  \__| \___/ |_|_|_| \___| |_|     |_|   \___/ |_|    \__| \__,_| |_|
                                                                                        """)
    print("""
    Enter 1 to view own order
    Enter 2 to View all Groceries
    Enter 3 to view personal information
    Enter 4 to Place order of Groceries
    Enter 5 to go back to the Main Page""")
    try:#the input should be only an integer.
        choice=int(input("Enter the number:"))
        return choice
        
    except:
        print("please type numbers only")

    

def welcome():
    print("""
 __      __        _                              _             ___   ___   ___   ___   _  _    ___    ___      ___      _            ___   _         _   
 \ \    / /  ___  | |  __   ___   _ __    ___    | |_   ___    | __| | _ \ | __| / __| | || |  / __|  / _ \    / __|  __| |  _ _     | _ ) | |_    __| |  
  \ \/\/ /  / -_) | | / _| / _ \ | '  \  / -_)   |  _| / _ \   | _|  |   / | _|  \__ \ | __ | | (__  | (_) |   \__ \ / _` | | ' \    | _ \ | ' \  / _` |  
   \_/\_/   \___| |_| \__| \___/ |_|_|_| \___| ___\__| \___/   |_|   |_|_\ |___| |___/ |_||_|  \___|  \___/    |___/ \__,_| |_||_|   |___/ |_||_| \__,_|  
                                              / __|  _ _   ___   __   ___   _ _  (_)  ___   ___                                                           
                                             | (_ | | '_| / _ \ / _| / -_) | '_| | | / -_) (_-<                                                           
                                              \___| |_|   \___/ \__| \___| |_|   |_| \___| /__/                                                           
                                                                                                                                                          """)





#this will be the main function where all the previus functions will be excuted.
def main():
    welcome()
    while True:#this function will be none stop until the user asks to break it
        choice=login_type()
        if choice==1:#this choice is for the user
            username=input("Enter your username:")
            password=input("enter your password:")
            if login(username,password,"user"):
                while True:
                    customer_choice=customer_menu()
                    if customer_choice==1:
                        View_orders(username)
                    elif customer_choice==2:
                        read_groceries_file()
                    elif customer_choice==3:
                        information_file(username)
                    elif customer_choice==4:
                        order_status=order(username)
                        if order_status==True:
                            print("payment has been done successfully")
                        else:
                            print("payment has not been done")
                    elif customer_choice==5:
                        break
                    else:
                        print("your entry is wrong")
                        continue
            else:
                continue
        elif choice==2:#this choice is for the admin
            username=input("Enter your username:")
            password=input("enter your password:")
            if login(username,password,"admin"):
                while True:
                    admin_choice=admin_menu()
                    if admin_choice==1:
                        groceries_name=input("enter the grocery name:")
                        price=float(input("enter the price:"))
                        append_groceries(groceries_name,price)
                    elif admin_choice==2:
                        modify_groceries()
                    elif admin_choice==3:
                        read_groceries_file()
                    elif admin_choice==4:
                        all_orders()
                    elif admin_choice==5:
                        specific_customer_orders()
                    elif admin_choice==6:
                        delete_product()
                    elif admin_choice==7:
                        specific_grocery()
                    elif admin_choice==8:
                        break
                    else:
                        print("your entry is wrong")
                        continue
            else:
                continue
        elif choice==3:#this choice is for the guest
            while True:
                geust_choice=guest_menu()
                if geust_choice==1:
                    read_groceries_file()
                elif geust_choice==2:
                    username = input('Enter Username: ')
                    password = input('Enter Password: ')
                    gender=input("Enter your gender:")
                    date_of_birth=input("Enter your date of birth:")
                    Email=input("Enter your Email:")
                    phone_number=input("Enter your Phone number:")
                    address=input("Enter your address:")
                    if new_account(username,password,gender,date_of_birth,Email,phone_number,address):
                            print('Account Created')
                elif geust_choice==3:
                    break
                else:
                    print("your entry is wrong")
                    continue

        elif choice==4:#this choice to exit the program
            break

        else:#anything ealse will display that
            print("your entry is wrong")
            continue



main()
                
                        

