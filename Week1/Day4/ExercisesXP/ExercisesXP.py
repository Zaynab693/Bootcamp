#Exercise 1: What Are You Learning?
#Instructions:
#Step 1: Define a Function
def display_message():
    #Step 2: Print a Message
    print("I am learning about functions in Python!")
#Step 3: Call the Function
display_message()
#--------------------------------------------------------------------------------------------------------------------------------
#Exercise 2: What’s Your Favorite Book?
#Instructions:
#Step 1: Define a Function with a Parameter
def favorite_book(title):
    #Step 2: Print a Message with the Title
    print(f"One of my favorite books is {title}.")
#Call the Function with an Argument
favorite_book("To Kill a Mockingbird")
#--------------------------------------------------------------------------------------------------------------------------------
#Exercise 3: Some Geography
#Instructions:
#Step 1: Define a Function with Parameters ok
def describe_city(city, country="Unknown"):
    #Step 2: Print a Message
    print(f"{city} is in {country}.")
#Step 3: Call the Function
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
#--------------------------------------------------------------------------------------------------------------------------------
#Exercise 4: Random
#Instructions:
#Step 1: Import the Random Module
import random
#Step 2: Define a Function with a Parameter
def random_number(num):
    #Step 3: Generate a Random Number
    rand_num = random.randint(1, 100)
    #Step 4: Compare and Print a Message
    if num == rand_num:
        print(f"Congratulations! You guessed the number {rand_num} correctly!")
    else:
        print(f"Sorry, the correct number was {rand_num}. Better luck next time!")
#Step 5: Call the Function
random_number(42)
#--------------------------------------------------------------------------------------------------------------------------------
#Exercise 5: Let’s Create Some Personalized Shirts!
#Instructions:
#Step 1: Define a Function with Parameters
def make_shirt(size, text):
    #Step 2: Print a Message
    print(f"The shirt size is {size} and it has the message: '{text}' printed on it.")
#Step 3: Call the Function
make_shirt("Large", "Hello, World!")
#Step 4: Call the Function with Default Values
def make_shirt(size="Large", text="I love Python"):
    print(f"The shirt size is {size} and it has the message: '{text}' printed on it.")
#Step 5: Call the Function with Default and Custom Values
make_shirt()
make_shirt("Medium")
make_shirt("Small", "Amazing Code!")
#--------------------------------------------------------------------------------------------------------------------------------
#Exercise 6: Magicians…
#Instructions:
#Step 1: Create a List of Magician Names
magicians_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#Step 2: Create a Function to Display Magicians
def show_magicians(magician_names):

    for name in magician_names:
        print(name)
#Step 3: Create a Function to Modify the List
def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"
#Step 4: Call the Functions
make_great(magicians_names)
show_magicians(magicians_names)
#--------------------------------------------------------------------------------------------------------------------------------
#Exercise 7: Temperature Advice
#Instructions:
#Step 1: Create the get_random_temp() Function
def get_random_temp():
    return random.randint(-10, 40)
#Step 2: Create the main() Function
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
#Step 3: Provide Temperature-Based Advice
    if temp < 0:
        print("Brrr, it's freezing! Wear a heavy coat, scarf, and gloves.")
    elif 0 <= temp < 16:
        print("It's a bit chilly. Wear a coat.")
    elif 16 <= temp < 23:
        print("The weather is nice. A light jacket should be fine.")
    else:
        print("It's warm outside! No jacket needed.")
#Step 4: Floating-Point Temperatures (Bonus)
    temp_float = random.uniform(-10, 40)
    print(f"The floating-point temperature right now is {temp_float:.2f} degrees Celsius.")
#Step 5: Month-Based Seasons (Bonus)
import random

def get_random_temp(season):
    if season == "winter":
        return random.uniform(-10, 10)
    elif season == "spring":
        return random.uniform(10, 20)
    elif season == "summer":
        return random.uniform(20, 40)
    else:  
        return random.uniform(5, 20)

def main():
    month = int(input("Enter a month number (1-12): "))

    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 23:
        print("Nice weather.")
    elif temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
