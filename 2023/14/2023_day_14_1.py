"""
Advent of Code 2023
Adam Pletcher
adam.pletcher@gmail.com

--- Day 14: Parabolic Reflector Dish ---
You reach the place where all of the mirrors were pointing: a massive parabolic reflector dish attached to the side 
of another large mountain.

The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic 
reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant 
to focus light, all it's doing right now is sending it in a vague direction.

This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where 
it's pointing and use the light to fix the lava production.

Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and 
pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. 
Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls 
which ropes move and ultimately the focus of the dish.

In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that 
lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while 
the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks 
(your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....

You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't 
collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south 
edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, 
the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1

The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north 
support beams?
"""

import numpy

DIR_N = (-1, 0)
DIR_E = (0, 1)
DIR_S = (1, 0)
DIR_W = (0, -1)


class Point2():
	def __init__(self, y, x):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return f'<Point2 ({self.y}, {self.x}>'

	
class Rock():
	def __init__(self, shape, y, x):
		self.pos = Point2(y, x)
		self.shape = shape

	def __repr__(self):
		return f'<Rock {self.shape} ({self.pos.y}, {self.pos.x})>'
	

def parse_input():
	grid = [ ]
	rocks = { }

	for line in open('input.txt', 'r'):
		row = [c for c in line.strip()]
		grid.append(numpy.array(row))
		
	grid = numpy.array(grid)
	
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] != '.':
				rock = Rock(grid[y][x], y, x)
				rocks[(y,x)] = rock
				
	return (grid, rocks)


def roll_rocks(grid, rocks, dir):
	max_x = max([r.pos.x for r in rocks.values()])
	max_y = max([r.pos.y for r in rocks.values()])
	moved = True

	if dir == DIR_N:
		while moved:
			moved = False

			for y in range(1, max_y+1):
				for x in range(0, max_x+1):
					rock = rocks.get((y, x))
					
					if rock and rock.shape == 'O' and not (y-1, x) in rocks:
						rocks.pop((y, x))
						rock.pos = Point2(y-1, x)
						rocks[(y-1, x)] = rock
						moved = True
				
	if dir == DIR_S:
		while moved:
			moved = False

			for y in range(max_y-1, 0, -1):
				for x in range(0, max_x+1):
					rock = rocks.get((y, x))
					
					if rock and rock.shape == 'O' and not (y+1, x) in rocks:
						rocks.pop((y, x))
						rock.pos = Point2(y+1, x)
						rocks[(y+1, x)] = rock
						moved = True

	if dir == DIR_E:
		while moved:
			moved = False

			for y in range(0, max_y+1):
				for x in range(max_x, 0, -1):
					rock = rocks.get((y, x))
					
					if rock and rock.shape == 'O' and not (y, x+1) in rocks:
						rocks.pop((y, x))
						rock.pos = Point2(y, x+1)
						rocks[(y, x+1)] = rock
						moved = True

	if dir == DIR_W:
		while moved:
			moved = False

			for y in range(0, max_y+1):
				for x in range(1, max_x+1):
					rock = rocks.get((y, x))
					
					if rock and rock.shape == 'O' and not (y, x-1) in rocks:
						rocks.pop((y, x))
						rock.pos = Point2(y, x-1)
						rocks[(y, x-1)] = rock
						moved = True

	grid2 = [ ]
	for row in grid:
		grid2.append(numpy.array(['.' for x in range(len(grid[0]))]))
		
	grid = numpy.array(grid2)
	
	for pos, rock in rocks.items():
		grid[pos] = rock.shape
	
	return (grid, rocks)


def get_load_number(grid, rocks, dir):
	total = 0
	
	for pos, rock in rocks.items():
		if rock.shape == '#':
			continue
		
		if dir == DIR_N:
			load = len(grid) - rock.pos.y
			total += load

	return total


if __name__ == '__main__':
	grid, rocks = parse_input()
	
	print(grid)
	
	grid, rocks = roll_rocks(grid, rocks, DIR_N)
	print('')
	print(grid)
	
	total = get_load_number(grid, rocks, DIR_N)
	
	print(f'total = {total}')
	
