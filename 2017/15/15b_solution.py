"""
Advent of Code 2017

input is:
Generator A starts with 873, only produces multiples of 4
Generator B starts with 583, only produces multiples of 8

answer is 279

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

	pairs_needed = 5000000

	input_a = 873
	input_b = 583

	#input_a = 65
	#input_b = 8921

	diff_count = 0

	pairs = [ ]

	while len( pairs ) < pairs_needed:
		#print( '---' )
		#print( 'input_a   =', input_a )
		#print( 'input_b   =', input_b )

		generated_a = None
		generated_b = None

		while not generated_a:
			input_a = ( factor_a * input_a ) % 2147483647

			if input_a % 4 == 0:
				generated_a = input_a

		while not generated_b:
			input_b = ( factor_b * input_b ) % 2147483647

			if input_b % 8 == 0:
				generated_b = input_b

		#print( 'gen_a     =', generated_a )
		#print( 'gen_b     =', generated_b )

		bin_val_a = int_to_binary( generated_a )
		bin_val_b = int_to_binary( generated_b )

		pairs.append( ( bin_val_a, bin_val_b ) )

		#print( 'bin_val_a =', bin_val_a )
		#print( 'bin_val_b =', bin_val_b )

		if bin_val_a == bin_val_b:
			diff_count += 1

		if len( pairs ) % 10000 == 0:
			print( '{0}/{1} = {2}'.format( len( pairs ), pairs_needed, diff_count ) )


	print( 'diff_count =', diff_count )

	print( 'done' )

	# 39999369 too high - oops, need to count matches, not differences
	# 631