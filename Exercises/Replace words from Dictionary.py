# Replace words from Dictionary

test_str = 'geekforgeeks best for geeks'
repl_dict = {'geeks' : 'all CS aspirants'}

def replace_func(str, repl_dict):
      str = test_str.split()
      new_list = []
      for i in str:
            if i in repl_dict.keys():
                  new_list.append(repl_dict[i])
            else:
                  new_list.append(i)
      print(' '.join(new_list))

def replace_func2(str,repl_dict):
      return ' '.join([repl_dict.get(i,i) for i in str.split()])

replace_func(test_str,repl_dict)

print(replace_func2(test_str,repl_dict))

