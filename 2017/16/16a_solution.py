"""
Advent of Code 2017

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.


input is: input.txt
answer is padheomkgjfnblic

"""



if __name__ == '__main__':
	progs = 'abcdefghijklmnop'

	moves = open( 'input.txt', 'r' ).read( ).strip( ).split( ',' )

	for move in moves:
		if move.startswith( 's' ):
			# Spin
			pos = int( move[ 1: ] )
			progs = progs[ -pos: ] + progs[ :-pos ]

		elif move.startswith( 'x' ):
			# Swap by pos
			move = move[ 1: ]
			pos1, pos2 = sorted( [ int( p ) for p in move.split( '/' ) ] )

			progs = progs[ :pos1 ] + progs[ pos2 ] + progs[ pos1+1:pos2 ] + progs[ pos1 ] + progs[ pos2+1: ]

		elif move.startswith( 'p' ):
			move = move[ 1: ]
			name1, name2 = [ n for n in move.split( '/' ) ]

			progs = progs.replace( name1, 'x' ).replace( name2, name1 ).replace( 'x', name2 )

	print( 'progs =', progs )

	print( 'done' )

