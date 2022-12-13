"""
Advent of Code 2022
Adam Pletcher
adam.pletcher@gmail.com

--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a 
decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area 
from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where 
a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best 
signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has 
elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can 
move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of 
the destination square can be at most one higher than the elevation of your current square; that is, if your current 
elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the 
destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but 
eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or 
right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""

import numpy
import string


class Point2( ):
	def __init__(self, y, x, height):
		self.id = (y,x)
		self.x = x
		self.y = y
		self.height = height
		self.links = [ ]
		
	def __repr__(self):
		return f'<Point2 ({self.y},{self.x}) h:{self.height}>'


def parse_input( ) -> tuple:
	lines = [ ]
	points = { }
	x = 0
	y = 0
	
	for line in open('input.txt', 'r'):
		row = [ ]
		
		for c in line.strip():
			if c == 'S':
				height = 0
				coord_start = (y,x)
			elif c == 'E':
				height = 25
				coord_end = (y,x)
			else:
				height = string.ascii_lowercase.index(c)

			point = Point2(y, x, height)
			points[(y,x)] = point
		
			row.append(height)
			x += 1

		lines.append(row)
		y += 1
		x = 0
		
	grid = numpy.array(lines)
		
	return (grid, points, points[coord_start], points[coord_end])


def build_links(grid, points) -> None:
	col_len = len(grid)
	row_len = len(grid[0])
	
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			point = points[(y,x)]
			
			coords = (
				(point.y-1, point.x),
				(point.y, point.x+1),
				(point.y+1, point.x),
				(point.y, point.x-1)
			)
			
			# Get rid of any that are off the edge
			coords = [c for c in coords if c[1] >= 0 and c[0] >= 0 and c[1] < row_len and c[0] < col_len]
			
			# Get rid of any that are more than 1 level above this point
			links = [ ]
			
			for c in coords:
				dest = points[c]
				
				if dest.height > point.height + 1:
					continue
				
				links.append(dest)
				
			point.links = links
			
	return points
	

def pathfind( node_start, node_end ):
	"""
	Adapted from
	http://ai-depot.com/Tutorial/PathFinding.html
	https://web.archive.org/web/20200204071343/http://ai-depot.com/Tutorial/PathFinding.html
	"""

	path = [node_start]
	visited_nodes = [node_start]
	path_lengths = { }
	
	while path:
		node = path.pop(0)
	
		if node == node_end:
			return path_lengths[node]
		
		for link in node.links:
			if link in visited_nodes:
				continue

			path.append(link)
			visited_nodes.append(link)
			path_lengths[link] = path_lengths.get(node, 0) + 1
			

if __name__ == '__main__':
	grid, points, start, end = parse_input()
	points = build_links(grid, points)
	
	path_length = pathfind(start, end)
	
	print('answer =', path_length)
