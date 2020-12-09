#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
popi = Cat('Popi', 5)
maya = Cat('Maya', 9)
benji = Cat('Benji', 2)

# 2 Create a function that finds the oldest cat
def find_oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_age = find_oldest_cat(popi.age, maya.age, benji.age)
print(f"The oldest cat is {oldest_age} years old.")