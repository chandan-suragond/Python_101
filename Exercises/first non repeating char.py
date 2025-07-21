from collections import Counter

s = 'swiss'

def first_non_repeating_char(s):
    li = list(s)
    di = {}
    for i in li:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    for k, v in di.items():
        if v == 1:
            return k
    return None

def first_non_repeating_char_Counter(s):
    freq = dict(Counter(s))
    for k, v in freq.items():
        if v == 1:
            return k
    return None


print(first_non_repeating_char(s))
print(first_non_repeating_char_Counter(s))