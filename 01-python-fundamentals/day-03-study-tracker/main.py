# Personal Study tracker -helps to manage the study sessions
import json
# constants
filename = "study_sessions.json"
# 1. Main Menu
def main_menu():
    print("======PERSONAL STUDY SESSION TRACKER======")
    menu_items = ["Add study session", "view all sessions", "Search by subject", "View total study time", "Exit"]
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item}")
    try:
        menu_option = int(input("Choose an option: "))
        if menu_option < 0 or menu_option > 5:
            print("Please enter a number from 1 to 5")
            return None
        return menu_option
    except ValueError:
        print("Please enter a whole number from 1 to 5")
        return
    
# option = main_menu()

# 2. Add a study section
def add_study():
    print("======ADD STUDY SESSION======")
    subject_name = input("Enter subject name: ").strip()
    if not subject_name.strip():
        print("Please subject name cannot be empty!!")
        return
    topic_studied = input("Enter topic studied: ").strip()
    if not topic_studied.strip():
        print("Please topic studied cannot be empty!!")
        return
    try:
         duration = int(input("Enter duration in minutes: "))
         if duration < 0 or duration == 0 :
             print("Please duration cannot be negative or equal to 0")
             return
    except ValueError:
        print("Please enter a whole number on duration")
        return
    user_data = {"subject": subject_name, "topic": topic_studied, "duration": duration}
    # Calling the save data fuction
    save_study_session(user_data)
    print("Study session saved successfully!")


# SAVE FILE DATA using(Read-Modify-Write pattern)
def save_study_session(data):
    # Read study data
    study_data = load_study_sessions()
    # modify the study data 
    study_data.append(data)
    # Write the updated data
    with open(filename, "w") as file:
        json.dump(study_data, file, indent=4)
# LOAD SAVED DATA function
def load_study_sessions():
    try:
        with open(filename, "rt") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Study data must be a list")
            return data
    except FileNotFoundError:
        # Start with an empty list, when file does not exists
        return []
    except json.JSONDecodeError:
        print("Error: Study file is corrupted.")
        return None
        
# add_study()
# 3. View all sessions
def view_sessions():
    print("======VIEW ALL SESSIONS======")
    # load the data 
    session_data = load_study_sessions()
    # Check if there is data in the file
    if not session_data:
        print("No study record recorded yet!!")
        return None
    
    # loop through the data 
    for index, data in enumerate(session_data, start=1):
        print(f"{index} | {data['subject']}\t| {data['topic']}\t| {data['duration']} minutes")
# view_sessions()

# 4. Search by subject
def search_sessions():
    print("======SEARCH BY SUBJECT NAME======")
    subject_name = input("Enter subject name: ").strip()
    if not subject_name.strip():
        print("Please subject name cannot be empty!!")
        return
    # Load data
    session_data = load_study_sessions()
    found = False
    for x in session_data:
        value = x["subject"]
        if subject_name.lower() == value.lower():
            print(f"Subject: {x['subject']} \nTopic: {x['topic']} \nDuration: {x['duration']} minutes")
            found = True
    if not found:
        print("Ooops!! the subject is not available.")
# search_sessions()

# 5. calculate the total study time
def total_study_time():
    print("======TOTAL STUDY TIME======")
    # Load data
    session_data = load_study_sessions()
    times = []
    for x in session_data:
        times.append(x["duration"])
    total_minutes = sum(times)
    hours, minutes =  divmod(total_minutes, 60)
    # print(f"Total Time: {str(hours) + " Hours and " if hours else ""}{minutes} minutes")
    if hours:
        print(f"Total time: {hours} hours and {minutes} minutes")
    else:
        print(f"Total time: {minutes} minutes")
# total_study_time()

while True:
    option = main_menu()
    if option == 1:
        add_study()
    elif option == 2:
        view_sessions()
    elif option == 3:
        search_sessions()
    elif option == 4:
        total_study_time()
    elif option == 5:
        break
    