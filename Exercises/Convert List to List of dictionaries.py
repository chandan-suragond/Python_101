# Convert List to List of dictionaries

test_list = ['Gfg',3, "is", 8]
key_list = ["name", "id"] 

def dictify(test_li, key_li):
      result_list = []
      for i in range(0,len(test_li),2):
            for j in range(0,len(key_li),2):
                  result_list.append({key_li[j]:test_li[i],key_li[j+1]:test_li[i+1]})
      return result_list

print(f"List of dictionaries - {dictify(test_list,key_list)}")
