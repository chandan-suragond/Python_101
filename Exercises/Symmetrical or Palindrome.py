# Python program to check whether the string is Symmetrical or Palindrome

str = 'malayalam'

str_len = len(str)

first_half = str[:int(str_len/2)]
second_half = str[int(str_len/2):]
# reversed_second_half = ''.join(reversed(second_half))
# print(reversed_second_half)

print("String is symmetrical" if first_half == second_half else "String is not symmetrical")
print("String is a palindrome" if str == ''.join(reversed(str)) else "String is not a palindrome")


# # Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# # solution - 1
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(result)
# print(list(result))

# # solution - 2
# new_list = []
# for i,j in zip(numbers1,numbers2):
#     new_list.append(i+j)
# print(new_list)
