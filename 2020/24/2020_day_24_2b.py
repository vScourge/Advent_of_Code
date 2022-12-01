"""
--- Day 24: Lobby Layout ---
Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. 
You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the 
check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. 
Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. 
The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). 
Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting 
from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. 
These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of 
these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference 
tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. 
For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew

In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?


--- Part Two ---
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208

After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?
"""

### IMPORTS ###

import collections
import math
import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'

NE = 0
E = 1
SE = 2
SW = 3
W = 4
NW = 5


### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	paths = [ ]
	l = 0
	
	for line in lines:
		moves = [ ]
		i = 0
		
		while i < len( line ):
			c = line[ i ]
			
			if c == 'e':
				moves.append( E )
				i += 1
			elif c == 'w':
				moves.append( W )
				i += 1
			elif c == 'n':
				if line[ i+1 ] == 'e':
					moves.append( NE )
				else:
					moves.append( NW )
				i += 2
			else:
				if line[ i+1 ] == 'e':
					moves.append( SE )
				else:
					moves.append( SW )
				i += 2
		
		paths.append( moves )		
		l += 1
		
	return paths


def move_on_grid( pos, direction ):
	if direction == NE:
		pos = ( pos[ 0 ], pos[ 1 ] - 1 )
	elif direction == E:
		pos = ( pos[ 0 ] + 1, pos[ 1 ] )
	elif direction == SE:
		pos = ( pos[ 0 ] + 1, pos[ 1 ] + 1 )
	elif direction == SW:
		pos = ( pos[ 0 ], pos[ 1 ] + 1 )
	elif direction == W:
		pos = ( pos[ 0 ] - 1, pos[ 1 ] )
	elif direction == NW:
		pos = ( pos[ 0 ] - 1, pos[ 1 ] - 1 )
		
	return pos


def get_adjacent_hexes( pos ):
	adj_dirs = (
	    ( 0, -1 ),
	    ( 1, 0 ),
	    ( 1, 1 ),
	    ( 0, 1 ),
	    ( -1, 0 ),
	    ( -1, -1 )
	)
	
	hexes = [ ]
	
	for adj_dir in adj_dirs:
		adj_pos = ( pos[ 0 ] + adj_dir[ 0 ], pos[ 1 ] + adj_dir[ 1 ] )
		hexes.append( adj_pos )
			
	return hexes


def get_adjacent_values( grid, pos ):
	adj_hexes = get_adjacent_hexes( pos )
		
	values = [ ]
	
	for adj_hex in adj_hexes:
		if adj_hex in grid:
			values.append( grid[ adj_hex ] )
		else:
			values.append( True )
			
	return values
	

def main( paths ):
	"""
	"""
	grid = { (0,0): True }	# True = white
	pos = ( 0, 0 )
	
	for path in paths:
		#print( '\nPath =', path )
		
		for direction in path:
			pos = move_on_grid( pos, direction )
			
			if pos not in grid:
				grid[ pos ] = True
				
			#print( 'dir {0}, pos {1} = {2}'.format( direction, pos, grid[ pos ] ) )

		# Flip this tile
		grid[ pos ] = not grid[ pos ]

		# Reset to reference tile		
		pos = ( 0, 0 )

	print( 'day = 0, count = {0}\n'.format( list( grid.values( ) ).count( False ) ) )
			
	# Simulate days
	# 1. Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
	# 2. Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
	for day in range( 100 ):
		# Since the default for tiles is white (True), we have to explicitly add white tiles around
		# each black tile, so rule #2 above can apply correctly.
		grid2 = dict( grid )
		
		for pos, val in grid.items( ):
			if not val:
				for a_pos in get_adjacent_hexes( pos ):
					if a_pos not in grid:
						grid2[ a_pos ] = True
		
		grid = dict( grid2 )
		
		# Make fresh copy
		grid2 = dict( grid )
		
		for pos, val in grid.items( ):
			count = get_adjacent_values( grid, pos ).count( False )
			
			if grid[ pos ] == False and ( count == 0 or count > 2 ):
				grid2[ pos ] = True
			elif grid[ pos ] == True and count == 2:
				grid2[ pos ] = False

		grid = dict( grid2 )
		
		print( 'day = {0}, count = {1}'.format( day+1, list( grid.values( ) ).count( False ) ) )
	
	return list( grid.values( ) ).count( False )
	
# test answer = 67384529

### CLASSES ###

#class Point( ):
	#def __init__( self, x, y ):
		#self.x = x
		#self.y = y
		
	#def __repr__( self ):
		#return '<Point ({0}, {1})>'.format( self.x, self.y )
	

### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	paths = parse_input( )
	answer = main( paths )
	
	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 30033 not right
