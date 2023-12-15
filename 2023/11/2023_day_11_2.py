"""
Advent of Code 2023
Adam Pletcher
adam.pletcher@gmail.com

--- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to 
be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he 
confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there 
once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). 
The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. 
However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach 
the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or 
columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
   
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......

Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to 
assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......

In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each 
pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly 
one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......

This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations 
marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5

In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum 
of these lengths?

--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each 
empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 
empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths 
between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum 
of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far 
beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the 
shortest path between every pair of galaxies. What is the sum of these lengths?
"""

import numpy


class Point2():
	def __init__(self, y, x):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return f'<Point2 ({self.y}, {self.x}>'

	
class Galaxy():
	def __init__(self, y, x):
		self.pos = Point2(y, x)


	def __lt__(self, other):
		if self.pos.y < other.pos.y:
			return True
		elif self.pos.y == other.pos.y and self.pos.x < other.pos.x:
			return True
		else:
			return False
	
	def __eq__(self, other):
		return self.pos.y == other.pos.y and self.pos.x == other.pos.x

	def __hash__(self):
		return hash((self.pos.y, self.pos.x))

	def __repr__(self):
		return f'<Galaxy ({self.pos.y},{self.pos.x})>'



def distance(gal1, gal2, gaps_y, gaps_x):
	gap_amount = 1000000

	# Get Manhattan distance
	dist = abs(gal1.pos.x - gal2.pos.x) + abs(gal1.pos.y - gal2.pos.y)

	# Account for expansion gaps
	dist += sum(gap_amount - 1 for c in gaps_x if min(gal1.pos.x, gal2.pos.x) < c < max(gal1.pos.x, gal2.pos.x))
	dist += sum(gap_amount - 1 for r in gaps_y if min(gal1.pos.y, gal2.pos.y) < r < max(gal1.pos.y, gal2.pos.y))

	return dist
		


def parse_input():
	list_data = [ ]
	y = 0
	
	for line in open('input.txt', 'r'):
		line = line.strip()
		list_data.append(numpy.array([c for c in line]))

	data = numpy.array(list_data)
	
	# Now expand universe
	gaps_y = [ ]
	gaps_x = [ ]
	
	for y in range(len(data)-1, -1, -1):
		row = data[y]

		if len(set(row)) == 1:
			gaps_y.append(y)
		
	for x in range(len(data[0])-1, -1, -1):
		col = data[0:len(data), x:x+1]
		
		if len(set([c[0] for c in col])) == 1:
			gaps_x.append(x)

	
	# Now make galaxies
	galaxies = [ ]
	y = 0
	
	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == '#':
				galaxies.append(Galaxy(y, x))
			x += 1
		y += 1
		
	galaxies.sort()

	return (data, galaxies, gaps_y, gaps_x)
		

if __name__ == '__main__':
	data, galaxies, gaps_y, gaps_x = parse_input()
			
	pairs = { }
	done = [ ]
	
	for gal1 in galaxies:
		for gal2 in galaxies:
			if gal1 == gal2:
				continue
			
			pair_list = [gal1, gal2]
			pair_list.sort()
			pair = tuple(pair_list)
			
			if pair in pairs:
				continue
			
			dist = distance(gal1, gal2, gaps_y, gaps_x)
			pairs[pair] = dist

	total = sum(pairs.values())
	print(f'sum of distances = {total}')
	

# 82000210 too low
