#Exercise 1: Favorite Numbers
#Instructions:

#Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers= {1,3,5,7,9}
#Add two new numbers to the set.
my_fav_numbers.add(11)
my_fav_numbers.add(70)
#Remove the last number you added to the set.
my_fav_numbers.remove(70)
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers= {2,4,6,8,10}
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

#-----------------------------------------------------------------------------------------------------------

#Exercise 2: Tuple
#Instructions:
#Given a tuple of integers, try to add more integers to the tuple.
my_tuple = (1, 2, 3, 4, 5)
my_tuple.append(6)  # This will raise an AttributeError
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
#Python enforces this to make tuples safe and efficient when used as fixed collections or as keys in dictionaries.
#-----------------------------------------------------------------------------------------------------------
# Exercise 3: List Manipulation
#Instructions:
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
basket.remove("Banana")
#Remove "Blueberries" from the list.
basket.remove("Blueberries")
#Add "Kiwi" to the end of the list.
basket.append("Kiwi")
#Add "Apples" to the beginning of the list. 
basket.insert(0, "Apples")
#Count how many apples are in the basket.
apple_count = basket.count("Apples")
#Clear the basket.
basket.clear()
#Print the final state of the list.
print(basket)
#-----------------------------------------------------------------------------------------------------------
# Exercise 4: Floats
#Instructions:
#Recap: What is a float? What’s the difference between a float and an integer?
#A float is a number that has a decimal point, while an integer is a whole number without a decimal point.
#Create a list containing the following sequence of mixed types: floats and integers:
mixed_numbers = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
#Avoid hard-coding each number manually.
mixed_numbers = [x * 0.5 for x in range(3, 11)]
#-----------------------------------------------------------------------------------------------------------
#Exercise 5: For Loop
#Instructions:
#Write a for loop to print all numbers from 1 to 20, inclusive.
for i in range(1,21):
    print(i)
#Write another for loop that prints every number from 1 to 20 where the index is even.
numbers = list(range(1, 21))
for index in range (len(numbers)):
    if index % 2 == 0:
        print(numbers[index])
#-----------------------------------------------------------------------------------------------------------
#Exercise 6: While Loop
#Instructions:
#Use an input to ask the user to enter their name.
while True:
    name = input("Enter your name: ")
    
    if len(name) >= 3 and not name.isdigit():
        print("Thank you!")
        break
    else:
        print("Please enter a valid name (at least 3 characters and no digits).", end=" ")
#-----------------------------------------------------------------------------------------------------------
#Exercise 7: Favorite Fruits
#Instructions:
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).

#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"
favorite_fruits = input("Enter your favorite fruits (separated by spaces): ").split()
any_fruit = input("Enter the name of a fruit: ")
if any_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


#-----------------------------------------------------------------------------------------------------------
#Exercise 8: Pizza Toppings
#Instructions:
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.
toppings = []  
base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping.lower() == "quit": 
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")
total_cost = base_price + (len(toppings) * topping_price)

print("\n--- Pizza Summary ---")
print("Your toppings:", ", ".join(toppings))
print(f"Total cost: ${total_cost:.2f}")
#-----------------------------------------------------------------------------------------------------------
#Exercise 9: Cinemax Tickets
#Instructions:
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.
total_cost = 0  
while True:
    age_input = input("Enter the age of a family member (or 'quit' to finish): ")

    if age_input.lower() == "quit":  
        break
    age = int(age_input)  
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price  
    print(f"Ticket price: ${price}")

print(f"\nTotal ticket cost for the family: ${total_cost}")
#-----------------------------------------------------------------------------------------------------------
#Exercise 9: Cinemax Tickets
#Instructions:
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.
total_cost = 0
while True:
    age_input = input("Enter the age of a family member (or 'quit' to finish): ")

    if age_input.lower() == "quit":  
        break

    age = int(age_input)  
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    total_cost += price  
    print(f"Ticket price: ${price}")

print(f"\nTotal ticket cost for the family: ${total_cost}")
#-----------------------------------------------------------------------------------------------------------
#Bonus
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.

attendees = []  

while True:
    age_input = input("Enter age of person (or 'quit' to finish): ")

    if age_input.lower() == "quit":
        break  
   
    age = int(age_input)

   
    if 16 <= age <= 21:
        attendees.append(age)
        print(" Allowed to watch the movie!")
    else:
        print("Not allowed (age restriction).")


print("\nFinal list of attendees:")
print(attendees)

