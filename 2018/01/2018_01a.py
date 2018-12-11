freq = 0

for x in open( 'input.txt', 'r' ):
	freq += int( x )
	
print( freq )