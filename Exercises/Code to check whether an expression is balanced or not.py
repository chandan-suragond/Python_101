# Code to check whether an expression is balanced or not 
class CreateStack():
      def __init__(self):
            self.stk = []

      def add_ele(self,ele):
            self.stk.append(ele)

      def rem_ele(self):
            self.stk.pop()

if __name__ == "__main__":
      stk1 = CreateStack()
      expr = '[{(()}]'
      # expr = '{(()}]'
      li = list(expr)
      opening_braces = '(','[','{'
      closing_braces = ')',']','}'

      for i in li:
            if i == '(' or i == '[' or i == '{':
                  stk1.add_ele(i)
            elif len(stk1.stk) !=0 and (stk1.stk[-1] == opening_braces[closing_braces.index(i)]):
                  stk1.rem_ele()
      if stk1.stk:
            print(f"Expression {expr} is not balanced")
      else:
            print(f"Expression {expr} is balanced")


# Incorrect approach
# li1 = list(expr)
# print(li1)
# li2 = list(reversed(list(expr)))
# print(li2)
# if li1 == li2:
#       print(f"Expression {expr} is balanced")
# else:
#       print(f"Expression {expr} is NOT balanced")

