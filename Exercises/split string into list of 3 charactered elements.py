# split string into list of 3 charactered elements

s = "geeksforgeeks"

# ['gee','ksf','org','eek','s']

def split_string(s,n):
    li = list(s)
    new_li = [''.join(li[i:i+n]) for i in range(0,len(li), n)]

    # li = list()
    # for i in range(0,len(s),n):
    #     li.append(s[i:i+n])
    # return li

    return new_li

print(split_string(s,3))