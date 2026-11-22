import datetime
from storage import load_accounts, save_account, update_account, delete_account_helper
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
        return None
    return user_input
# Basic url check
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
    is_valid = basic_url_check(website_url)
    if not is_valid:
        print("Website URL is invalid")
        return None
    username = validate_input_str("Username")
    #TODO: Make username unique to prevent duplication
    demo_password = validate_input_str("Password")
    # account_category = validate_input_str("Account Category")
    categories = ["Social Media", "Education", "Entertainment", "Other"]
    print("Available Categories")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    try:
        category_option = int(input('Choose account category (1-4): ')) 
        if category_option <=0 or category_option > len(categories):
            print(f"Please enter a value more than 1 and less than {len(categories)}")
            return
        account_category = categories[category_option - 1]
        remarks = validate_input_str("Remarks")
        
        user_account_data = {"website_name": website_name, "website_url": website_url, "username": username, "password": demo_password, "category": account_category, "remark": remarks}
        save_account(user_account_data)
    except ValueError:
        print(f"Please enter a whole number from 1 to {len(categories)}")
# add_account()

# FEATURE 3 - View all Accounts
def view_accounts():
    print("======VIEW ALL ACCOUNTS======")
    # Load data 
    accounts = load_accounts()
    if not accounts:
        print("No account available!!")
        return 
    print(f"No\t Website Name\tWebsite URL\tUsername\tRemarks")
    for index, account in enumerate(accounts, start=1):
        print(f"{index}. {account['website_name']}\t{account['website_url']}\t{account['username']}\t{account['remark']}")
    
# view_accounts()

# FEATURE - 4 Search by Website name
def search_by_website():
    print("======SEARCH BY WEBSITE NAME======")
    website_name = validate_input_str("Website Name")
    # Load accounts
    accounts = load_accounts()
    found = False
    for x in accounts:
        value = x['website_name']
        if value.lower() == website_name.lower():
            print(f"Website Name: {x['website_name']}\nWebsite URL: {x['website_url']}\nUsername: {x['username']}\nRemarks: {x['remark']}\n")
            found = True
    if not found:
        print("Account with such website name doesnot exists!!")
    
# search_by_website()

#FEATURE - 5 UPDATE AN ACCOUNT
# Update_single_field function
def update_single_field(field_name, name, id):
    updated_value = validate_input_str(f"Updated {name}")
    decide = input(f"Are you sure you want to update {name}?(Y/N): ").lower().strip()
    if decide in ("y", "yes"):
        # Modify
        # account[field_name] = updated_value
        update_account(field_name, updated_value, id)
        print(f"{name} updated successfully")
    elif decide in ("n", "no"):
        print("Update Cancled!!")
    else:
        print("Please enter Y or N")    
def update_account_data():
    print("======UPDATE AN ACCOUNT DETAILS======")
    try:
        # a. Get the user account ID
        account_id = int(input("Enter account ID to be updated: "))
        if account_id <= 0:
            print("Account ID cannot be less than 1")
            return None
        # load account data
        accounts = load_accounts()
        if account_id > len(accounts):
            print("Account ID does not exists")
            return None
        account =accounts[account_id - 1]
        
        # b. Display the account details to be updated
        print(
            f"Website Name: {account['website_name']}\n"
            f"Website URL: {account['website_url']}\n"
            f"Username: {account['username']}\n"
            f"Category: {account['category']}\n"
            f"Remarks: {account['remark']}\n"
        )
        # c. Provide selection menu for what to update
        print("Update Menu")
        for i, key in enumerate(account.keys(), start=1):
            print(f"{i}. {key.capitalize()}")
        update_option = int(input("Choose a field to update: "))
        if update_option <=0 or update_option > len(account.keys()):
            print(f"Select update option form 1 to {len(account.keys())}")
            return None
        # d. Selection block and its logic
        if update_option == 1:
            update_single_field(field_name="website_name",  name="Website Name", id=account_id-1)
        elif update_option == 2:
            update_single_field(field_name="website_url",  name="Website URL", id=account_id-1)
        elif update_option == 3:
            update_single_field(field_name="username",  name="Username", id=account_id-1)
        elif update_option == 4:
            update_single_field(field_name="password",  name="Demo Password", id=account_id-1)
        elif update_option == 5:
            update_single_field(field_name="category",  name="Category", id=account_id-1)
        elif update_option == 6:
            update_single_field(field_name="remark",  name="Remark", id=account_id-1)
    except ValueError:
        print("Please enter a whole number as account ID")
        return None
    
# update_account_data()

# FEATURE - 6 DELETE AN ACCOUNT
def delete_account():
    print("======DELETE AN ACCOUNT======")
    try:
        account_id = int(input("Enter account ID to be deleted: "))
        if account_id <= 0:
            print("Account ID cannot be less than 1")
            return
        accounts = load_accounts()
        if account_id > len(accounts):
            print("Account doest not exists")
            return
        account = accounts[account_id - 1]
        
        # Display the account to be deleted
        print(
            f"Website Name: {account['website_name']}\n"
            f"Website URL: {account['website_url']}\n"
            f"Username: {account['username']}\n"
            f"Category: {account['category']}\n"
            f"Remarks: {account['remark']}\n"
        )
        decide = input("Are you sure you want to delete this record?(Y/N)").lower().strip()
        if decide in ("y", "yes"):
            delete_account_helper(account_id)
            print("Account deleted successfully")
        elif decide in ("n", "no"):
            print("Deletion Cancled!!")
        else:
            print("Please enter Y or N")
    except ValueError:
        print("Please enter a whole number as ID number")
        return
