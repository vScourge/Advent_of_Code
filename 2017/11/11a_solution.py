"""
Advent of Code 2017

input is: input.txt

 create a list P
 add the start node S, to P giving it one element
 Until first path of P ends with G, or P is empty
	extract the first path from P
	extend the path one step to all neighbors creating X new paths
	reject all paths with loops
	add each remaining new path to P
 If G found -> success. Else -> failure.

  \  0  /
5  +---+  1
  /     \
-+       +-
  \     /
4  +---+  2
  /  3  \

"""

DIR_N		= 0
DIR_NE	= 1
DIR_SE	= 2
DIR_S		= 3
DIR_SW	= 4
DIR_NW	= 5

STR_TO_DIR = {
   'n': 		DIR_N,
   'ne':		DIR_NE,
   'se':		DIR_SE,
   's':		DIR_S,
   'sw':		DIR_SW,
   'nw':		DIR_NW,
}

HEXES = { } 		# key is hex ID, value is Hex object
NEXT_ID	= 0


class Hex( ):
	def __init__( self, ring ):
		global NEXT_ID

		self.id = int( NEXT_ID )
		NEXT_ID += 1

		self.ring = ring
		self.links = { }		# keys are direction, values are Hex objects



	def __repr__( self ):
		return '<Hex {0}>'.format( self.id )


def pathfind( node_start, node_goal ):
	"""
	Adapted from
	http://ai-depot.com/Tutorial/PathFinding.html
	"""

	paths = [ [ node_start ] ]

	final_path = None

	while True:
		# Extract first path from list
		path = paths.pop( 0 )
		# Get last node in that path
		node = path[ -1 ]

		new_paths = [ ]
		for link in node.links.values( ):
			new_path = path + [ link ]
			new_paths.append( new_path )

		# Remove new paths that form loops, where a node
		# is listed more than once in the path.
		new_paths = [ p for p in new_paths if len( p ) == len( set( p ) ) ]

		# Add the new paths to our main list
		paths.extend( new_paths )

		# See if we're done
		if not paths:
			break

		if paths[ 0 ][ -1 ] == node_goal:
			final_path = paths[ 0 ]
			break

	return final_path


def add_adjacent_hex( a_hex, direction, ring_num ):
	global HEXES

	if a_hex.links.get( direction ):
		# Already has adjacent hex
		return

	op_direction = direction + 3
	op_direction = op_direction % 6

	new_hex = Hex( ring_num )
	a_hex.links[ direction ] = new_hex
	new_hex.links[ op_direction ] = a_hex

	# Add other neighbors to new hex
	# One to the left of new_hex, relative to a_hex
	d1 = direction - 1
	d1 = d1 % 6

	if a_hex.links.get( d1 ):
		d2 = op_direction + 1
		d2 = d2 % 6
		new_hex.links[ d2 ] = a_hex.links[ d1 ]

		d3 = d2 + 3
		d3 = d3 % 6
		a_hex.links[ d1 ].links[ d3 ] = new_hex


	# One to the right of new_hex, relative to a_hex
	d1 = direction + 1
	d1 = d1 % 6

	if a_hex.links.get( d1 ):
		d2 = op_direction - 1
		d2 = d2 % 6
		new_hex.links[ d2 ] = a_hex.links[ d1 ]

		d3 = d2 + 3
		d3 = d3 % 6
		a_hex.links[ d1 ].links[ d3 ] = new_hex

	# Add new hex to main list
	HEXES[ new_hex.id ] = new_hex

	return new_hex




if __name__ == '__main__':
	# Read in our data for the path to follow
	data = open( 'input.txt', 'r' ).read( ).strip( ).split( ',' )

	# Start with one hex, then create more and expand in concentric circles
	# as we walk away from it using the input path steps provided.  This
	# leaves us with a board of hexes guaranteed to contain both start and
	# end points, plus the shortest path between them.

	# Create first origin hex
	hex_start = Hex( 0 )
	HEXES[ hex_start.id ] = hex_start

	cur_hex_id = 0
	cur_hex = HEXES[ cur_hex_id ]

	for move_str in data:
		move_dir = STR_TO_DIR[ move_str ]

		hex_dest = cur_hex.links.get( move_dir )

		if not hex_dest:
			# Destination hex needs to be created. Do this by looping over all
			# hexes in current ring, adding new adjacent hexes for each as needed.
			# This effectively expands the board by 1 ring.
			cur_ring_hexes = [ h for h in HEXES.values( ) if h.ring == cur_hex.ring ]

			for a_hex in cur_ring_hexes:
				for direction in range( 6 ):
					add_adjacent_hex( a_hex, direction, cur_hex.ring + 1 )

			hex_dest = cur_hex.links[ move_dir ]

		cur_hex = hex_dest

	# At this point our hex_dest is the final destination hex, and the board is
	# expanded to encompass the shortest path between the origin and dest hexes.
	shortest_path = pathfind( hex_start, hex_dest )

	print( 'shortest path =', shortest_path )
	print( 'length =', len( shortest_path ) )

	print( 'done' )