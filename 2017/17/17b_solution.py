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
	
	for i in range( 50000000 ):
		#if i % 100000 == 0:
			#print( i )
			
		# move forward N steps
		for s in range( steps ):
			pos += 1
			if pos >= len( buf ):
				pos = 0
				
		# Insert new value
		buf.insert( pos + 1, i + 1 )
		if pos+1 == 1:
			print( i, buf[ 1 ] )
			
		pos = pos + 1

				
		#print( buf )
		

	print( buf[ :10 ] )
	print( 'answer =', buf[ 1 ] )
	print( 'done' )

	# 261 too low