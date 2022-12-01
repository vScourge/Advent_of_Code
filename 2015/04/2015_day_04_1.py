"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle answer was 346386.

--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle answer was 9958218.
"""

### IMPORTS ###

import hashlib
import time


### CONSTANTS ###

#INPUT_FILENAME = 'input.txt'


### FUNCTIONS ###

#def parse_input( ):
	#lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

def main( secret_key, num_zeroes ):
	i = 0
	
	while True:
		md5 = hashlib.md5( )
		i_str = bytes( secret_key + str( i ), encoding = 'utf-8' )
		md5.update( i_str )
		
		if md5.hexdigest( ).startswith( '0' * num_zeroes ):
			return i
	
		i += 1
	

### CLASSES ###


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	#grid = parse_input( )
	secret_key = 'iwrupvqb'

	answer = main( secret_key, 5 )
	print( 'answer1 =', answer )
	answer = main( secret_key, 6 )
	print( 'answer2 =', answer )
	
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 2136
