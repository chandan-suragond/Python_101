# Count the character frequency in given string

input_str = "aabccddefff"
# output: a2b1c2d2e1f3


li = list(input_str)

new_li = []
counter = 1
for i in range(1,len(li)):
    if li[i] == li[i-1]:
        counter+=1
    else:
        new_li.append(li[i-1])
        new_li.append(str(counter))
        counter = 1
new_li.append(li[i-1])
new_li.append(str(counter))
print(''.join(new_li))