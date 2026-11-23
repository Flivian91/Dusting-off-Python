import datetime

x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%y/%m/%d"))
y = datetime.datetime(2020, 6, 3)
# print(y.strftime("%p"))
def common_word_checker(text):
    counts = {}
    best = ""
    for word in text.lower().strip():
        if len(text) < 3:
            continue
        counts[word] = counts.get(word, 0) + 1
        if counts[word] > counts.get(best, 0):
            best = word
    return f"Best word: {best} with {counts[best]} counts"
x = common_word_checker("banananaa")
print(x)