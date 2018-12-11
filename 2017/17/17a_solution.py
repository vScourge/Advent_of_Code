"""
Advent of Code 2017

input is: 366
answer is 

"""



if __name__ == '__main__':
	buf = [ 0 ]
	steps = 366
	#steps = 3
	
	i = 0
	pos = 0
	
	for i in range( 2017 ):
		# move forward N steps
		for s in range( steps ):
			pos += 1
			if pos >= len( buf ):
				pos = 0
				
		# Insert new value
		buf.insert( pos + 1, i + 1 )
		pos = pos + 1
		
		#print( buf )
		

	print( buf[ pos-5:pos+5 ] )
	print( 'answer =', buf[ pos + 1 ] )
	print( 'done' )

	# 261 too low