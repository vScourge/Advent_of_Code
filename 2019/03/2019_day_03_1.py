"""
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""

### CONSTANTS ###


### FUNCTIONS ###

def get_distance( p1, p2 ):
	return abs( p1.x - p2.x ) + abs( p1.y - p2.y )


### CLASSES ###

class Point2( ):
	def __init__( self, x, y ):
		self.x = x
		self.y = y


class Wire( ):
	def __init__( self ):
		self.pos = Point2( 0, 0 )
		self.path = [ ( 0, 0 ) ]

	def build_path( self, directions ):
		for data in directions:
			c = data[ 0 ]
			dist = int( data[ 1: ] )
			
			if c == 'U':
				for i in range( dist ):
					self.pos.y -= 1
					self.path.append( ( self.pos.x, self.pos.y ) )
			elif c == 'D':
				for i in range( dist ):
					self.pos.y += 1
					self.path.append( ( self.pos.x, self.pos.y ) )
			elif c == 'L':
				for i in range( dist ):
					self.pos.x -= 1
					self.path.append( ( self.pos.x, self.pos.y ) )
			elif c == 'R':
				for i in range( dist ):
					self.pos.x += 1
					self.path.append( ( self.pos.x, self.pos.y ) )

### MAIN ###

if __name__ == "__main__":
	data = open( 'input.txt', 'r' ).readlines( )

	wire1 = Wire( )
	wire1.build_path( data[ 0 ].split( ',' ) )
	wire2 = Wire( )
	wire2.build_path( data[ 1 ].split( ',' ) )
	
	shortest_dist = 99999999
	origin = Point2( 0, 0 )
	
	c = 0
	
	for coord1 in wire1.path:
		print( '{0} of {1}'.format( c, len( wire1.path ) ) )
		c += 1
		
		if coord1 == ( 0, 0 ) or coord1 not in wire2.path:
			continue
		
		dist = get_distance( origin, Point2( coord1[ 0 ], coord1[ 1 ] ) )
		
		if dist < shortest_dist:
			shortest_dist = dist
			
	print( 'Shortest dist =', shortest_dist )
	
# Answer 768