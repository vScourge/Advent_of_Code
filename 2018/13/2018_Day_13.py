"""
--- Day 13: Mine Cart Madness ---
A crop of this size requires significant logistics to transport produce, soil, fertilizer, and so on. The Elves are very busy
pushing things around in carts on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for another 1000 years, the Elves seem to be making this
up as they go along. They haven't even figured out how to avoid collisions yet.

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (| and -), curves (/ and \), and intersections (+). Curves connect exactly two perpendicular
pieces of track; for example, this is a closed loop:

/----\
|    |
|    |
\----/
Intersections occur when two perpendicular paths cross. At an intersection, a cart is capable of turning left, turning right,
or continuing straight. Here are two loops connected by two intersections:

/-----\
|     |
|  /--+--\
|  |  |  |
\--+--/  |
   |     |
   \-----/
Several carts are also on the tracks. Carts always face either up (^), down (v), left (<), or right (>). (On your initial map,
the track under each cart is a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it turns left the first time, goes straight the
second time, turns right the third time, and then repeats those directions starting again with left the fourth time, straight
the fifth time, and so on. This process is independent of the particular intersection at which the cart has arrived - that is,
the cart has no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a time. They do this based on their current location:
carts on the top row move first (acting from left to right), then carts on the second row move (again from left to right), then
carts on the third row, and so on. Once each cart has moved one step, the process repeats; each of these loops is called a tick.

For example, suppose there are two carts on a straight track:

|  |  |  |  |
v  |  |  |  |
|  v  v  |  |
|  |  |  v  X
|  |  ^  ^  |
^  ^  |  |  |
|  |  |  |  |
First, the top cart moves. It is facing down (v), so it moves down one square. Second, the bottom cart moves. It is facing up (^),
so it moves up one square. Because all carts have moved, the first tick ends. Then, the process repeats, starting with the first
cart. The first cart moves down, then the second cart moves up - right into the first cart, colliding with it! (The location of
the crash is marked with an X.) This ends the second and last tick.

Here is a longer example:

/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/-->\
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/

/---v
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/

/---\
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/

/---\
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/

/---\
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/

/---\
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/---\
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/

/---\
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/

/---\
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/

/---\
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/
After following their respective paths for a while, the carts eventually crash. To help prevent crashes, you'd like to know the location of the
first crash. Locations are given in X,Y coordinates, where the furthest left column is X=0 and the furthest top row is Y=0:

           111
 0123456789012
0/---\
1|   |  /----\
2| /-+--+-\  |
3| | |  X |  |
4\-+-/  \-+--/
5  \------/
In this example, the location of the first crash is 7,3.


--- Part Two ---
There isn't much you can do to prevent crashes in this ridiculous system. However, by predicting the crashes,
the Elves know where to be in advance and instantly remove the two crashing carts the moment any crash occurs.

They can proceed like this for a while, but eventually, they're going to run out of carts. It could be useful
to figure out where the last cart that hasn't crashed will end up.

For example:

/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/

/---\
|   |
| v-+-\
| | | |
\-+-/ |
  |   |
  ^---^

/---\
|   |
| /-+-\
| v | |
\-+-/ |
  ^   ^
  \---/

/---\
|   |
| /-+-\
| | | |
\-+-/ ^
  |   |
  \---/
After four very expensive crashes, a tick ends with only one cart remaining; its final location is 6,4.

What is the location of the last cart at the end of the first tick where it is the only cart left?
"""

import sys
import time


DIR_N 		= 0
DIR_E 		= 1
DIR_S 		= 2
DIR_W 		= 3

DIRS 			= ( DIR_N, DIR_E, DIR_S, DIR_W )
DIR_CHARS	= ( '^', '>', 'v', '<' )

LEFT 			= 0
STRAIGHT		= 1
RIGHT			= 2


### CLASSES ###

class Point( ):
	def __init__( self, x, y ):
		self.x = x
		self.y = y


	def get_tuple( self ):
		return ( self.x, self.y )


	def __eq__( self, other ):
		return self.x == other.x and self.y == other.y


	def __repr__( self ):
		return '<Point ({0},{1})>'.format( self.x, self.y )


