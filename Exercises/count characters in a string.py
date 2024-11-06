# count characters in a string

str = "abcdabdcecda dcab"

def char_counts_func(s):
    char_count = {}

    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    print(char_count)
    max_char = max(char_count, key=char_count.get)

    return max_char

print(char_counts_func(str))