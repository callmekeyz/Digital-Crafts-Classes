my_pets = ["daisy","molly","shadow"]
my_pets.append("rainbow")
print(my_pets)

my_dogs = ["daisy","molly"]
my_cats = ["shadow","rainbow"]

my_pets = my_dogs + my_cats
my_pets = my_dogs + []
print(len(my_pets))
print(my_pets)
print(my_dogs)

combined_literal = [1,3,5] + ["a","b",True]
print(combined_literal)

new_set_of_pets = []
new_set_of_pets.extend(my_dogs)
print(new_set_of_pets)
new_set_of_pets.extend(my_cats)
print(new_set_of_pets)

my_pets[2:1] = ["el gato diablo","horseface cat"]
print(my_pets)
del my_pets[2]
print(my_pets)