"""
Advent of Code 2017

input it input.txt
answer is 25608480
"""

offsets = open( 'input.txt', 'r' ).read( ).split( '\n' )
offsets = [ int( o ) for o in offsets ]
print( 'len offsets =', len( offsets ) )

i = 0
steps = 0

while i < len( offsets ):
	steps += 1

	print( steps, i, offsets[ :10 ] )

	old_i = int( i )

	i += offsets[ i ]

	# Increment this last offset by 1
	if offsets[ old_i ] >= 3:
		offsets[ old_i ] -= 1
	else:
		offsets[ old_i ] += 1


print( 'steps =', steps )
print( 'done' )
