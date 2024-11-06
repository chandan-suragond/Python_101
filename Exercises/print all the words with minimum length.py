a="Chandan Suragond is an engineer"
# print all the words with minimum length

words_li = a.split()

minimum_length = min(len(word) for word in words_li)

min_words = [word for word in words_li if len(word) == minimum_length]

print(min_words)

