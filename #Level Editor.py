#Level Editor
'''
import json
map_file_location = str(input("What level number (1 or 2)"))
map_file = open(str(map_file_location)+".json", "w")


map_x = int(input("How wide?"))
map_y = int(input("How long?"))
'''
map_x = 16
map_y = 16
level_full = []
level_length = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
i = 0




level_array = [[""]*map_y]*map_x

x = 0
y = 0
#ranlen = 16
print(range(len(level_array)))
print(range(len(level_array[y])))


for y in range(len(level_array)):
    print(str(y+1))
    level_array[x] = [["1"]*int]
    for x in range(len(level_array[y+1])):
        level_array[x][y] = (str(alphabet[y]).upper()) + str(y+1)
        x =+ 1
    
    y += 1
    x = 0

'''
for y in range(len(level_array)):
    y += 1
    for x in range(len(level_array[y-1])):
        temp_cord = (str(alphabet[x]).upper() + str(y))
        print(temp_cord)
        level_array[x][(y-1)] = temp_cord
        x += 1
    x = 0
'''
for i in range(len(level_array)):
    print(level_array[i])
    


#json.dump
    

'''
while i != map_y:
    level_length.append([])
    i += 1
y = 0
x = 0

while y != map_y:
    level_full.append([])
    while x != map_x:
        level_full[y].append(level_length)
        x += 1
    y += 1

for i in level_full:
    print(level_full[i])

'''