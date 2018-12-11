"""
Advent of Code 2017

input is: uugsqrei

answer is 8194

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


if __name__ == '__main__':
	rows = [ ]
	base_input = 'uugsqrei'
	used_count = 0

	for i in range( 128 ):
		key_str = base_input + '-' + str( i )
		knot_hash = get_knot_hash( key_str )

		bin_str = hex_to_binary( knot_hash )
		used_count += bin_str.count( '1' )

		rows.append( bin_str )

	print( 'total used =', used_count )
	print( 'done' )