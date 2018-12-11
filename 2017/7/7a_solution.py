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

answer is cyrupz
"""

class Program( ):
	def __init__( self, name, above = None, below = None ):
		if not above:
			above = [ ]
			
		self.name = name
		self.above = above
		self.below = below
		

if __name__ == '__main__':
	progs = { }
	
	for line in open( 'input.txt', 'r' ):
		name = line.split( ' ' )[ 0 ]
		
		if '->' in line:
			above = [ c.strip( ) for c in line.split( '>' )[ -1 ].split( ',' ) ]
		else:
			above = [ ]
			
		prog = Program( name, above = above )
		
		progs[ name ] = prog
		
	# Assign parent to all progs that have one
	for prog in progs.values( ):
		for above_name in prog.above:
			above_prog = progs[ above_name ]
			above_prog.below = prog.name
	
	# Now find the one program with no parent
	parentless = [ p for p in progs if not progs[ p ].below ]
	
	print( 'parentless =', parentless )