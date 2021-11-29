
def Menu(file):
    file = open(file, 'r')
    food = {}
    for line in file:
        line = line.rstrip()
        if line != "" and line[0].isupper() and not line.endswith(':'): #food
            f = line
            food.update({line : []})
        elif line != "" and line[0].islower(): #ingredients
            food[f].append(line)
    return food

print(Menu("spam.txt"))