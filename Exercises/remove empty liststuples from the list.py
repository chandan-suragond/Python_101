# Program to remove empty lists/tuples from the list

li = [2,3,1,['chan','dan'],[],(),['tim','cook'],[]]
# for ele in li:
#       if ele == []:
#             li.remove(ele)
# print(li)

# lst = list(filter(None,li)) #filters empty lists and tuples
# print(lst)

while [] in li :
    li.remove([])

print(li)