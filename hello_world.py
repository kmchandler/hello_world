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

for animal in animals:
    if len(animal) >= 5:
        print(animal)
