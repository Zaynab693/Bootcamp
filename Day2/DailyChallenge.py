#Challenge 1: Multiples of a Number
#Instructions:
#1. Ask the user for two inputs:
#A number (integer).
#A length (integer).
#2. Create a program that generates a list of multiples of the given number.
#3. The list should stop when it reaches the length specified by the user.

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)

#-----------------------------------------------------------------------------------------------------------
#Challenge 2: Remove Consecutive Duplicate Letters
#Instructions:


user_input = input("Enter a string: ")


result = ""


for i in range(len(user_input)):
    
    if i == 0 or user_input[i] != user_input[i-1]:
        result += user_input[i]


print("Modified string:", result)


