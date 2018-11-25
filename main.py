"""
PLAN
    1. Read and store input tiles
    2. Put tiles into output with no constraints
    3. WFC algorithm
"""
import sys
import os
import random
import numpy as np
from PIL import Image


tiles = []
tileConnections = []
tileSize = (25,25)
outputSize = (150, 150)

print("Creating Tiles")
for input in os.listdir("Tiles"):
    if ".png" in input:
        with Image.open("Tiles/"+input) as img:
            for x in range(0, int(img.size[0] / tileSize[0])):
                for y in range(0, int(img.size[1] / tileSize[1])):
                    tiles.append(img.crop((x*tileSize[0], y*tileSize[1], (x+1)*tileSize[0], (y+1)*tileSize[1])))

print("Processing Tiles")
#add rotated tiles
tempTiles = []
for tile in tiles:
    tempTiles.append(tile.rotate(90))
    tempTiles.append(tile.rotate(180))
    tempTiles.append(tile.rotate(270))
tiles += tempTiles

for tile0 in tiles:
    for tile1 in tiles:
        imgArray0 = np.asarray(tile0)
        imgArray1 = np.asarray(tile1)

        if(imgArray0[0] == imgArray1[tileSize[0]]):
            





for i in range(0, len(tiles)):
    tiles[i].save("test/" + str(i) + ".png")

print("Assembling Output")
with Image.new("RGB", outputSize) as output:
    for x in range(0, int(outputSize[0] / tileSize[0])):
        for y in range(0, int(outputSize[1] / tileSize[1])):
            output.paste(random.choice(tiles), (x*tileSize[0], y*tileSize[1], (x+1)*tileSize[0], (y+1)*tileSize[1]))
    output.save("output.png")