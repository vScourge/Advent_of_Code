freq = 0
freqs = [ ]
found = False

while not found:
	for x in open( 'input.txt', 'r' ):
		freq += int( x )
		
		if freq in freqs:
			print( freq )
			found = True
			break
	
		freqs.append( freq )