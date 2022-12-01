"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. 
The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. 
Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map 
have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), 
one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points 
are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?


--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, 
although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations 
will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""


import numpy

def parse_input( ):
	data_list = [ ]
	#data = numpy.array( [ ], dtype = numpy.int64 )
	
	for line in open( 'input.txt', 'r' ):
		row = [ int( x ) for x in line.strip( ) ]
		data_list.append( row )
	
	data = numpy.array( data_list, dtype = numpy.int64 )

	# Pad outside of grid with 1 row of -1 values
	data = numpy.pad( data, pad_width = 1, mode = 'constant', constant_values = -1 )	

	return data


def get_higher_adj_points( data, x, y ):
	adj_points = [
	    (x,y-1),
	    (x-1,y),
	    (x+1,y),
	    (x,y+1)
	]

	high_adj_points = [ ]
	val = data[ y, x ]
	
	for point in adj_points:
		adj_val = data[ point[ 1 ], point[ 0 ] ]

		if adj_val != 9 and adj_val > val:
			high_adj_points.append( point )
	               
	return high_adj_points
	
	

def get_basin_points_recurse( data, x, y ):
	basin_points = [ ]
	
	# Add the point we're checking around
	basin_points.append( (x,y) )

	# Now add its adjacent points	
	adj_points = get_higher_adj_points( data, x, y )
	basin_points += list( adj_points )

	# Recurse, for each adjacent points, collect their adjacent points
	for point in adj_points:
		basin_points += get_basin_points_recurse( data, point[ 0 ], point[ 1 ] )

	# remove duplicates and return list
	return list( set( basin_points ) )
	


data = parse_input( )
answer = 0
lowpoints = [ ]

# First find all the lowpoints
for y in range(len( data ) ):
	for x in range( len( data[ y ] ) ):
		val = data[ y ][ x ]

		if val == -1:
			continue
		
		vals_slice = numpy.copy( data[ y-1:y+2, x-1:x+2 ] )

		vals_slice[0,0] = -1
		vals_slice[0,2] = -1
		vals_slice[2,0] = -1
		vals_slice[2,2] = -1
		
		vals = vals_slice.flatten( )

		# Make center value -1 so it gets ignored, since it's the value itself
		vals[ 4 ] = -1
		adj_vals = [ v for v in vals if v != -1 ]
		
		num_adj = len( adj_vals )
		
		higher_adj_vals = [ v for v in adj_vals if v > val ]
		
		if len( adj_vals ) == len( higher_adj_vals ):
			# We found a lowpoint
			#print( 'lowpoint =', val, '({0},{1})'.format( x-1,y-1 ) )
			lowpoints.append( (x,y) )
			
# Now find basin around each lowpoint
basins = [ ]
for lowpoint in lowpoints:
	basin = get_basin_points_recurse( data, lowpoint[ 0 ], lowpoint[ 1 ] )
	basins.append( basin )
	#print( 'foo' )

basin_sizes = [ len( x ) for x in basins ]

basin_sizes.sort( reverse = True )
answer = 1

for i in range( 3 ):
	answer *= basin_sizes[ i ]

print( answer )
	

# 902880