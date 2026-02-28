# Exercise 1 : Use the terminal
# Instructions
# Run this command in the terminal to open a python console:
# python
# "The $PATH variable in Linux is essential for the system to locate the programs or scripts you're trying to run without needing to specify their full location.""
# "When you enter python3, the shell looks through the directories in the $PATH variable one by one, from left to right, until it finds the python3 program."
# Exercise 2 : Alias
# Instructions
# Read about alias, and try to open a python console with the command: py
# Exercise 2 : Alias
# Instructions
# Read about alias, and try to open a python console with the command:
# $ py
# Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:
3 <= 3 < 9 # True
3 == 3 == 3 # True
bool(0) # False
bool(5 == "5") # False
bool(4 == 4) == bool("4" == "4") # True
bool(bool(None)) # False
x = (1 == True)
y = (1 == False)
a = True + 4 # 5
b = False + 10 # 10
print("x is", x) # True
print("y is", y) # False
print("a:", a) # 5
print("b:", b) # 10

# Exercise 4 : How many characters in a sentence ?
#Instructions
#Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))
#Exercise 5: Longest word without a specific character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
sentence = ""
while True:
    user_input = input("Please enter a sentence without the letter 'A': ")
    if "A" not in user_input and len(user_input) > len(sentence):
        sentence = user_input
        print("Congratulations! You've set a new longest sentence.")