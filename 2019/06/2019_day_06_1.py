"""
--- Day 6: Universal Orbit Map ---
You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA (drawn with lines) is only partly shown. In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses orbit count checksums - the total number of direct orbits (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?
"""


### CONSTANTS ###


### FUNCTIONS ###


### CLASSES ###

class Body( ):
	def __init__( self, name, orbits, orbited_by = None ):
		self.name = name
		self.orbits = orbits
		self.orbited_by = orbited_by

	def __repr__( self ):
		return '<Body object "{0}">'.format( self.name )


### MAIN ###

if __name__ == "__main__":
	root = Body( 'COM', None )
	bodies = { 'COM': root }

	for line in open( 'input.txt', 'r' ):
		name1, name2 = line.strip( ).split( ')' )

		body = Body( name2, name1 )
		bodies[ name2 ] = body

	# Replace orbits name with actual reference, and add backreferences
	for name, body in bodies.items( ):
		if body.orbits:
			host_body = bodies[ body.orbits ]
			body.orbits = host_body

			if host_body.orbited_by:
				host_body.orbited_by.append( body )
			else:
				host_body.orbited_by = [ body ]

	# Count how many indirect orbites we have
	num_orbits = 0

	for body in bodies.values( ):
		cur_body = body
		count = 0

		while cur_body.orbits:
			count += 1
			cur_body = cur_body.orbits

		if count > 0:
			num_orbits += count

	direct_orbits = len( bodies ) - 1 	# Don't count COM

	print( 'total =', num_orbits )
	print( 'DONE' )


