# Complete Password Manager Prototype
dummy_accounts = [
    {
        "website_name": "GitHub",
        "website_url": "https://github.com",
        "username": "dev_kamau",
        "password": "P@ssw0rd123!",
        "category": "Other",
        "remarks": "Work repository account"
    },
    {
        "website_name": "Gmail",
        "website_url": "https://google.com",
        "username": "wanjiku.m@gmail.com",
        "password": "MySecretEmail#99",
        "category": "Email",
        "remarks": "Primary personal email"
    },
    {
        "website_name": "Safaricom Portal",
        "website_url": "https://safaricom.co.ke",
        "username": "0712345678",
        "password": "SafPass2026$",
        "category": "Utilities",
        "remarks": "Fiber internet billing"
    },
    {
        "website_name": "KRA iTax",
        "website_url": "https://kra.go.ke",
        "username": "A001234567Z",
        "password": "TaxPortal#2026",
        "category": "Email",
        "remarks": "Annual tax returns portal"
    },
    {
        "website_name": "LinkedIn",
        "website_url": "https://linkedin.com",
        "username": "brian.otieno@outlook.com",
        "password": "NetWork@2026!",
        "category": "Social",
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
    # account_category = validate_input_str("Account Category")
    categories = ["Social Media", "Education", "Entertainment", "Other"]
    print("Available Categories")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    category_option = int(input('Choose account category (1-4): ')) 
    if category_option <=0 or category_option > len(categories):
        print(f"Please enter a value more than 1 and less than {len(categories)}")
        return
    account_category = categories[category_option - 1]
    remarks = validate_input_str("Remarks")
    
    user_account_data = {"website_name": website_name, "website_url": website_url, "username": username, "password": demo_password, "category": account_category, "remark": remarks}
    print(user_account_data)
    # TODO : Append the dict to the list
    # TODO : Store the list in a file
# add_account()

# FEATURE 3 - View all Accounts
def view_accounts():
    print("======VIEW ALL ACCOUNTS======")
    # TODO - Load data from storage
    if not dummy_accounts:
        print("Account Details does not exists")
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
# Update_single_field function
def update_single_field(field_name, account, name):
    updated_website_name = validate_input_str(f"Updated {name}")
    decide = input(f"Are you sure you want to update {name}?(Y/N): ").lower().strip()
    if decide in ("y", "yes"):
        # Modify
        account[field_name] = updated_website_name
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
        if account_id < 0:
            print("Account ID cannot be less than 1")
            return None
        if account_id > len(dummy_accounts):
            print("Account ID does not exists")
            return None
        account =dummy_accounts[account_id - 1]
        
        # b. Display the account details to be updated
        print(
            f"Website Name: {account['website_name']}\n"
            f"Website URL: {account['website_url']}\n"
            f"Username: {account['username']}\n"
            f"Username: {account['category']}\n"
            f"Remarks: {account['remarks']}\n"
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
            update_single_field(field_name="website_name", account=account, name="Website Name")
        elif update_option == 2:
            update_single_field(field_name="website_url", account=account, name="Website URL")
        elif update_option == 3:
            update_single_field(field_name="username", account=account, name="Username")
        elif update_option == 4:
            update_single_field(field_name="password", account=account, name="Demo Password")
        elif update_option == 5:
            update_single_field(field_name="remarks", account=account, name="Remarks")
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
        if account_id > len(dummy_accounts):
            print("Account doest not exists")
            return
        account = dummy_accounts[account_id - 1]
        
        # Display the account to be deleted
        print(
            f"Website Name: {account['website_name']}\n"
            f"Website URL: {account['website_url']}\n"
            f"Username: {account['username']}\n"
            f"Username: {account['category']}\n"
            f"Remarks: {account['remarks']}\n"
        )
        decide = input("Are you sure you want to delete this record?(Y/N)").lower().strip()
        if decide in ("y", "yes"):
            dummy_accounts.pop(account_id -1)
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
    found = False
    for x in dummy_accounts:
        value = x["username"]
        if value.lower() == username.lower():
            print(f"Website Name: {x['website_name']}\nWebsite URL: {x['website_url']}\nUsername: {x['username']}\nRemarks: {x['remarks']}\n")
            found = True
    if not found:
        print("Account with such Username doesnot exists!!")
            
# search_by_username()
# FEATURE -8 ACCOUNT STATISTICS
def account_statistics():
    print("======ACCOUNT STATISTICS======")
    # Handle empty list
    if not dummy_accounts:
        print("Accounts does not exist!!")
        return
    # count the number of appearance of a category
    counts = {}
    for acc in dummy_accounts:
        cat = acc["category"]
        counts[cat] = counts.get(cat, 0) + 1
    print(f"Total Accounts: {len(dummy_accounts)}")
    # Show sorted items using lambda and force others being the last
    sorted_counts = sorted(counts.items(), key=lambda x: x[0] == "Other")
    for category, count in sorted_counts:
        print(f"{category}: {count}")
# account_statistics()

# FEATURE 9 -Search by category
def search_by_category():
    # get available categories
    categories = {}
    for acc in dummy_accounts:
        cat = acc["category"]
        categories[cat] = categories.get(cat, 0)
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
        for x in dummy_accounts:
            value = x["category"]
            if list_category[category_option - 1] == value:
                print(
                    f"Website Name: {x['website_name']}\n"
                    f"Website URL: {x['website_url']}\n"
                    f"Username: {x['username']}\n"
                    f"Username: {x['category']}\n"
                    f"Remarks: {x['remarks']}\n"
                        )
                found = True
        if not found:
            print("No category found")
            return
    except ValueError:
        print(f"Please enter a whole number from 1 to {len(categories)}")
        return
# search_by_category()

# FEATURE 9 - SORT ACCOUNTS
def sort_account():
    pass
    
        
        

    

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
            pass
        elif option == 10:
            pass
            break
        elif option == 11:
            break
# Intialize the program or calling the function
# intial_program()
  