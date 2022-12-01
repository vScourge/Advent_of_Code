"""
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. 
The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route 
directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system 
to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions 
paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. 
(That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would 
still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west 
position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
"""

### IMPORTS ###

import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'

NORTH		= 0
EAST		= 1
SOUTH		= 2
WEST 		= 3

LEFT		= 'L'
RIGHT		= 'R'
FORWARD		= 'F'

DIR_TO_MOVE = {
    NORTH: ( 0, -1 ),
    EAST: ( 1, 0 ),
    SOUTH: ( 0, 1 ),
    WEST: ( -1, 0 )
}

### FUNCTIONS ###



### CLASSES ###

class Pos( ):
	def __init__( self, x, y ):
		self.x = x
		self.y = y

	def __repr__( self ):
		return '<Pos ({0}, {1})>'.format( self.x, self.y )
	


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )
	
	instructions = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )
	
	pos_start = Pos( 0, 0 )
	pos = Pos( 0, 0 )
	facing = EAST				# 0 = N, 1 = E, 2 = S, 3 = W
	
	for instr in instructions:
		direction = instr[ 0 ]
		distance = int( instr[ 1: ] )
		
		if direction == 'N':
			pos.y -= distance
		elif direction == 'E':
			pos.x += distance
		elif direction == 'S':
			pos.y += distance
		elif direction == 'W':
			pos.x -= distance

		elif direction in ( 'L', 'R' ):
			if direction == 'L':
				mult = -1
			else:
				mult = 1
			
			facing += int( distance / 90 * mult )

			if facing < 0:
				facing += 4
			elif facing > 3:
				facing -= 4
			
		if direction == 'F':
			move_dir = DIR_TO_MOVE[ facing ]
			pos.x += move_dir[ 0 ] * distance
			pos.y += move_dir[ 1 ] * distance
			
		print( '{0}, {1}, {2}'.format( instr, pos, facing ) )
			
	
	distance = abs( pos.x + pos.y )
	print( 'answer =', distance )
	print( 'done in {0:.4f}'.format( time.perf_counter( ) - time_start ) )

# 2280