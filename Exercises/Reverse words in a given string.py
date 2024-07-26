# Reverse words in a given String in Python
str ="chandan loves nivedita"
print(f"Actual line : {str}")
# solution - 1

words = str.split()
print("After usage of split : ",words)

new_lst = list(map(lambda x: x[::-1],words))
print(' '.join(new_lst))

reversed_str = ''

for i in range(len(words)-1,-1,-1):
    if i == len(words)-1 :
        reversed_str = words[i] 
    else:
        reversed_str = reversed_str + ' '+ words[i] 
print(f"Reversed line : {reversed_str}")

# solution - 2

# words = str.split()[::-1]
# print(' '.join(words))