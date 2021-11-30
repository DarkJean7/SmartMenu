
def Menu(file):
    file = open(file, 'r')
    food = {}
    for line in file:
        line = line.rstrip()
        if line != "" and line[0].isupper() and not line.endswith(':'): #food
            f = line
            food.update({line : [True]})
        elif line != "" and line[0].islower(): #ingredients
            food[f].append(line)
    return food

def FoodList(file):
    file = open(file, 'r')
    foodList = []
    for line in file:
        line = line.rstrip()
        if line != "" and line[0].isupper() and not line.endswith(':'):
            foodList.append(line)
    return foodList

def Available():
    available = []
    notAvailable = []
    for k in range(len(fL)):
        if restaurant.get(fL[k])[0]:
            available.append(fL[k])
        else:
            notAvailable.append(fL[k])
    return available, notAvailable

restaurant = Menu("spam.txt")
fL = FoodList("spam.txt")

print(restaurant)
print(len(fL))
print(Available())
