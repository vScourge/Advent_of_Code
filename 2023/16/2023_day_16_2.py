"""
Advent of Code 2023
Adam Pletcher
adam.pletcher@gmail.com

--- Day 16: The Floor Will Be Lava ---
With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production 
Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways 
are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.

Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. 
There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to 
the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty 
space (.), mirrors (/ and \), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts 
some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....

The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what 
it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.

If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For 
instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a 
rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.

If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter 
were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same 
direction.

If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the 
two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | 
splitter would split into two beams: one that continues upward from the splitter's column and one that continues 
downward from the splitter's column.

Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is 
energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..

Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving 
in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead 
only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..

Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing 
the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?

--- Part Two ---
As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. 
There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading 
away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, 
if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), 
any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, 
you need to find the configuration that energizes as many tiles as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\....
|v-v\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\
.v//.|.v..

Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..

Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in 
that configuration?
"""

import numpy

DIR_N = 0
DIR_E = 1
DIR_S = 2
DIR_W = 3

ID = 0

def parse_input():
	data = [ ]

	for line in open('input.txt', 'r'):
		row = [c for c in line.strip()]
		data.append(numpy.array(row))
			
	return numpy.array(data)


class Point2( ):
	def __init__( self, y, x ):
		self.y = y
		self.x = x
		
	def __repr__(self):
		return f'<Point2 ({self.y}, {self.x})>'

		
class Beam():
	def __init__(self, start_y, start_x, dir):
		global ID
		
		self.pos = Point2(start_y, start_x)
		self.dir = dir

		self.id = ID
		ID += 1

		self.path = numpy.array([self.pos])
		self.done = False
		

	def __repr__(self):
		return f'<Beam {self.id} ({self.pos.y}, {self.pos.x}), {beam.dir}>'


def get_num_energized(grid, y, x, dir):
	beam = Beam(y, x, dir)
	beams = numpy.array([beam])
	
	#cells_done = numpy.array([f'{beam.pos.y},{beam.pos.x},{beam.dir}'])
	cells_done = numpy.array([])
	
	while True:
		for i in range(len(beams)):
			beam = beams[i]
			
			while not beam.done:
				if beam.dir == DIR_N:
					new_pos = Point2(beam.pos.y-1, beam.pos.x)
				elif beam.dir == DIR_E:
					new_pos = Point2(beam.pos.y, beam.pos.x+1)
				elif beam.dir == DIR_S:
					new_pos = Point2(beam.pos.y+1, beam.pos.x)
				else:
					new_pos = Point2(beam.pos.y, beam.pos.x-1)

				if new_pos.x < 0 or new_pos.y < 0 or new_pos.x == len(grid[0]) or new_pos.y == len(grid):
					# Out of bounds
					beam.done = True
					continue
				
				# Move beam to new pos
				beam.pos = new_pos
				
				key = f'{beam.pos.y},{beam.pos.x},{beam.dir}'
				if key in cells_done:
					beam.done = True
					continue
				
				cells_done = numpy.append(cells_done, key)
				
				beam.path = numpy.append(beam.path, beam.pos)
				cell = grid[beam.pos.y][beam.pos.x]
				
				if cell == '.':
					continue
				elif cell == '\\':
					if beam.dir == DIR_N:
						beam.dir = DIR_W
					elif beam.dir == DIR_E:
						beam.dir = DIR_S
					elif beam.dir == DIR_S:
						beam.dir = DIR_E
					elif beam.dir == DIR_W:
						beam.dir = DIR_N
				elif cell == '/':
					if beam.dir == DIR_N:
						beam.dir = DIR_E
					elif beam.dir == DIR_E:
						beam.dir = DIR_N
					elif beam.dir == DIR_S:
						beam.dir = DIR_W
					elif beam.dir == DIR_W:
						beam.dir = DIR_S
				elif cell == '|':
					if beam.dir == DIR_N or beam.dir == DIR_S:
						continue
					else:
						# Dir is E or W
						beam.dir = DIR_N
						beam2 = Beam(beam.pos.y, beam.pos.x, DIR_S)
						beams = numpy.append(beams, beam2)
				elif cell == '-':
					if beam.dir == DIR_E or beam.dir == DIR_W:
						continue
					else:
						# Dir is N or S
						beam.dir = DIR_W
						beam2 = Beam(beam.pos.y, beam.pos.x, DIR_E)
						beams = numpy.append(beams, beam2)

		# See if we need another cycle
		if all(b.done for b in beams):
			break

	unique_cells_done = set([(int(c.split(',')[0]), int(c.split(',')[1])) for c in cells_done])
	
	for y in range(len(grid)):
		row = ''
		for x in range(len(grid[0])):
			if (y,x) in unique_cells_done:
				row += '#'
			else:
				row += '.'
				
		print(row)
	print('')
			
	total = len(unique_cells_done)		
	return total
	
	
if __name__ == '__main__':
	data = parse_input()
	grid = data
	max_energized = 0
	
	max_x = len(grid[0])-1
	max_y = len(grid)-1
	
	c = 0
	num_checks = len(grid) * 2 + len(grid[0]) * 2 + 4
	
	# Do corners first
	corners = [
		(0, -1, DIR_E),
		(-1, 0, DIR_S),
		(-1, max_x, DIR_S),
		(0, max_x+1, DIR_W),
		(max_y, max_x+1, DIR_W),
		(max_y+1, max_x, DIR_N),
		(max_y+1, 0, DIR_N),
		(max_y, -1, DIR_E)
	]
	
	for corner in corners:
		y, x, dir = corner
		max_energized = max(max_energized, get_num_energized(grid, y, x, dir))
		c += 1
		print('{0} of {1}, {2}'.format(c, num_checks, max_energized))
	
	# Now do edges
	for x in range(1, len(grid[0])-1):
		max_energized = max(max_energized, get_num_energized(grid, -1, x, DIR_S))
		c += 1
		print('{0} of {1}, {2}'.format(c, num_checks, max_energized))

	for x in range(1, len(grid[0])-1):
		max_energized = max(max_energized, get_num_energized(grid, len(grid), x, DIR_N))
		c += 1
		print('{0} of {1}, {2}'.format(c, num_checks, max_energized))

	for y in range(1, len(grid)-1):
		max_energized = max(max_energized, get_num_energized(grid, y, -1, DIR_E))
		c += 1
		print('{0} of {1}, {2}'.format(c, num_checks, max_energized))

	for y in range(1, len(grid)-1):
		max_energized = max(max_energized, get_num_energized(grid, y, len(grid[0]), DIR_W))
		c += 1
		print('{0} of {1}, {2}'.format(c, num_checks, max_energized))
		
	print('max_energized =', max_energized)
	