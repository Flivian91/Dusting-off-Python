# Complete Password Manager Prototype
dummy_accounts = [
    {
        "website_name": "GitHub",
        "website_url": "https://github.com",
        "username": "dev_kamau",
        "password": "P@ssw0rd123!",
        "remarks": "Work repository account"
    },
    {
        "website_name": "GitHub",
        "website_url": "https://github.com",
        "username": "dev_kamau",
        "password": "P@ssw0rd123!",
        "remarks": "Work repository account"
    },
    {
        "website_name": "Gmail",
        "website_url": "https://google.com",
        "username": "wanjiku.m",
        "password": "MySecretEmail#99",
        "remarks": "Primary personal email"
    },
    {
        "website_name": "Saf Portal",
        "website_url": "https://safaricom.co.ke",
        "username": "0712345678",
        "password": "SafPass2026$",
        "remarks": "Fiber internet billing"
    },
    {
        "website_name": "KRA iTax",
        "website_url": "https://kra.go.ke",
        "username": "A001234567Z",
        "password": "TaxPortal#2026",
        "remarks": "Annual tax returns portal"
    },
    {
        "website_name": "LinkedIn",
        "website_url": "https://linkedin.com",
        "username": "brian.otieno@outlook.com",
        "password": "NetWork@2026!",
        "remarks": "Professional networking profile"
    }
]

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
    print("======ADD A NEW ACCOUNT======")
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


# FEATURE 3 - View all Accounts
def view_accounts():
    print("======VIEW ALL ACCOUNTS======")
    # TODO - Load data from storage
    if not dummy_accounts:
        print("No Account available right now")
        return None
    print(f"No Website Name\tWebsite URL\tUsername\tRemarks")
    for index, account in enumerate(dummy_accounts, start=1):
        print(f"{index}. {account['website_name']}\t{account['website_url']}\t{account['username']}\t{account['remarks']}")
    
# view_accounts()

# FEATURE - 4 Search by Website name
def search_by_website():
    print("======SEARCH BY WEBSITE NAME======")
    website_name = validate_input_str("Website Name")
    found = False
    for x in dummy_accounts:
        value = x['website_name']
        if value.lower() == website_name.lower():
            print(f"Website Name: {x['website_name']}\nWebsite URL: {x['website_url']}\nUsername: {x['username']}\nRemarks: {x['remarks']}\n")
            found = True
    if not found:
        print("Account with such website name doesnot exists!!")
    
# search_by_website()

#FEATURE - 5 UPDATE AN ACCOUNT
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
# intial_program()
  