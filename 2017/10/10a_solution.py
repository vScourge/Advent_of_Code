"""
Advent of Code 2017

input is: "data_input" below


"""

data_input = '147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'
#data_input = '3,4,1,5'

if __name__ == '__main__':
	lengths = [ int( x ) for x in data_input.split( ',' ) ]
	data = [ x for x in range( 256 ) ]
	#data = [ x for x in range( 5 ) ]
	pos = 0
	skip = 0

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

	print( 'answer1 =', data[ 0 ] * data[ 1 ] )
	# 3422 too low

	print( 'done' )