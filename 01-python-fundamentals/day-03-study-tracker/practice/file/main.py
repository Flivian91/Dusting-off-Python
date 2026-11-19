# f = open("demofile.txt", "rt")
# print(f.read())
# f.close()

# Using the with statement
# with open("demofile.txt", "rt") as f:
#     # print(f.read())
#     print(f.readline())
#     print(f.readline())

# Looping through the file
# with open('demofile.txt', 'rt') as f:
#     for x in f:
#         print(x)

# Append a file
# with open("demofile.txt", 'w') as f:
#     f.write("\nI love flivian")
    
# # open and read the file
# with open("demofile.txt", "rt") as f:
#     print(f.read())

# Creating new file
try:
    f = open("demofiles.txt", "x")
    print("file created successfully!")
except FileExistsError:
    print("File cannot be created since it exists")