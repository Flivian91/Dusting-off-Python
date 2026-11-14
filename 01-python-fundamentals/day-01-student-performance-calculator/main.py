# Student Perfomance calculator
student_name = input("Enter student`s name:")
# subjects: eng, comp, math, bio, chem
# Function to perfom validation of all the subjects
def get_marks(subject):
    try:
        mark = int(input(f"Enter {subject} marks: "))
        if mark < 0 or mark > 100 :
            print(f"invalid {subject} marks")
            return None
        return mark
    except ValueError:
        print("Please enter a valid number")
        return None

# Calling function
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

    # Grade determiner logic
    # Grade range 0-39 E,40-49 D,50-59 C,60-69 B,70-100 A
    if average_marks >= 70:
        print(f"{student_name} scored a total of {total_marks} and the average is {average_marks:.2f} A")
    elif average_marks >= 60:
        print(f"{student_name} scored a total of {total_marks} and the average is {average_marks:.2f} B")
    elif average_marks >= 50 :
        print(f"{student_name} scored a total of {total_marks} and the average is {average_marks:.2f} C")
    elif average_marks >=40:
        print(f"{student_name} scored a total of {total_marks} and the average is {average_marks:.2f} D")
    elif average_marks >=0 and average_marks <= 39 :
        print(f"{student_name} scored a total of {total_marks} and the average is {average_marks:.2f} E")
    else:
        print("Invalid marks")
else:
    print("Invalid Marks")
    
