# Student Perfomance calculator
studentName = input("Enter student`s name:")
# subjects: eng, comp, math, bio, chem
eng = int(input("Enter English Marks:"))
comp = int(input("Enter Computer Studies Marks:"))
math = int(input("Enter Mathematics Marks:"))
bio = int(input("Enter Biology Marks:"))
chem = int(input("Enter Chemistry Marks:"))

# Calculate total marks
totalmarks = eng + comp + math + bio + chem
# Calculate average
averageMarks = (totalmarks/5)
# Grade determiner logic
# Grade range 0-39 E,40-49 D,50-59 C,60-69 B,70-100 A
if averageMarks >= 70 and averageMarks <= 100:
    print(f"{studentName} scored {averageMarks} A")
elif averageMarks >= 60 and averageMarks <= 69 :
    print(f"{studentName} scored {averageMarks} B")
elif averageMarks >= 50 and averageMarks <= 59 :
    print(f"{studentName} scored {averageMarks} C")
elif averageMarks >=40 and averageMarks <= 49 :
    print(f"{studentName} scored {averageMarks} D")
elif averageMarks >=0 and averageMarks <= 39 :
    print(f"{studentName} scored {averageMarks} C")
else:
    print("Invalid marks")