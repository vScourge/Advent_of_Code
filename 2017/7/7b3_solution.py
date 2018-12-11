"""
Advent of Code 2017

input is: input.txt

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could get down,
if they weren't expending all of their energy trying to keep the tower balanced. Apparently,
one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower.
Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced.
The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl
must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs
above it must each match. This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even
though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units
lighter for its stack to weigh 243 and keep the towers balanced. If this change were made,
its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to
balance the entire tower?


answer is
"""

PROGS = { }


class Program( ):
	def __init__( self, name, weight, above_names = None ):
		if not above_names:
			above_names = [ ]

		self.name = name
		self.weight = weight
		self.above = [ ]
		self.above_names = above_names
		self.below = None
		self.siblings = [ ]


	def __lt__( self, other ):
		return self.name < other.name


	def __repr__( self ):
		return '<Program "{0}">'.format( self.name )


def get_weight_recurse( prog ):
	weight = int( prog.weight )

	for above_prog in prog.above:
		weight += get_weight_recurse( above_prog )

	return weight



if __name__ == '__main__':
	PROGS = { }

	# Create initial program objects
	for line in open( 'input.txt', 'r' ):
		name = line.split( ' ' )[ 0 ]
		weight = int( line.split('(' )[ 1 ].split( ')' )[ 0 ] )

		if '->' in line:
			above_names = [ c.strip( ) for c in line.split( '>' )[ -1 ].split( ',' ) ]
		else:
			above_names = [ ]

		prog = Program( name, weight, above_names = above_names )

		PROGS[ name ] = prog

	# Assign above/below progs to all progs that have them
	for prog in PROGS.values( ):
		for above_name in prog.above_names:
			above_prog = PROGS[ above_name ]
			prog.above.append( above_prog )
			above_prog.below = prog

	# Now assign siblings
	for prog in PROGS.values( ):
		siblings = [ p for p in PROGS.values( ) if p != prog and p.below == prog.below ]
		prog.siblings = siblings

	# Now find the one program with no parent
	bottom_prog = [ p for p in PROGS if not PROGS[ p ].below ][ 0 ]

	# Now go through all programs from top to bottom, and compare weights across
	# siblings at each level.  When a level is found with programs of different
	# weights, we've found our culprit.
	done_progs = [ ]

	for prog in sorted( list( PROGS.values( ) ) ):
		if prog in done_progs:
			continue

		#weights = [ p.weight for p in prog.siblings ]
		weights = [ get_weight_recurse( p ) for p in prog.siblings ]
		weights.append( get_weight_recurse( prog ) )

		weights_unique = list( set( weights ) )

		if len( weights_unique ) > 1:
			# A program at this level is imbalanced
			if weights.count( weights_unique[ 0 ] ) > 1:
				pass
				#print( '1prog {0}, weight ='.format( prog.name ), weights_unique[ 0 ], weights )
			else:
				# This is the one we care about.
				print( '2prog {0}, weight ='.format( prog.name ), weights_unique[ 1 ], weights )

			print( 'imbalance' )

		done_progs.append( prog )
		done_progs.extend( prog.siblings )


print( 'done' )