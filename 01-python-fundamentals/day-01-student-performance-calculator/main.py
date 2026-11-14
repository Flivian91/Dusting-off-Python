# Student Perfomance calculator
student_name = input("Enter student`s name:")
if student_name == "":
    print("Student name cannot be null")
    exit()
# Function to perfom validation of all the subjects
def get_marks(subject):
    try:
        mark = int(input(f"Enter {subject} marks: "))
        if mark < 0 or mark > 100 :
            print(f"invalid {subject} marks")
            return None
        return mark
    except ValueError:
        print(f"Invalid input for {subject}. Please enter a whole number")
        return None

# Calling function and 
eng = get_marks("English")
comp = get_marks("Computer")
math = get_marks("Mathematics")
bio = get_marks("Biology")
chem = get_marks("Chemistry")

# list
marks = [eng, comp, math, bio, chem]

# Calculate total marks
if None not in marks:
    
    total_marks = sum(marks)
    # Calculate average
    average_marks = (total_marks/len(marks))
    highest_mark = max(marks)
    lowest_mark = min(marks)
    print("=======Report========")
    print(f"Total marks: {total_marks}")
    print(f"Average Mark: {average_marks:.2f}")
    print(f"Highest Mark: {highest_mark}")
    print(f"Lowest Mark: {lowest_mark}")
          

    # Grade determiner logic
    # Grade range 0-39 E,40-49 D,50-59 C,60-69 B,70-100 A
    if average_marks >= 70:
        print(f" Grade: A")
    elif average_marks >= 60:
        print(f" Grade: B")
    elif average_marks >= 50 :
        print(f" Grade: C")
    elif average_marks >=40:
        print(f" Grade: D")
    else:
        print(f" Grade: E")
else:
    print("Invalid Marks")
    
