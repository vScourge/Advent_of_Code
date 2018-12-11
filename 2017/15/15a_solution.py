"""
Advent of Code 2017

input is:
Generator A starts with 873
Generator B starts with 583

answer is 631

"""


def int_to_binary( int_val ):
	# Convert to binary
	bin_str = str( bin( int_val ) )

	# we need 32 bits so pad it out
	bin_str = ( '0' * 32 + bin_str[ 2: ] )[ -16: ]

	return bin_str



if __name__ == '__main__':

	factor_a = 16807
	factor_b = 48271

	iterations = 40000000

	input_a = 873
	input_b = 583

	#input_a = 65
	#input_b = 8921

	diff_count = 0

	for i in range( iterations ):
		print( '---' )
		#print( 'input_a   =', input_a )
		#print( 'input_b   =', input_b )

		input_a = ( factor_a * input_a ) % 2147483647
		input_b = ( factor_b * input_b ) % 2147483647

		#print( 'val_a     =', input_a )
		#print( 'val_b     =', input_b )

		bin_val_a = int_to_binary( input_a )
		bin_val_b = int_to_binary( input_b )

		print( 'bin_val_a =', bin_val_a )
		print( 'bin_val_b =', bin_val_b )

		if bin_val_a == bin_val_b:
			diff_count += 1

		if i % 10000 == 0:
			print( '{0}/{1} = {2}'.format( i, iterations, diff_count ) )


	print( 'diff_count =', diff_count )

	print( 'done' )

	# 39999369 too high - oops, need to count matches, not differences
	# 631