# delete_account()

# FEATURE -7 SEARCH BY USERNAME
def search_by_username():
    print("======SEARCH ACCOUNT BY USERNAME======")
    username = validate_input_str("Username")
    accounts = load_accounts()
    found = False
    for x in accounts:
        value = x["username"]
        if value.lower() == username.lower():
            print(f"Website Name: {x['website_name']}\nWebsite URL: {x['website_url']}\nUsername: {x['username']}\nRemarks: {x['remark']}\n")
            found = True
    if not found:
        print("Account with such Username doesnot exists!!")
            
# search_by_username()
# FEATURE -8 ACCOUNT STATISTICS
def account_statistics():
    print("======ACCOUNT STATISTICS======")
    # Load data
    accounts = load_accounts()
    # Handle empty list
    if not accounts:
        print("Accounts does not exist!!")
        return
    # count the number of appearance of a category
    counts = {}
    for acc in accounts:
        cat = acc["category"]
        counts[cat] = counts.get(cat, 0) + 1
    print(f"Total Accounts: {len(accounts)}")
    # Show sorted items using lambda and force others being the last
    sorted_counts = sorted(counts.items(), key=lambda x: x[0] == "Other")
    for category, count in sorted_counts:
        print(f"{category}: {count}")
# account_statistics()

# FEATURE 9 -Search by category
def search_by_category():
    # get available categories
    accounts = load_accounts()
    categories = {}
    for acc in accounts:
        cat = acc["category"]
        categories[cat] = categories.get(cat, 0) + 1
    print('All categories include')
    for index, x in enumerate(categories.keys(), start=1):
        print(f"{index}. {x}")
    try:
        category_option = int(input("Choose a category: "))
        if category_option <= 0 or category_option > len(categories):
            print(f"Please enter a value from 1 to {len(categories)}")
            return
        found = False
        list_category = list(categories)
        for x in accounts:
            value = x["category"]
            if list_category[category_option - 1] == value:
                print(
                    f"Website Name: {x['website_name']}\n"
                    f"Website URL: {x['website_url']}\n"
                    f"Username: {x['username']}\n"
                    f"Username: {x['category']}\n"
                    f"Remarks: {x['remark']}\n"
                        )
                found = True
        if not found:
            print("No category found")
            return
    except ValueError:
        print(f"Please enter a whole number from 1 to {len(categories)}")
        return
# search_by_category()

# FEATURE 10 - SORT ACCOUNTS
# Sort order logic
def sort_order_fun(field_name):
    sort_orders = ["Ascending", "Descending"]
    for i, item in enumerate(sort_orders, start=1):
        print(f"{i}. {item}")
    sort_order_option = int(input("Choose sort order: "))
    if sort_order_option <= 0 or sort_order_option > len(sort_orders):
        print("Please enter 1 or 2")
    # Load data
    accounts = load_accounts()
    if sort_order_option == 1:
        sorted_accounts = sorted(accounts, key=lambda x: x[field_name])
    else:
        sorted_accounts = sorted(accounts, key=lambda x: x[field_name], reverse=True)
    return sorted_accounts
def sort_account():
    # Sort options
    sort_menu_items = ["Website", "Username", "Category"]
    for index, item in enumerate(sort_menu_items, start=1):
        print(f"{index}. Alphabetically by {item}")
    try:
        sort_option = int(input("Choose a sort option: "))
        if sort_option <= 0 or sort_option > len(sort_menu_items):
            print(f"Please enter a value form 0 to {len(sort_menu_items)}")
            return
        # Sort by Website name
        if sort_option == 1:
           sorted_accounts = sort_order_fun("website_name")
        elif sort_option == 2:
            sorted_accounts = sort_order_fun("username")
        elif sort_option == 3:
            sorted_accounts = sort_order_fun("category")
        print(sorted_accounts)
    except ValueError:
        print(f"Please enter a whole number form 0 to {len(sort_menu_items)}")
        return
# sort_account()

# FEATURE 11: Export account report
def export_account_report():
    print("=======Account Report======")
    # Load data
    accounts = load_accounts()
    filename = validate_input_str("File name")
    x = datetime.datetime.now()
    try: 
        with open(filename +".txt", "x") as f:
            f.write(f"Account report created at: {x} \n")
            f.write(f"Total number of accounts: {len(accounts)}\n")
            for index, account in enumerate(accounts, start=1):
                f.write(f"{index}\t|{account['website_name']}\t|{account['username']}\t|{account['category']}\n")
            print("Report created successfully")
    except FileExistsError:
        print("File already exists, change file name")
        return
# export_account_report()
# Selection Block
def intial_program():
    while True:
        option = main_menu()
        if option == 1:
            add_account()
        elif option == 2:
            view_accounts()
        elif option == 3:
            search_by_website()
        elif option == 4:
            update_account_data()
        elif option == 5:
            delete_account()
        elif option == 6:
            search_by_username()
        elif option == 7:
            account_statistics()
        elif option == 8:
            search_by_category()
        elif option == 9:
            sort_account()
        elif option == 10:
            export_account_report()
        elif option == 11:
            break
# Intialize the program or calling the function
intial_program()  