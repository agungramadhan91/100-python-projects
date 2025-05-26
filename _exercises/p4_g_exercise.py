import random

row1 = ["😏","😏","😏"]
row2 = ["😏","😏","😏"]
row3 = ["😏","😏","😏"]

map  = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
coordinate = []

for xy in position:
    coordinate.append(xy)

coordinate_x = int(coordinate[0]) - 1
coordinate_y = int(coordinate[1]) - 1

map[coordinate_x][coordinate_y] = "👻"
print(f"{row1}\n{row2}\n{row3}")