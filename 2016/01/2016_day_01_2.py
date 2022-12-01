"""
You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get -
the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work 
them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, 
follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of 
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the 
destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the d
estination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at 
the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

### IMPORTS ###


### CONSTANTS ###


### FUNCTIONS ###


### CLASSES ###



### MAIN ###

# 1-5 f: vfffff

def update_fdir( fdir, new_dir ):
	if new_dir == 'L':
		fdir -= 1
	elif new_dir == 'R':
		fdir += 1
		
	if fdir < 0:
		fdir = 3
	elif fdir > 3:
		fdir = 0
		
	return fdir

	
if __name__ == "__main__":
	x = y = 0
	fdir = 0
	visited = [ ( 0, 0 ) ]
	
	instructions = open( 'input.txt', 'r' ).read( ).strip( ).split( ', ' )
	
	for inst in instructions:
		new_dir = inst[ 0 ]
		steps = int( inst[ 1: ] )
		
		fdir = update_fdir( fdir, new_dir )
		
		visits = [ ]
		
		if fdir == 0:
			y -= steps
				
		elif fdir == 1:
			x += steps
		elif fdir == 2:
			y += steps
		elif fdir == 3:
			x -= steps
			
		if ( x, y ) in visited:
			break
		else:
			visited.append( ( x, y ) )
			
	dist = abs( x ) + abs( y )
	print( dist )
		
	# 310 too high
	