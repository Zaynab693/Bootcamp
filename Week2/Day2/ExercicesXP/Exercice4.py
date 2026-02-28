#Step 1 — Create the Person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""   # empty string by default

    def is_18(self):
        return self.age >= 18
#Step 2 — Create the Family class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []    # list of Person objects

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("This family member does not exist.")

    def family_presentation(self):
        print(f"\nThe {self.last_name} Family:")
        for person in self.members:
            print(f"- {person.first_name}, {person.age} years old")
#Step 3 — Test the Classes
my_family = Family("Smith")

my_family.born("Alice", 17)
my_family.born("Bob", 20)
my_family.born("Charlie", 12)

my_family.family_presentation()

my_family.check_majority("Bob")
my_family.check_majority("Alice")
my_family.check_majority("Charlie")