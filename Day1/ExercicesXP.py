#Exercise 1: Hello World
#Instructions
#Print the following output using one line of code:
#Hello world
#Hello world
#Hello world
#Hello world
print("Hello World \n" * 4)
#Exercise 2: Some Math
#Instructions
#Write code that calculates the result of:

#(99^3)*8 (meaning 99 to the power of 3, times 8).
a = (99**3)*8
print(a)

#Exercise 3: What is the output?
#Instructions
#Predict the output of the following code snippets:
#Coment what is your guess, then run the code and compare
5 < 3 # False
3 == 3 # True
3 == "3" # False
"3" > 3 # Error
"Hello" == "hello" # False
#Exercise 4: Your Computer Brand
#Instructions           
#Create a variable called computer_brand which value is the brand name of your computer.    
computer_brand = "ASUS"
#Using the computer_brand variable, print a sentence that states the following:
print(f"I have a {computer_brand} computer.")

#Exercise 5: Your information
#Instructions
#Create a variable called name, and set it’s value to your name.
name = "Zaynab"
#Create a variable called age, and set it’s value to your age.
age = 21
#Create a variable called shoe_size, and set it’s value to your shoe size.
shoe_size = 38
#Create a variable called info, and set it’s value to a sentence that includes all the variables above.
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
#Print the info variable.
print(info)
#Exercise 6: A & B
#Instructions               
#Create two variables, a and b.
# #Each variable’s value should be a number.
a = 20
b = 10
#If a is bigger than b, print "Hello World"
if a > b:
    print("Hello World")
#Exercise 7: Odd or Even
#Instructions       
#Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Exercise 8: What’s your name?
#Instructions       
#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
name = input("What is your name? ")
if name == "Zaynab":
    print("WOW, we have the same name 😉!")
else:
    print("Nice to meet you, " + name + "! But my name is cooler 😎!")
#Exercise 9: Tall enough to ride a roller coaster
#Instructions
#Write code that will ask the user for their height in centimeters.
height = int(input("Please enter your height in centimeters: "))
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.
if height >= 145:
    print("You are tall enough to ride the roller coaster!")    
else:
    print("Sorry, you need to grow some more to ride the roller coaster.")