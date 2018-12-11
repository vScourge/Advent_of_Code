"""
Advent of Code 2017

input is: uugsqrei

answer is 1141

"""


def get_knot_hash( input_str ):
	"""
	Calculates a knot hash based on arbitrary input string
	"""
	suffix = [ 17, 31, 73, 47, 23 ]

	lengths = [ ord( x ) for x in input_str ] + suffix
	data = [ x for x in range( 256 ) ]
	pos = 0
	skip = 0

	for round_num in range( 64 ):
		for length in lengths:
			data2 = data + data

			span = data2[ pos:pos+length ]
			span.reverse( )

			# replace this span in data
			rpos = pos + 0

			for val in span:
				data[ rpos ] = val

				rpos += 1
				if rpos == len( data ):
					rpos = 0

			pos += length + skip
			pos = pos % len( data )

			skip += 1

	dense_hash = [ ]

	for i in range( 16 ):
		start = i * 16
		end = start + 16

		xor = 0

		for num in data[ start:end ]:
			xor = xor ^ num

		dense_hash.append( xor )

	hex_hash = ''

	for num in dense_hash:
		hex_str = hex( num ).split( 'x' )[ 1 ]
		hex_str = '0' + hex_str
		hex_str = hex_str[ -2: ]

		hex_hash += hex_str

	return hex_hash



def hex_to_binary( hex_str ):
	bin_str = ''

	for c in hex_str:
		b = ( '000' + bin( int( c, 16 ) )[ 2: ] )[ -4: ]
		bin_str += b

	return bin_str


def get_adjacent( rows, x, y ):
	"""
	Find all cells like this one, to left and right in a row
	"""


def flood_fill_recurse( rows, x, y ):
	"""
	Given set of rows, and x & y position, find coords of all
	connected elements adjacent to this one, looking in all
	directions
	"""

def flood_fill( data, x, y, old_char, new_char ):
	"""
	The recursive algorithm. Starting at x and y, changes any adjacent
	characters that match old_char to new_char.

	Adapted from:
	http://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/
	"""

	worldWidth = len( data )
	worldHeight = len( data[ 0 ] )

	if old_char == None:
		old_char = data[ y ][ x ]

	if data[ y ][ x ] != old_char:
		# Base case. If the current y, x character is not the old_char,
		# then do nothing.
		return

	# Change the character at data[y][x] to new_char
	data[ y ] = data[ y ][ :x ] + new_char + data[ y ][ x+1: ]
	#data[ y ][ x ] = new_char

	# Recursive calls. Make a recursive call as long as we are not on the
	# boundary (which would cause an Index Error.)
	if x > 0: # left
		flood_fill( data, x - 1, y, old_char, new_char )

	if y > 0: # up
		flood_fill( data, x, y - 1, old_char, new_char )

	if x < worldWidth - 1: # right
		flood_fill( data, x + 1, y, old_char, new_char )

	if y < worldHeight - 1: # down
		flood_fill( data, x, y + 1, old_char, new_char )



if __name__ == '__main__':
	data = [ ]
	base_input = 'uugsqrei'
	used_count = 0

	# Create our data
	# Each string in data list is a row
	# Each char position is a column
	for i in range( 128 ):
		key_str = base_input + '-' + str( i )
		knot_hash = get_knot_hash( key_str )

		bin_str = hex_to_binary( knot_hash )
		used_count += bin_str.count( '1' )

		data.append( bin_str )

	# Find regions
	regions = [ ]

	for y in range( len( data ) ):
		for x in range( len( data[ y ] ) ):
			if data[ y ][ x ] == '1':
				regions.append( ( x, y ) )
				flood_fill( data, x, y, '1', ' ' )


	print( 'total regions =', len( regions ) )
	print( 'done' )