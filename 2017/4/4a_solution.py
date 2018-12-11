"""
Advent of Code 2017

input it input.txt
Answer is: 383

"""

valid_count = 0

for line in open( 'input.txt', 'r' ):
	valid = True

	words = line.strip( ).split( ' ' )

	for word in words:
		if words.count( word ) > 1:
			valid = False
			break

	if valid:
		valid_count += 1

print( 'valid =', valid_count )