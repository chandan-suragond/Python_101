# This code is designed to analyze a string and find various character types within it.
# It includes methods to find alphabets, digits, special characters, uppercase letters, lowercase letters, and the length of the string.
# The main function prompts the user for input and creates an instance of the Intro class to perform the analysis.
 
class Intro:
    def __init__(self, s):
        self.s = s

    def find_alphabet(self):
        count = 0
        for i in self.s:
            if i.isalpha():
                count = 1
                print(i, end=' ')
        if count == 0:
            print("No alphabets found in the string.")
        else:
            print()
        
    def find_digit(self):
        count = 0
        for i in self.s:
            if i.isdigit():
                count = 1
                print(i, end=' ')
        if count == 0:
            print("No digits found in the string.")
        else:
            print()

    def find_special(self):
        count = 0
        for i in self.s:
            if not i.isalnum():
                count = 1
                print(i, end=' ')
        if count == 0:
            print("No special characters found in the string.")
        else:
            print()

    def find_uppercase(self):
        count = 0
        for i in self.s:
            if i.isupper():
                count = 1
                print(i, end=' ')
        if count == 0:
            print("No uppercase letters found in the string.")
        else:
            print()

    def find_lowercase(self):
        count = 0
        for i in self.s:
            if i.islower():
                count = 1
                print(i, end=' ')
        if count == 0:
            print("No lowercase letters found in the string.")
        else:
            print()

    def find_length(self):
        print("Length of the string is:", len(self.s))

def main():
    """
    Main function to process a user-provided string or a default string.
    It creates an Intro object with the string and calls methods to:
    - Find and display all alphabetic characters.
    - Find and display all digits.
    - Find and display all special characters.
    - Find and display all uppercase letters.
    - Find and display all lowercase letters.
    - Find and display the length of the string.
    """
    s = input("Enter a string: ")
    s = '234cswer6234!@324dsfrAERC' if not s else s
    intro = Intro(s)
    intro.find_alphabet()
    intro.find_digit()
    intro.find_special()
    intro.find_uppercase()
    intro.find_lowercase()
    intro.find_length()

if __name__ == "__main__":
    main()