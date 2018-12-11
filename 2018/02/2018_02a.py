data = { }

for line in open( 'input.txt', 'r' ):
	line = line.strip( )
	for c in line:
		count = line.count( c )
		
		if line not in data:
			data[ line ] = [ ]
			
		if count not in data[ line ]:
			data[ line ].append( count )

count_2 = 0
count_3 = 0

for line, counts in data.items( ):
	if 2 in counts:
		count_2 += 1
	if 3 in counts:
		count_3 += 1
		
print( count_2 * count_3 )