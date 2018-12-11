"""
Advent of Code 2017

input is: "data_input" below

answer is:
70b856a24d586194331398c7fcfa0aaf

"""

data_input = '147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'
#data_input = '3,4,1,5'

suffix = [ 17, 31, 73, 47, 23 ]

if __name__ == '__main__':
	lengths = [ ord( x ) for x in data_input ] + suffix
	data = [ x for x in range( 256 ) ]
	#data = [ x for x in range( 5 ) ]
	pos = 0
	skip = 0

	for round_num in range( 64 ):
		print( '---\nRound =', round_num + 1 )

		for length in lengths:
			print( '---\ndata1 =', data )
			data2 = data + data

			span = data2[ pos:pos+length ]
			print( 'span1 =', span )

			span.reverse( )
			print( 'span2 =', span )

			# replace this span in data
			rpos = pos + 0

			for val in span:
				data[ rpos ] = val

				rpos += 1
				if rpos == len( data ):
					rpos = 0

			pos += length + skip

			pos = pos % len( data )
			#if pos >= len( data ):
				#pos = len( data ) - pos

			skip += 1
			print( 'data2 =', data )


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


	print( 'answer2 =', hex_hash )
	# 3422 too low

	print( 'done' )