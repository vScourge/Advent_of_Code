"""
Advent of Code 2017

input is: input.txt
answer1 is 300

"""

import re

regex = re.compile( '<(.*?)>' )


class Particle( ):
	def __init__( self, pos, vel, acc ):
		self.pos = pos
		self.vel = vel
		self.acc = acc

	def simulate( self ):
		self.vel = ( self.vel[0] + self.acc[0], self.vel[1] + self.acc[1], self.vel[2] + self.acc[2] )
		self.pos = ( self.pos[0] + self.vel[0], self.pos[1] + self.vel[1], self.pos[2] + self.vel[2] )

	def get_distance( self ):
		dist = sum( [ abs( z ) for z in self.pos ] )
		return dist


# p=<-11104,1791,5208>, v=<-6,36,-84>, a=<19,-5,-4>

if __name__ == '__main__':
	particles = [ ]

	for line in open( 'input.txt', 'r' ):
		groups = regex.findall( line )

		pos = [ int( x ) for x in groups[ 0 ].split( ',' ) ]
		vel = [ int( x ) for x in groups[ 1 ].split( ',' ) ]
		acc = [ int( x ) for x in groups[ 2 ].split( ',' ) ]

		particles.append( Particle( pos, vel, acc ) )


	for i in range( 5000 ):
		c = 0
		min_part = ( 0, 9999999 )

		for part in particles:
			part.simulate( )
			dist = part.get_distance( )
			#print( dist )

			if dist < min_part[ 1 ]:
				min_part = ( c, dist )

			c += 1

		print( i, min_part )


	print( 'particle with min distance:', min_part )

	print( 'done' )

