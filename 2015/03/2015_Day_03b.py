"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via 
radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), 
or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and 
Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

import time


### CLASSES ###


### FUNCTIONS ###

def move( grid, pos, dir ):
	if dir == '^':
		pos = ( pos[ 0 ], pos[ 1 ] - 1 )
	elif dir == '>':
		pos = ( pos[ 0 ] + 1, pos[ 1 ] )
	elif dir == '<':
		pos = ( pos[ 0 ] - 1, pos[ 1 ] )
	elif dir == 'v':
		pos = ( pos[ 0 ], pos[ 1 ] + 1 )

	if pos in grid:
		grid[ pos ] += 1
	else:
		grid[ pos ] = 1

	return ( grid, pos )

	
### MAIN ###

if __name__ == "__main__":
	time_start = time.time( )

	pos1 = (0,0)
	pos2 = (0,0)
	
	grid = { pos1: 0 }
	count = 0

	directions = open( 'input.txt', 'r' ).read( )
	santa_moves = True
	
	for dir in directions:
		if santa_moves:
			grid, pos1 = move( grid, pos1, dir )
		else:
			grid, pos2 = move( grid, pos2, dir )
			
		santa_moves = not santa_moves
	
	print( 'gifted houses = {0}'.format( len( grid ) ) )
	print( 'done in {0:.2f} secs'.format( time.time( ) - time_start ) )