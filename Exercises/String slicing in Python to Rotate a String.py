# String slicing in Python to Rotate a String

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee" 

s = "GeeksforGeeks"
d = 2
# rotation = 'left'
rotation = 'right'

print(f"Actual string: {s}")
if rotation == 'left':
    print("Left rotated string w 2 places: ",s[d:]+s[:d])
elif rotation == 'right':
    print("Right rotated string w 2 places: ",s[-d:]+s[:-d])