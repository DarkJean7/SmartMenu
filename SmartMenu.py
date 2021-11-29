
def Menu(file):
    file = open(file, 'r')
    food = []
    ingredients = []
    for line in file:
        line = line.rstrip()
        if line != "" and line[0].isupper() and not line.endswith(':'): #food
            food.append(line)
        elif line != "" and line[0].islower() and line not in ingredients: #ingredients
            ingredients.append(line)
            ingredients = sorted(ingredients)
    print(food, ingredients)
    
print(Menu("spam.txt"))
