"""
Advent of Code 2017

input is
11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11

answer is 4074
"""

input_str = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'
banks = [ int( x ) for x in input_str.split( '\t' ) ]
configs = [ ]

done = False
c = 0

while not done:
	c += 1

	print( '{0} - {1}'.format( c, ' '.join( [ str( x ) for x in banks ] ) ) )

	# Get index of first bank with highest # of blocks
	num_blocks = max( banks )
	cur_idx = banks.index( num_blocks )

	# How many blocks to distribute to each bank
	dist_amt = len( banks ) // num_blocks

	# zero out current one
	banks[ cur_idx ] = 0

	# Distribute
	for i in range( num_blocks ):
		cur_idx += 1

		if cur_idx > len( banks ) - 1:
			# Wrap around
			cur_idx = 0

		banks[ cur_idx ] += dist_amt

	# Done distributing, see if this config has been seen before
	banks_tuple = tuple( banks )

	if banks_tuple in configs:
		print( 'Answer =', c )
		done = True
	else:
		configs.append( banks_tuple )