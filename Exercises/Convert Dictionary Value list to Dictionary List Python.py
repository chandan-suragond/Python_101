# Convert Dictionary Value list to Dictionary List Python

test_list = [{'Gfg' : [5, 6, 5]}, {'is' : [10, 2, 3]}, {'best' : [4, 3, 1]}] 
op_list = [{'Gfg': 5, 'is': 10, 'best': 4}, {'Gfg': 6, 'is': 2, 'best': 3}, {'Gfg': 5, 'is': 3, 'best': 1}]

print(f"Init list {test_list}")
res = [{} for ind in range(len(test_list))]
# print(res)
ind = 0
for el in test_list:
      # {'Gfg' : [5, 6, 5]}
      # print(el)
      for k,v in el.items():
            # 'Gfg' : [5, 6, 5]
            for val in v:
                  # [5, 6, 5]
                  res[ind][k] = val
                  # print(k,v)
                  ind+=1
            ind=0

print(f"Result {res}")