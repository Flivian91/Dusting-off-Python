# Complete Password Manager Prototype

# FEATURE 1 - Main Menu
def main_menu():
    print("======WELCOME TO PASSWORD MANAGER PROTOTYPE======")
    menu_items = ["Add Account", "View All Accounts", "Search Account", "Update Account", "Delete Account", "Search by Username", "View Account Statistics", "Search by Website Category", "Sort Account", "Export Account Report", "Exit"]
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item}")
    try:
        menu_option_input = int(input("Choose a option: "))
        if menu_option_input <= 0 or menu_option_input > len(menu_items):
            print(f"Please enter a menu option from 1 to {len(menu_items)}")
            return 
        return menu_option_input
    except ValueError:
        print(f"Please enter a whole number from 0 to {len(menu_items)}")
        return None

# FEATURE 2 -Add a new account
# Input validation
def validate_input_str(input_name):
    user_input = input(f"Enter {input_name}: ").strip()
    if not user_input.strip():
        print(f"Please {input_name} cannot be empty!!")
        return
    return user_input
def basic_url_check(url):
    # 1. Check that it starts with http:// or https://
    has_protocol = url.startswith(("http://", "https://"))
    # 2. Check that there is a dot for the domain (e.g., .com) and no spaces
    has_dot = "." in url
    no_spaces = " " not in url
    return has_protocol and has_dot and no_spaces

#  add account inplementation
def add_account():
    website_name = validate_input_str("Website Name")
    website_url = validate_input_str("Website URL(eg 'https://www.mywebsite.com')")
    # basic url check using lambda function
    is_valid = basic_url_check(website_url)
    if not is_valid:
        print("Website URL is invalid")
        return None
    username = validate_input_str("Username")
    #TODO: Make username unique to prevent duplication
    demo_password = validate_input_str("Password")
    account_category = validate_input_str("Account Category")
    remarks = validate_input_str("Remarks")
    
    user_account_data = {"website_name": website_name, "website_url": website_url, "username": username, "password": demo_password, "account_category": account_category, "remark": remarks}
    # TODO : Append the dict to the list
    # TODO : Store the list in a file

    
# Selection Block
def intial_program():
    while True:
        option = main_menu()
        if option == 1:
            add_account()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        elif option == 10:
            pass
            break
        elif option == 11:
            break
# Intialize the program or calling the function
intial_program()
  