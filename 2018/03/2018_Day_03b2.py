#3 @ 584,823: 22x10

import pickle

data = set( [ ] )
doubled_all = pickle.load( open( 'doubled.txt','rb' ) )


count = 0

for line in open( 'input.txt', 'r' ):
	line = line.strip( )
	#print( line )

	stuff1 = line.split( '@' )[ 1 ].strip( )
	stuff2 = stuff1.split( ':' )

	stuff3 = stuff2[ 0 ].split( ',' )
	x = int( stuff3[ 0 ] )
	y = int( stuff3[ 1 ] )

	stuff4 = stuff2[ 1 ].split( 'x' )
	w = int( stuff4[ 0 ] )
	h = int( stuff4[ 1 ] )

	#print( x,y,w,h )
	overlap = False

	for h1 in range( h ):
		for w1 in range( w ):
			x1 = x + w1
			y1 = y + h1

			if (x1,y1) in doubled_all:
				overlap = True

	if not overlap:
		print( line )

print( count )