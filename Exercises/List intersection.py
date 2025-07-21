#code to write common elements from 2 lists and sort it in descending order

def intersection(a, b):
  return sorted(list(set(a) & set(b)),reverse=True)

print(intersection([3,1,2],[1,0,2]))