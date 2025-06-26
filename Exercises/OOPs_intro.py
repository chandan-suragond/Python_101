# This code is designed to analyze a string and find various character types within it.
# It includes methods to find alphabets, digits, special characters, uppercase letters, lowercase letters, and the length of the string.
# The main function prompts the user for input and creates an instance of the Intro class to perform the analysis.

class Intro:
    """
    A class to analyze a string and identify various character types within it.

    Attributes:
        s (str): The string to be analyzed.

    Methods:
        find_alphabet(): Prints all alphabetic characters in the string.
        find_digit(): Prints all digit characters in the string.
        find_special(): Prints all special (non-alphanumeric) characters in the string.
        find_uppercase(): Prints all uppercase alphabetic characters in the string.
        find_lowercase(): Prints all lowercase alphabetic characters in the string.
        find_length(): Prints the length of the string.
    """

    def __init__(self, s):
        """
        Initializes the Intro object with the provided string.

        Args:
            s (str): The string to be analyzed.
        """
        self.s = s

    def find_alphabet(self):
        """
        Prints all alphabetic characters in the string.
        If no alphabetic characters are found, prints a message indicating so.
        """
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
        """
        Prints all digit characters in the string.
        If no digits are found, prints a message indicating so.
        """
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
        """
        Prints all special (non-alphanumeric) characters in the string.
        If no special characters are found, prints a message indicating so.
        """
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
        """
        Prints all uppercase alphabetic characters in the string.
        If no uppercase letters are found, prints a message indicating so.
        """
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
        """
        Prints all lowercase alphabetic characters in the string.
        If no lowercase letters are found, prints a message indicating so.
        """
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
        """
        Prints the length of the string.
        """
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