# check if the string is balanced using dictionary

# s = '([]{}'
s = ')[]{}'
# s = '()[]{}'
list_s = list(s)
stack = []
brackets_dict = {'(':')', '[':']', '{':'}'}
isbalanced = True

for bracket in list_s:
    if bracket in brackets_dict.keys():
        stack.append(bracket)
        print(stack)
    elif bracket in brackets_dict.values():
      if stack and bracket == brackets_dict[stack[-1]]:
        stack.pop()
        print(stack)
      else:
         isbalanced = False

print("List is balanced") if not stack and isbalanced else print("List not balanced")

# ----------------------------------------------------------------------------
# check if the string is balanced using lists

s = '([]{}'
# s = ')[]{}'
# s = '()[]{}'
list_s = list(s)
stack = []
isbalanced = True
opening_brackets = '(','[','{'
closing_brackets = ')',']','}'

for bracket in list_s:
    if bracket in opening_brackets:
        stack.append(bracket)
        print(stack)
    elif bracket in closing_brackets:
        if stack and stack[-1] == opening_brackets[closing_brackets.index(bracket)]:
            stack.pop()
            print(stack)
        else:
            isbalanced = False  

print("List balanced") if isbalanced and not stack else print("List not balanced")          

# ----------------------------------------------------------------------------

# # Code to check whether an expression is balanced or not using Stacks
# class CreateStack():
#       def __init__(self):
#             self.stk = []

#       def add_ele(self,ele):
#             self.stk.append(ele)

#       def rem_ele(self):
#             self.stk.pop()

# if __name__ == "__main__":
#       stk1 = CreateStack()
#       expr = '[{(()}]'
#       # expr = '{(()}]'
#       li = list(expr)
#       opening_braces = '(','[','{'
#       closing_braces = ')',']','}'

#       for i in li:
#             if i == '(' or i == '[' or i == '{':
#                   stk1.add_ele(i)
#             elif len(stk1.stk) !=0 and (stk1.stk[-1] == opening_braces[closing_braces.index(i)]):
#                   stk1.rem_ele()
#       if stk1.stk:
#             print(f"Expression {expr} is not balanced")
#       else:
#             print(f"Expression {expr} is balanced")


