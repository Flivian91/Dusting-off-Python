# While Loops in python
# i = 1
# while i < 7:
#     print(i)
#     i += 1
# else:
#     print("Done")
"""
Coding Challenge
1. Create a variable i with the value 0
2. Write a while loop that runs as long as i is less than 6
3. Inside the loop: increment i by 1
4. If i equals 3, use continue to skip that iteration
5. Print i
"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        print("(3) will be skipped")
        continue
    print(i)
    
    