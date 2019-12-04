"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""

### CONSTANTS ###

temp_min, temp_max = '236491-713787'.split( '-' )
R_MIN = [ int( i ) for i in temp_min ]
R_MAX = [ int( i ) for i in temp_max ]


### FUNCTIONS ###

def get_groups( data ):
	# Keys are the digits, values are length of each group
	groups = { }
	i = 0
	
	while True:
		if data[ i ] == data[ i+1 ]:
			if data[ i ] not in groups:
				groups[ data[ i ] ] = 2
			else:
				groups[ data[ i ] ] += 1
				
		i += 1
		if i == len( data ) - 1:
			break

	return groups		
	
	
def validate_password( data ):
	if sorted( data ) != data:
		# Values don't increase left-to-right
		return False
	
	if len( set( data ) ) == len( data ):
		# no two values are the same
		return False
		
	groups = get_groups( data )
	
	if not groups:
		# Must have at least one group
		return False
		
	if len( groups ) == 1 and list( groups.values( ) )[ 0 ] == 2:
		# Has only one group, and that group has exactly 2 digits
		return True
	
	if len( groups ) > 1 and 2 in groups.values( ):
		# Has more than one group, and at least one of them has exactly 2 digits
		return True

	return False


def increase_value( data ):
	val = int( ''.join( [ str( i ) for i in data ] ) )
	val += 1
	data = ( [ 0, 0, 0, 0, 0, 0 ] + [ int( i ) for i in str( val ) ] )[ -6: ]

	return data
		

### CLASSES ###


### MAIN ###

if __name__ == "__main__":
	valid_count = 0
	
	data = list( R_MIN )
	
	while True:
		if validate_password( data ):
			valid_count += 1
			
		if data == R_MAX:
			break

		data = increase_value( data )

	print( 'Valid passwords =', valid_count )
	
# Answer 757