class Cart( ):
	def __init__( self, pos, dir ):
		self.pos = pos
		self.dir = dir
		self.next_turn = LEFT


	def __lt__( self, other ):
		if self.pos.y < other.pos.y:
			return True

		if self.pos.y == other.pos.y and self.pos.x < other.pos.x:
			return True

		return False


	def __repr__( self ):
		return '<Point ({0},{1}),{2}>'.format( self.pos.x, self.pos.y, self.dir )


### FUNCTIONS ###

def get_next_spot( pos, dir ):
	x = pos.x
	y = pos.y

	if dir == DIR_N:
		y -= 1
	elif dir == DIR_E:
		x += 1
	elif dir == DIR_S:
		y += 1
	else:
		x -= 1

	return Point( x, y )


def get_map_str( map, carts ):
	buf = ''

	for y in range( len( map ) ):
		row = map[ y ]

		for cart in carts:
			if cart.pos.y == y:
				row = row[ :cart.pos.x ] + DIR_CHARS[ cart.dir ] + row[ cart.pos.x+1: ]

		buf += row + '\n'

	return buf


### MAIN ###

if __name__ == "__main__":

	map = [ ]

	for line in open( 'input.txt', 'r' ):
		map.append( line.rstrip( '\n' ) )

	# Find carts on initial map
	# Replace them with map characters
	carts = [ ]
	y = 0

	for y in range( len( map ) ):
		row = map[ y ]

		for x in range( len( row ) ):
			c = row[ x ]

			if c in DIR_CHARS:
				c_dir = DIR_CHARS.index( c )
				carts.append( Cart( Point( x, y ), c_dir ) )

				if c_dir == DIR_E or c_dir == DIR_W:
					map[ y ] = row[ :x ] + '-' + row[ x+1: ]
				else:
					map[ y ] = row[ :x ] + '|' + row[ x+1: ]

	turn = 1
	first_crash = True
	dead_carts = [ ]

	# Main loop
	while True:
		carts.sort( )

		for cart in carts:
			pos2 = get_next_spot( cart.pos, cart.dir )
			spot2 = map[ pos2.y ][ pos2.x ]

			if spot2 == '\\':
				if cart.dir == DIR_S:
					cart.dir = DIR_E
				elif cart.dir == DIR_W:
					cart.dir = DIR_N
				elif cart.dir == DIR_N:
					cart.dir = DIR_W
				elif cart.dir == DIR_E:
					cart.dir = DIR_S

			elif spot2 == '/':
				if cart.dir == DIR_S:
					cart.dir = DIR_W
				elif cart.dir == DIR_W:
					cart.dir = DIR_S
				elif cart.dir == DIR_N:
					cart.dir = DIR_E
				elif cart.dir == DIR_E:
					cart.dir = DIR_N

			elif spot2 == '+':
				if cart.next_turn == 0:
					cart.dir -= 1
					if cart.dir < 0:
						cart.dir = 3
				elif cart.next_turn == 2:
					cart.dir += 1
					if cart.dir > 3:
						cart.dir = 0

				cart.next_turn += 1
				if cart.next_turn > 2:
					cart.next_turn = 0

			cart.pos = pos2

			# See if it collided with another
			for other_cart in carts:
				if other_cart == cart:
					continue

				if other_cart.pos == cart.pos:

					if first_crash:
						print( 'crash = {0}, turn = {1}'.format( cart.pos.get_tuple( ), turn ) )
						first_crash = False

					dead_carts += [ cart, other_cart ]

		# remove dead carts
		carts = [ c for c in carts if c not in dead_carts ]

		# For part 2, see if we have only 1 cart left
		if len( carts ) == 1:
			print( 'last cart {0}, turn = {1}'.format( carts[ 0 ].pos.get_tuple( ), turn ) )
			sys.exit( )

		#print( '\n\n\n\n\n{0}'.format( get_map_str( map, carts ) ) )
		turn += 1

	print( 'done' )