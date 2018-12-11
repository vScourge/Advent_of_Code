"""
qLkKleEZHhTtzGtiITowWOJjlLJkKZzRrQqsvV
"""
import string


def react( line ):
	#print( line )
	
	i = 0
	length = len( line )
	
	while i < length - 1:
		char1 = line[ i ]
		char2 = line[ i+1 ]
		
		if char1.lower( ) != char2.lower( ) or char1 == char2:
			# not a match
			i += 1
		else:
			# match, so both chars are destroyed
			#if len( buf ) > 30790:
				#print( '---\n{0}\n{1}'.format( i, line[ -50: ] ) )

			if i == 0:
				line = line[ 2: ]
			else:
				line = line[ :i ] + line[ i+2: ]
				i -= 1
				
			#if len( buf ) > 30790:
				#print( '{0}\n{1}'.format( i, line[ -50: ] ) )

			length = len( line )

	return line	


### MAIN ###

if __name__ == "__main__":
	orig_line = open( 'input.txt', 'r' ).read( )

	min_length = 50000
	min_line = None
	
	for polymer in string.ascii_lowercase:
		line = orig_line
		
		line = line.replace( polymer, '' ).replace( polymer.upper( ), '' )
		line = react( line )
		
		if len( line )	< min_length:
			min_length = len( line )
			min_line = line
			
	print( min_line )
	print( 'answer = {0}'.format( len( min_line ) ) )
	print( 'done' )