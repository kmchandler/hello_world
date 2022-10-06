import random

animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

greeting = input("Please choose from the following greetings: Input 1 for Southern, 2 for English, and 3 for German")

while len(greeting) <=1:
  if greeting == '1':
      print("Howdy, Yall!")
      break
  if greeting == '2':
      print("Hello!")
      break
  if greeting == '3':
      print("Guten Tag!!")
      break
  else:
      print("Howdy, Y'all!")
    
animal_names = input("List out some funny animal names:")
animal_list = animal_names.split(' ')
for num, animal in enumerate(animal_list,1):
     print(num, animal)

for animal in animals:
    if len(animal) >= 5:
        print(animal)

random_animal = random.choice(animal_list)

fav_color = input("What is your favorite color?")
print(f"Whould you like to have a {fav_color} {random_animal}")
