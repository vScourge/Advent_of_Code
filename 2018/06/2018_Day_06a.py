"""
qLkKleEZHhTtzGtiITowWOJjlLJkKZzRrQqsvV
"""

import string

### CLASSES ###

class Point( ):
	def __init__( self, x, y ):
		self.x = x
		self.y = y
		
	def __repr__( self ):
		return '<Point ({0},{1})>'.format( self.x, self.y )
		

### FUNCTIONS ###

def get_distance( point1, point2 ):
	return abs( point1.x - point2.x ) + abs( point1.y - point2.y )

def get_nearest_coords( point1, coords ):
	nearest_coords = [ ]
	nearest_dist = 99999

	for coord in coords:
		if point1 == coord:
			continue
		
		this_dist = get_distance( point1, coord )

		if this_dist < nearest_dist:
			nearest_dist = this_dist
			nearest_coords = [ coord ]
		elif this_dist == nearest_dist:
			nearest_coords.append( coord )
			
	return nearest_coords
	

### MAIN ###

if __name__ == "__main__":
	coords = [ ]
	
	# read input
	for line in open( 'input.txt', 'r' ):
		chars = line.strip( ).replace( ',', '' ).split( ' ' )
		coord = Point( int( chars[ 0 ] ), int( chars[ 1 ] ) )
		coords.append( coord )
	
	# figure size of space
	min_x = min( [ c.x for c in coords ] ) - 10
	min_y = min( [ c.y for c in coords ] ) - 10
	max_x = max( [ c.x for c in coords ] ) + 10
	max_y = max( [ c.y for c in coords ] ) + 10
	
	space = { }
	
	for y in range( min_y, max_y ):
		for x in range( min_x, max_x ):
			space[ (x, y) ] = '.'
	
	# Start marking map coords
	for y in range( min_y, max_y ):
		for x in range( min_x, max_x ):
			coord = Point(x, y)
			nearest_coords = get_nearest_coords( coord, coords )
			
			if len( nearest_coords ) > 1:
				continue
	
			marker = string.ascii_letters[ coords.index( nearest_coords[ 0 ] ) ]
			space[ (x, y) ] = marker
		
	max_area = 0
	buf = ''
	
	rows = [ ]
	for y in range( min_y, max_y ):
		row = ''
		for x in range( min_x, max_x ):
			row += space[ (x, y) ]
		rows.append( row )
	
	# Build set of letters to ignore
	ignore = set( )

	for x in rows[ 0 ]:
		ignore.add( x )
	for x in rows[ -1 ]:
		ignore.add( x )

	for row in rows:
		ignore.add( row[ 0 ] )
		ignore.add( row[ -1 ] )
		#print( row )
		
	ignore.remove( '.' )
	
	# Count areas
	all_markers = ''.join( rows ).replace( '.', '' )
	for marker in list( ignore ):
		all_markers = all_markers.replace( marker, '' )
		
	max_area = 0
	max_marker = None
	
	for marker in string.ascii_letters[ :50 ]:
		count = all_markers.count( marker )
		if count > max_area:
			max_area = count
			max_marker = marker
	
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