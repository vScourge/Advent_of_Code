"""
Advent of Code 2017

input it input.txt
answer is: 265

"""

valid_count = 0

def has_anagrams( words ):
	words2 = [ ]

	for word in words:
		letters = [ l for l in word ]
		letters.sort( )
		words2.append( ''.join( letters ) )

	return len( words ) > len( set( words2 ) )


for line in open( 'input.txt', 'r' ):
	valid = True

	words = line.strip( ).split( ' ' )

	for word in words:
		if words.count( word ) > 1:
			valid = False
			break

	if valid and has_anagrams( words ):
		valid = False

	if valid:
		valid_count += 1

print( 'valid =', valid_count )