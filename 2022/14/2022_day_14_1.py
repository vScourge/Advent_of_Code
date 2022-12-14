"""
Advent of Code 2022
Adam Pletcher
adam.pletcher@gmail.com

--- Day 14: Regolith Reservoir ---
The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the 
waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and 
the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into 
the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-
dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with 
structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the 
path, where x represents distance to the right and y represents distance down. Each path appears as a single line 
of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or 
vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; the first path consists of two straight lines, and the second 
path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 
498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes 
to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), 
the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the 
unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it 
is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible 
destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand 
is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.

The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.

After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.

After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.

Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.

Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the 
endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........

Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the 
abyss below?
"""

import numpy


class Point2:
	def __init__(self, y, x):
		self.y = y
		self.x = x
		
	def __repr__(self):
		return '<Point2 ({0},{1})>'.format(self.y, self.x)
	

def parse_input( ) -> tuple:
	line_coords = [ ]
	
	for line in open('input.txt', 'r'):
		parts = line.strip().split(' -> ')
		line_coords.append([(int(c.split(',')[0]), int(c.split(',')[1])) for c in parts])
		
	# Find min/max for grid array
	minx = 500
	miny = 0
	maxx = 500
	maxy = 0
	
	for c_line in line_coords:
		for c in c_line:
			minx = min(minx, c[0])
			miny = min(miny, c[1])
			maxx = max(maxx, c[0])
			maxy = max(maxy, c[1])

	# Make grid of required size, filled with empty char
	grid = numpy.full((maxy-miny+1, maxx-minx+1), fill_value = '.')
	
	# Draw lines on grid
	for c_line in line_coords:
		for i in range(len(c_line) - 1):
			c1x, c1y = c_line[i]
			c2x, c2y = c_line[i+1]
			
			if c1x != c2x:
				# Horiz line
				start, end = sorted([c1x, c2x])
				for x in range(start, end+1):
					grid[c1y-miny, x-minx] = '#'
			else:
				# Vert line
				start, end = sorted([c1y, c2y])
				for y in range(start, end+1):
					grid[y-miny, c1x-minx] = '#'
					
	return (grid, minx)


def print_grid(grid) -> None:
	print('')
	for row in grid:
		print(''.join(row))


def simulate_sand(grid, pos):
	start = Point2(pos.y, pos.x)
	
	while True:
		if pos.y+1 > len(grid):
			# off bottom of grid
			break
		
		# Check downward
		if grid[pos.y+1][pos.x] == '.':
			pos.y += 1
			continue
		
		if pos.x-1 < 0:
			# off left edge of grid
			break
		
		# Check lower-left
		if grid[pos.y+1][pos.x-1] == '.':
			pos.x -= 1
			continue
		
		if pos.x+1 >= len(grid[0]):
			# off right edge of grid
			break
		
		# Check lower-right
		if grid[pos.y+1][pos.x+1] == '.':
			pos.x += 1
			continue

		# Sand has come to a rest
		grid[pos.y][pos.x] = 'o'
		pos = Point2(start.y, start.x)
		
	return grid
		
		

if __name__ == '__main__':
	grid, minx = parse_input()

	sand_pos = Point2(0, 500-minx)

	grid = simulate_sand(grid, sand_pos)
	print_grid(grid)
	
	answer = list(numpy.ndarray.flatten(grid)).count('o')
	
	print('answer =', answer)
