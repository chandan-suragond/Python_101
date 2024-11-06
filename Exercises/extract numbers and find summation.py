# extract numbers and find summation 

s= "3hjblj23bh4jh23vbj4hv23;j4vhu234v;h32v4h2;3v4h23lj87"

def find_num_summation(s):
    numbers = []
    current_num = ''

    for ch in s:
        if ch.isdigit():
            current_num+=ch
        elif current_num:
            numbers.append(int(current_num))
            current_num = ''
    numbers.append(int(current_num))
    return sum(numbers)
 
print(find_num_summation(s))