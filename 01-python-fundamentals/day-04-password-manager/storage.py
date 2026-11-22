import json
# READ-WRITE-MODIFY pattern
filename = "accounts.json"
# Load accounts
def load_accounts():
    try:
        with open(filename, "rt") as file:
            accounts = json.load(file)
            if not isinstance(accounts, list):
                raise ValueError("Accounts must be a list")
            return accounts
    except ValueError:
        print("Accounts must be a list")
        return
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('Error Account data is corrupted')
        return None
# Save accounts
def save_account(data):
    # load data
    accounts = load_accounts()
    # add new data
    accounts.append(data)
    # write the data in json file
    with open(filename, "w") as f:
        json.dump(accounts, f, indent=4)
    print("Account added successfuly")
    
    