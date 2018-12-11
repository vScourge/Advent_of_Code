"""
Advent of Code 2017

It would take years to compute the actual final sequence of 1 billion dances.
Fortunately every input results in a cycle that repeats, where every N dances
the sequence is back in its original order.

This finds the cycle N where that repeat happens, then computes the modulus/
remainder of dividing 1 billion by the cycle number, then looking up what the
sequence was at that number when it was first encountered.

input is: input.txt
answer is bfcdeakhijmlgopn

"""

import time


if __name__ == '__main__':
	progs_orig = 'abcdefghijklmnop'
	progs = 'abcdefghijklmnop'

	moves = open( 'input.txt', 'r' ).read( ).strip( ).split( ',' )

	limit = 1000000000
	i = 0

	time_start = time.time( )
	
	all_progs = { }

	while i < limit:
		all_progs[ i ] = progs
		
		if i > 0 and progs == progs_orig:
			i2 = i - 1
			print( 'cycle =', i, 'steps' )

			steps = limit % i
			print( 'answer =', all_progs[ steps ] )
			break
		
			## How many whole cycles it takes, minus remainder
			#steps = limit // i	
			## Now add steps needed to complete remainder
			#steps += ( i * ( limit / 60 - steps ) )
			
			#print( 'answer =', steps )
			#break
			
			
		if i % 100 == 0:
			time_now = time.time( )
			secs = time_now - time_start
			eta_hours = secs * ( limit - i ) / 60.0 / 60.0
			time_start = time_now
			print( '{0:.4f}%, {1}, {2:.2f} secs, eta: {3:.2f} hours'.format( i / limit, i, secs, eta_hours ) )

		for move in moves:
			#ts = time.time( )

			if move.startswith( 's' ):
				# Spin

				pos = int( move[ 1: ] )

				progs = progs[ -pos: ] + progs[ :-pos ]

				#print( 's = {0:.6f}'.format( time.time( ) - ts ) )

			elif move.startswith( 'x' ):
				# Swap by pos
				pos1, pos2 = sorted( [ int( p ) for p in move[ 1: ].split( '/' ) ] )

				progs = progs[ :pos1 ] + progs[ pos2 ] + progs[ pos1+1:pos2 ] + progs[ pos1 ] + progs[ pos2+1: ]

				#print( 'x = {0:.6f}'.format( time.time( ) - ts ) )

			elif move.startswith( 'p' ):
				# Swap by name
				name1, name2 = [ n for n in move[ 1: ].split( '/' ) ]

				progs = progs.replace( name1, 'x' ).replace( name2, name1 ).replace( 'x', name2 )

				#print( 'p = {0:.6f}'.format( time.time( ) - ts ) )

		i += 1

	#print( 'progs =', progs )

	print( 'done' )

