 #Exercise 1: Converting Lists into Dictionaries
#Instructions:
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result_dict=zip(keys,values)
print(dict(result_dict))

#-----------------------------------------------------------------------------------------------------------
#Exercise 2: Cinemax #2
#Instructions:
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Family members’ ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name.title()}’s ticket: ${price}")
    total_cost += price

print("Total cost for the family: $", total_cost)

#Bonus:
#Allow the user to input family members’ names and ages, then calculate the total ticket cost.
family = {}
while True:
    name=input("Enter family member's name (or done to finish):")
    if name.lower()=="done":
        break
    age=int(input(f"Enter age of {name}:"))

    family[name]=age

total_cost=0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name.title()}’s ticket: ${price}")
    total_cost += price

print("Total cost for the family: $", total_cost)
#-----------------------------------------------------------------------------------------------------------
#Exercise 3: Zara
#Instructions:
#Create and manipulate a dictionary that contains information about the Zara brand.
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Change the value of number_stores to 2.
brand["number_stores"] = 2
#Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara offers clothes for {', '.join(brand['type_of_clothes'])}.")
#Add a new key country_creation with the value Spain.
brand["country_creation"] = "Spain"
#Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
#Delete the creation_date key.
del brand["creation_date"]
#Print the last item in international_competitors.
print(brand["international_competitors"][-1])
#Print the major colors in the US.
print(brand["major_color"]["US"])
#Print the number of keys in the dictionary.
print(len(brand))
#Print all keys of the dictionary.
print(brand.keys())
#Bonus:

#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}
brand.update(more_on_zara)
print(brand)
#-----------------------------------------------------------------------------------------------------------
#Exercise 4: Disney Characters
#Instructions:
#You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#1. Create a dictionary that maps characters to their indices:
char_to_index = {char: index for index, char in enumerate(users)}
#2. Create a dictionary that maps indices to characters:
index_to_char = {index: char for index, char in enumerate(users)}
#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_char_to_index = {char: index for index, char in enumerate(sorted(users))}

