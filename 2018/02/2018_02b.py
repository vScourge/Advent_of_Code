boxes = [ ]
c = 0

for line in open( 'input.txt', 'r' ):
	line = line.strip( )
	
	if c == 0:
		boxes.append( line )
		c += 1
		continue
	
	for old_line in boxes:
		diffs = 0
		for i in range( len( old_line ) ):
			if old_line[ i ] != line[ i ]:
				diffs += 1
				same_char = old_line[ i ]
		
		#print( ---\n{0}\n{1}\n{2}'.format( ol'diffs )
		if diffs == 1:
			print( old_line.replace( same_char, '' ) )
			exit( 0 )

	boxes.append( line )
	c += 1