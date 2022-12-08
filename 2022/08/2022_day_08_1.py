"""
Advent of Code 2022
Adam Pletcher
adam.pletcher@gmail.com

--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a 
previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good 
location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count 
the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). 
For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider 
trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to 
block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of 
height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 
0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most 
height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this 
arrangement.

Consider your map; how many trees are visible from outside the grid?
"""

import numpy


def parse_input() -> numpy.array:
	lines = [ ]
	
	for line in open('input.txt', 'r'):
		lines.append([int(x) for x in line.strip()])
		
	data = numpy.array(lines)
		
	return data


def is_visible(data: numpy.array, coord: tuple) -> bool:
	cy, cx = coord
	val = data[coord]
	
	# Lines of sight in 4 directions: N, E, S, W
	lines = [
		data[:cy, cx:cx+1],
		data[cy+1:, cx:cx+1:],
		data[cy:cy+1, :cx],
		data[cy:cy+1, cx+1:]
	]
	
	for line in lines:
		line = numpy.ndarray.flatten(line)
		
		if all([x < val for x in line]):
			# All trees along this line of sight are shorter
			return True

	return False
	
	
if __name__ == '__main__':
	data = parse_input()
	
	size_y = len(data)
	size_x = len(data[0])

	# Count with all border trees, which are all visible from edge
	num_visible = size_y * 2 + size_x * 2 - 4
	
	for y in range(size_y-2):
		for x in range(size_x-2):
			if is_visible(data, (y+1,x+1)):
				num_visible += 1
	
	print('answer =', num_visible)
