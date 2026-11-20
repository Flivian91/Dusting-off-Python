# Complete Password Manager Prototype

# FEATURE 1: Main Menu
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
        # Selection block
        while True:
            if menu_option_input == 1:
                print(menu_items[0])
            elif menu_option_input == 2:
                print(menu_items[1])
            elif menu_option_input == 3:
                print(menu_items[2])
            elif menu_option_input == 4:
                print(menu_items[3])
            elif menu_option_input == 5:
                print(menu_items[4])
            elif menu_option_input == 6:
                print(menu_items[5])
            elif menu_option_input == 7:
                print(menu_items[6])
            elif menu_option_input == 8:
                print(menu_items[7])
            elif menu_option_input == 9:
                print(menu_items[8])
            elif menu_option_input == 10:
                print(menu_items[9])
                break
            elif menu_option_input == 11:
                break
    except ValueError:
        print(f"Please enter a whole number from 0 to {len(menu_items)}")
        return None
# main_menu()
