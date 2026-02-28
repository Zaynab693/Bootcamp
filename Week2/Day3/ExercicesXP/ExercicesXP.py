#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency     # currency name (str)
        self.amount = amount         # currency amount (int or float)

    # STEP 1: String representation — used by print()
    def __str__(self):
        # plural 's' for amounts ≠ 1 (just like example)
        return f"{self.amount} {self.currency}s"

    # STEP 2: repr() representation — same as __str__ for this exercise
    def __repr__(self):
        return self.__str__()

    # STEP 3: convert currency object to integer
    def __int__(self):
        return self.amount

    # STEP 4: addition between Currency + Currency or Currency + int
    def __add__(self, other):
        # Case 1: adding another Currency object
        if isinstance(other, Currency):
            # Check currency labels match
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount

        # Case 2: adding an integer
        elif isinstance(other, int):
            return self.amount + other

        # If type not allowed → error
        raise TypeError("Unsupported type for addition")

    # STEP 5: in-place addition (+=)
    def __iadd__(self, other):
        # Case 1: add a Currency object
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

        # Case 2: add an int
        elif isinstance(other, int):
            self.amount += other
            return self

        raise TypeError("Unsupported type for in-place addition")
    
#---------------------------------------------------------------------------------------------------------------------------------
 #Exercise 3: String module
 # STEP 1: Import necessary modules
import string
import random

# STEP 2: Create a string of all uppercase and lowercase letters
all_letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# STEP 3: Generate a random string of length 5
random_string = ''.join(random.choice(all_letters) for _ in range(5))

# STEP 4: Print the random string
print(random_string)
#---------------------------------------------------------------------------------------------------------------------------------
#Exercise 4: Current Date
# STEP 1: Import the datetime module
import datetime

# STEP 2: Create a function to display the current date
def show_current_date():
    # STEP 2.1: Get the current date
    today = datetime.date.today()  # returns a date object

    # STEP 2.2: Display the date
    print(f"Today's date is: {today}")

# STEP 3: Call the function
show_current_date()
#---------------------------------------------------------------------------------------------------------------------------------
#Exercise 5: Amount of time left until January 1st
# STEP 1: Import the datetime module
import datetime

# STEP 2: Create a function to calculate time left until January 1st
def time_until_new_year():
    # STEP 2.1: Get the current date and time
    now = datetime.datetime.now()
    
    # STEP 3: Create a datetime object for January 1st of the next year
    next_year = now.year + 1
    jan1 = datetime.datetime(next_year, 1, 1, 0, 0, 0)
    
    # STEP 4: Calculate the time difference
    time_left = jan1 - now
    
    # STEP 5: Display the time difference
    print(f"Time left until January 1st: {time_left}")

# STEP 6: Call the function
time_until_new_year()
#---------------------------------------------------------------------------------------------------------------------------------
#Exercise 6: Birthday and minutes
# STEP 1: Import the datetime module
import datetime

# STEP 2: Create a function that calculates minutes lived
def minutes_lived(birthdate_str):
    """
    birthdate_str: string in 'YYYY-MM-DD' format, e.g., '1990-05-12'
    """
    # STEP 2.1: Parse the birthdate string into a datetime object
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    
    # STEP 2.2: Get the current datetime
    now = datetime.datetime.now()
    
    # STEP 2.3: Calculate the time difference
    time_diff = now - birthdate  # timedelta object
    
    # STEP 2.4: Convert the time difference to total minutes
    minutes = int(time_diff.total_seconds() / 60)
    
    # STEP 2.5: Display the result
    print(f"You have lived approximately {minutes} minutes.")

# STEP 3: Call the function with your birthdate
minutes_lived("2004-06-06")
#---------------------------------------------------------------------------------------------------------------------------------
#Exercise 7: Faker Module

# Step 1: Install faker (run this in your terminal, not in Python)
# pip install faker

# Step 2: Import the Faker class from the faker module
from faker import Faker

# Step 3: Create an instance of Faker
faker = Faker()

# Step 4: Create an empty list to store users
users = []

# Step 5: Create a function to generate fake users
def add_fake_users(number_of_users):
    """
    Generates 'number_of_users' fake users and appends them to the 'users' list.
    Each user is a dictionary with 'name', 'address', and 'language_code'.
    """
    for _ in range(number_of_users):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user)

# Step 6: Call the function to generate, e.g., 5 fake users
add_fake_users(5)

# Step 7: Print the list of users
for user in users:
    print(user)


