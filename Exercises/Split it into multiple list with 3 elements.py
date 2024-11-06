# Split it into multiple list with 3 elements
input_list = ['a','b','c','d','e','f','g'] 

def split_list(li, n):
    new_li = [li[i : i+n] for i in range(0, len(li), n)]
    print(new_li)

split_list(input_list, 3)
