"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of 
the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different 
rules overlap.

jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""

### IMPORTS ###

import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'


### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )
	return lines

def main( lines ):
	vowels = ( 'a', 'e', 'i', 'o', 'u' )
	combos = ( 'ab', 'cd', 'pq', 'xy' )
	nice = 0
		
	for line in lines:
		vowel_count = [ x in vowels for x in line ].count( True )

		if vowel_count < 3:
			continue
		
		good = True
		
		for combo in combos:
			if combo in line:
				good = False
				break
		
		if not good:
			continue
			
		good = False
		
		for i in range( len( line ) - 1 ):
			if line[ i ] == line[ i+1 ]:
				nice += 1
				print( line )
				break
	
	return nice

### CLASSES ###


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	lines = parse_input( )
	answer = main( lines )

	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 253 too high
