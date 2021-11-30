
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

def ChangeAvailability():
    print("The Available items are: ")
    for i in range(len(Available()[0])):
        print(Available()[0][i])
    print("The out of stock items are: ")
    for k in range(len(Available()[1])):
        print(Available()[1][k])
    item = input("Enter the name of the item to change: ")
    status = input("If the item is out of stock enter F, in the contrary enter T: ")
    if item in fL:
        if status.upper() == "F":
            restaurant[item].insert(0, False)
        elif status.upper() == "T":
            restaurant[item].insert(0, True)

restaurant = Menu("spam.txt")
fL = FoodList("spam.txt")

print(restaurant)
print(len(fL))
print(Available())
print(ChangeAvailability())
