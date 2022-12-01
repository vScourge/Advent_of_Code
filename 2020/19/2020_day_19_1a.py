"""
--- Day 19: Monster Messages ---
You land in an airport surrounded by dense forest. As you walk to your high-speed train, 
the Elves at the Mythical Information Bureau contact you again. They think their satellite 
has collected an image of a sea monster! Unfortunately, the connection to the satellite is 
having problems, and many of the messages sent back from the satellite have been corrupted.

They sent you a list of the rules valid messages should obey and a list of received messages 
they've collected so far (your puzzle input).

The rules for valid messages (the top part of your puzzle input) are numbered and build upon 
each other. For example:

0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

Some rules, like 3: "b", simply match a single character (in this case, b).

The remaining rules list the sub-rules that must be followed; for example, the rule 0: 1 2 means 
that to match rule 0, the text being checked must match rule 1, and the text after the part that 
matched rule 1 must then match rule 2.

Some of the rules have multiple lists of sub-rules separated by a pipe (|). This means that at 
least one list of sub-rules must match. (The ones that match might be different each time the 
rule is encountered.) For example, the rule 2: 1 3 | 3 1 means that to match rule 2, the text 
being checked must match rule 1 followed by rule 3 or it must match rule 3 followed by rule 1.

Fortunately, there are no loops in the rules, so the list of possible matches will be finite. 
Since rule 1 matches a and rule 3 matches b, rule 2 matches either ab or ba. Therefore, rule 0 
matches aab or aba.

Here's a more interesting example:

0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

Here, because rule 4 matches a and rule 5 matches b, rule 2 matches two letters that are the same 
(aa or bb), and rule 3 matches two letters that are different (ab or ba).

Since rule 1 matches rules 2 and 3 once each in either order, it must match two pairs of letters, 
one pair with matching letters and one pair with different letters. This leaves eight possibilities: 
aaab, aaba, bbab, bbba, abaa, abbb, baaa, or babb.

Rule 0, therefore, matches a (rule 4), then any of the eight options from rule 1, then b (rule 5):
aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb.

The received messages (the bottom part of your puzzle input) need to be checked against the rules 
so you can determine which are valid and which are corrupted. Including the rules and the messages 
together, this might look like:

0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb

Your goal is to determine the number of messages that completely match rule 0. In the above example, 
ababbb and abbbab match, but bababa, aaabbb, and aaaabbb do not, producing the answer 2. The whole 
message must match all of rule 0; there can't be extra unmatched characters in the message. (For 
example, aaaabbb might appear to match rule 0 above, but it has an extra unmatched b on the end.)

How many messages completely match rule 0?
"""

### IMPORTS ###

import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'

rules = { }
out = None


### FUNCTIONS ###

def parse_input( ):
	global rules
	
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	messages = [ ]

	for line in lines:
		if line == '':
			continue

		if ':' in line:		
			parts1 = line.split( ' ' )
			id = int( parts1[ 0 ].rstrip( ':' ) )
			
			if '"' in line:
				letter = parts1[ -1 ][ 1 ]
				code = '"{0}".find( "{1}" )'.format( '{msg}', letter )
			
			else:
				parts2 = line.split( ':' )[ 1 ]
				
				for part in parts2.split( '|' ):
					ids = [ int( x ) for x in part.strip( ).split( ' ' ) ]

					code_parts = [ ]

					if len( ids ) == 1:
						code = 'rules[ {0} ]( "{1}" ) > 0'.format( ids[ 0 ], '{msg}' )
					elif len( ids ) == 2:
						code = 'a = rules[ {0} ]( "{1}" );out = a > 0 and rules[ {2} ]( "{1}"[ a+1: ] ) > 0'.format( ids[ 0 ], '{msg}', ids[ 1 ] )
					else:
						raise IOError( 'doh' )
						
			rules[ id ] = Rule( id, code )

		else:
			messages.append( line )
		
	return messages


def main( rules, messages ):
	"""
	# "a"
	'"{0}".find( "{1}" )'
	# 2 3
	'a = rules[ {0} ]( {1} );a and rules[ {0} ]( {1}[ a+1: ] )'
	# 2 3 | 3 2
	'a = rules[ {0} ]( {1} );a != -1 and rules[ {0} ]( {1}[ a+1: ] )'
	
	0: 4 1 5
	1: 2 3 | 3 2
	2: 3
	3: 4 5 | 5 4
	4: "a"
	5: "b"
	"""
	
	total = 0
	
	for message in messages:
		if rules[ 0 ]( message ):
			total += 1
		
	return total
	

### CLASSES ###

class Rule( ):
	def __init__( self, id, code ):
		self.id = id
		self.code = code
		
	def __call__( self, message ):
		global out
		
		code_str = self.code.format( msg = message )
		print( code_str )
		
		if ';' in code_str:
			comp_code = compile( code_str, '', 'exec' )
			exec( comp_code )
			val = out
		else:
			comp_code = compile( code_str, '', 'eval' )
			val = eval( comp_code )

		return val
	              
	def __repr__( self ):
		return '<Rule {0}>'.format( self.id )
	


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	messages = parse_input( )
	answer = main( rules, messages )
	
	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 756 too low
