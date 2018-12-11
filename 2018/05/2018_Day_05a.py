"""
qLkKleEZHhTtzGtiITowWOJjlLJkKZzRrQqsvV
"""




### MAIN ###

if __name__ == "__main__":
	line = open( 'input.txt', 'r' ).read( )
	
	print( line )
	
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
	
	print( line )
	print( 'answer = {0}'.format( len( line ) ) )
	print( 'done' )