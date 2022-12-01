"""
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a 
desert in the distance! Since you have some spare time, you might as well see if there was 
anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small 
images created by the satellite's camera array. The camera array consists of many cameras; 
rather than produce a single square image, they produce many smaller square image tiles that 
need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique 
ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and 
flipped to a random orientation. Your first task is to reassemble the original image by orienting 
the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that 
should line up exactly with its adjacent tiles. All tiles have this border, and the border lines 
up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have 
this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. 
If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
"""

### IMPORTS ###

import math
import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input_james.txt'

rules = { }

import sys
import re

def readFile(fileName):
	records = {}
	with open(fileName) as file:
		temp = []
		tile = ''
		for line in file:
			line = line.strip()
			if line != '':
				if line[0] == 'T':
					tile = line[5:9]
				else:
					temp.append(line)
			else:
				records[tile] = temp
				temp = []
	return records

def main(fileName):
	records = readFile(fileName)
	edges = {}
	prod = 1
	for key in records.keys():
		temp = []
		l = ''
		r = ''
		tile = records[key]
		for i in tile:
			l += i[0]
		for i in tile:
			r += i[-1]
		temp.append(tile[0])
		temp.append(tile[-1])
		temp.append(r)
		temp.append(l)
		temp.append(r[::-1])
		temp.append(l[::-1])
		temp.append(tile[0][::-1])
		temp.append(tile[-1][::-1])
		edges[key] = temp
	for key in edges.keys():
		check = edges[key]
		found = []
		for otherKey in edges.keys():
			if otherKey != key:
				comp = edges[otherKey]
				for side in check:
					if side in comp:
						if side not in found:
							found.append(side)
		if len(found) == 4:
			prod *= int(key)
	print(prod)






if __name__ == '__main__':
	if len(sys.argv) == 1:
		fileName = 'input.txt'
	else:
		fileName = sys.argv[1]
	main(fileName)
	
# 17250897231301
