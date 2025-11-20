#Daily challenge: Old MacDonald’s Farm
# Step 1: Create the Farm class
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {} 

    # Step 8: Upgrade add_animal to accept multiple animals using **kwargs
    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    # Step 4: get_info method
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    # Step 6: get_animal_types method
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Step 7: get_short_info method
    def get_short_info(self):
        animal_list = []
        for animal in self.get_animal_types():
            if self.animals[animal] > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)
        # Construct sentence
        if len(animal_list) > 1:
            animals_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        else:
            animals_str = animal_list[0]
        return f"{self.name}'s farm has {animals_str}."

# Step 5: Test the code
macdonald = Farm("McDonald")


