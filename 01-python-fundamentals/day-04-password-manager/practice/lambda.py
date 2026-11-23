# Lambda function is a small, anonymous(unnamed) function that is defined using the lambda keyword
# lambda arguments:expression
# use cases
# 01. adding 10 to a number
# add_ten = lambda x: x + 10
# print(add_ten(5))
# 02. Custom sorting with sort()
# pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (9, "nine")]
# sort_menu_items = ["Website", "Username", "Category"]
# sorted_pairs = sorted(sort_menu_items, key=lambda x: x[0]) #sorts alphabets in ascending order
# print(sorted_pairs)
# 03. transforming a Map() function
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)
# 04. Filtering items using the filter() function
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
# print(even_numbers)

# Word checker
# def common_word_checker(text):
#     counts = {}
#     best = ""
#     for word in text.lower().strip():
#         if len(text) < 3:
#             continue
#         counts[word] = counts.get(word, 0) + 1
#         if counts[word] > counts.get(best, 0):
#             best = word
#     print(best)
#     print(counts)
# common_word_checker("ese")