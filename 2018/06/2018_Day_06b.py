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
			
			distance_sum = 0
			
			for coord2 in coords:
				distance_sum += get_distance( coord, coord2 )
				
			if distance_sum < 10000:
				space[ (x, y) ] = 'A'
		
	rows = [ ]
	for y in range( min_y, max_y ):
		row = ''
		for x in range( min_x, max_x ):
			row += space[ (x, y) ]
		rows.append( row )
	
	for row in rows:
		print( row )
		
	# Count areas
	all_markers = ''.join( rows )

	print( 'answer =', all_markers.count( 'A' ) )
	