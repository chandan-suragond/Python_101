# Count the character frequency in given string

input_str = "aabccddefff"
# output: a2b1c2d2e1f3

def using_dict(input_str):
    d = dict()
    for i in input_str:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for k, v in d.items():
        print(f"{k}{v}", end='')

using_dict(input_str)

# li = list(input_str)

# new_li = []
# counter = 1
# for i in range(1,len(li)):
#     if li[i] == li[i-1]:
#         counter+=1
#     else:
#         new_li.append(li[i-1])
#         new_li.append(str(counter))
#         counter = 1
# new_li.append(li[i-1])
# new_li.append(str(counter))
# print(''.join(new_li))