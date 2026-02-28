#Challenge 1: Letter Index Dictionary
#Instructions:
#1. User Input:
word= input("Enter a word:")
#2. Creating the Dictionary:
char_indices = {}
for index, char in enumerate(word):
    if char in char_indices:
        char_indices[char].append(index)  
    else:
        char_indices[char] = [index] 
#3. Displaying the Result:
print(char_indices) 


#--------------------------------------------------------------------------------------------------------------------------------
#Challenge 2: Affordable Items
#Instructions:
# Store Data:
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Data Cleaning:
money = int(wallet.replace("$", "").replace(",", ""))
clean_items_purchase = {item: int(price.replace("$", "").replace(",", "")) for item, price in items_purchase.items()}
#Determining Affordable Items:
basket = []
for item, price in clean_items_purchase.items():
    if price <= money:
        basket.append(item)
        money -= price

#Displaying the Result:
# 4. Print result
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
   