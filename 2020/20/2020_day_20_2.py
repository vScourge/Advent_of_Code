"""
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a 
desert in the distance! Since you have some spare time, you might as well see if there was 
anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small 
images created by the satellite's camera array. The camera array consists of many cameras; 
rather than produce a single square image, they produce many smaller square image tiles that 
need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique 
ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and 
flipped to a random orientation. Your first task is to reassemble the original image by orienting 
the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that 
should line up exactly with its adjacent tiles. All tiles have this border, and the border lines 
up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have 
this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....

For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171

To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. 
If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?


--- Part Two ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###

Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###

Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 
When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you 
might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above 
image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#

Determine how rough the waters are in the sea monsters' habitat by counting the number of # that 
are not part of a sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?

"""

### IMPORTS ###

import math
import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input0.txt'

rules = { }


### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	images = { }
	i = 0
	
	while i < len( lines ):
		line = lines[ i ]
		
		if line == '':
			i += 1
			continue
		
		# Get the ID
		id = int( line.split( ' ' )[ -1 ].rstrip( ':' ) )

		# Get the image data
		rows = [ ]
		i += 1
		
		for y in range( 10 ):
			row = lines[ i+y ]
			rows.append( [ l for l in row ] )
			
		data = numpy.array( rows )
		image = Image( id, data )
		
		images[ id ] = image
		
		i += 10
	
	return images


def align_image_to_another( img1, edge_num, img2 ):
	"""
	img1		= Fixed image
	edge_num	= Int 0-3, indicating which edge to align to
	img2		= Image to align to img1
	"""
	img1_edge = img1.edges[ edge_num ]
	
	# First find the edge on img2 that matches
	found = None
	
	for i in range( 4 ):
		if img1_edge == img2.edges[ i ]:
			found = i
			break
		elif img1_edge == tuple( reversed( img2.edges[ i ] ) ):
			found = -i
			break
		
	if found is None:
		return None
	
	e2 = abs( found )
	e1 = edge_num + 2
	if e1 > 3:
		e1 = e1 - 4

	while e2 != e1:
		img2.rotate_90( )
		e2 -= 1
		if e2 < 0:
			e2 = 3
			
	if found < 0:
		# Also flip it
		if e2 == 0 or e2 == 2:
			img2.flip_x( )
		else:
			img2.flip_y( )
	
	return img2


def main( images ):
	"""
	"""
	# Supplied images dict is our base list of images.
	# Key is image ID, value is Image object
	
	# unplaced_ids is a list of image IDs. As we find where each image goes, we'll remove
	# its ID from the stack list
	unplaced_ids = list( images.keys( ) )
	
	# Make our edges dict
	# Key is tuple of edge data, value is list of image IDs that have that same edge
	all_edges = { }
	
	for image in images.values( ):
		assert len( image.edges ) == 4

		for edge in image.edges:
			# Images can be flipped, so reverse each edge and check those too
			both_edges = [ edge, tuple( reversed( edge ) ) ]
			
			for this_edge in both_edges:
				if this_edge not in all_edges:
					all_edges[ this_edge ] = [ image.id ]
				elif image.id not in all_edges[ this_edge ]:
					all_edges[ this_edge ].append( image.id )
	
	# Find 4 corner images, and edge images
	corner_images = [ ]
	edge_images = [ ]
	
	for image in images.values( ):
		adj_image_ids = [ ]
		
		for edge in image.edges:
			adj_image_ids.extend( [ id for id in all_edges[ edge ] if id != image.id ] )

		image.adjacent = [ images[ id ] for id in adj_image_ids ]
		
		print( image.id, len( adj_image_ids ) )
		
		if len( adj_image_ids ) == 2:
			corner_images.append( image )
			#unplaced_ids.remove( image.id )
		elif len( adj_image_ids ) == 3:
			edge_images.append( image )
			#unplaced_ids.remove( image.id )
			
		# Fill out this image's "adjacent" property, referencing other images
		# that share an edge
		

	# Start building our map.
	# First corner image becomes (0,0) position in upper-left. Find edge images that connect
	# to its right (positive X) until we hit another corner image.
	unplaced_ids.remove( corner_images[ 0 ].id )
	
	print( '\nPlacing border...' )
	
	x = 0
	y = 0
	start_img = corner_images[ 0 ]
	cur_img = corner_images[ 0 ]

	grid = { (0,0): corner_images[ 0 ] }
	print( 'Placed (0,0) = {0}'.format( cur_img ) )
	
	# This piece will dictate the orientation of all the others.
	# We need to orient this first corner piece so it's two connecting edges are facing right and down.

	# Let's find the edge connecting to adj image #1, and rotate cur_image accordingly
	adj_img = cur_img.adjacent[ 0 ]
	
	found = None
	
	for a in range( 4 ):
		for b in range( 4 ):
			if cur_img.edges[ a ] == adj_img.edges[ b ]:
				found = ( a, b )
				break
			elif cur_img.edges[ a ] == tuple( reversed( adj_img.edges[ b ] ) ):
				found = ( a, -b )
				break

		if found:
			break

	# Rotate cur_img if needed, to get connecting edge on right side
	z = found[ 0 ]
	while z != 1:
		cur_img.rotate_90( )
		z -= 1
		if z < 0:
			z = 3

	# Next let's find the edge connecting to adj image #2, and flip cur_image accordingly if needed
	adj_img = cur_img.adjacent[ 1 ]
	
	found = None
	
	for a in range( 4 ):
		for b in range( 4 ):
			if cur_img.edges[ a ] == adj_img.edges[ b ]:
				found = ( a, b )
				break
			elif cur_img.edges[ a ] == tuple( reversed( adj_img.edges[ b ] ) ):
				found = ( a, -b )
				break

		if found:
			break

	# Flip cur_img along y if needed, to get connecting edge on bottom side
	if found[ 0 ] == 0:
		cur_img.flip_y( )
			
	# Now that upper-left corner is placed and oriented,	
	# Walk around our border, placing matching pieces as we go.
	dirs = (
	    (1,0),
	    (0,1),
	    (-1,0),
	    (0,-1)
	)
	
	for dir in dirs:
		while True:
			# Increment coords along direction we're moving
			x += dir[ 0 ]
			y += dir[ 1 ]

			if len( grid ) == len( edge_images ) + 4:
				# All corners & edges placed
				break
			
			adj_img = [ i for i in cur_img.adjacent if i in edge_images + corner_images and i.id in unplaced_ids ][ 0 ]
	
			# Place it on grid
			grid[ (x,y) ] = adj_img
			unplaced_ids.remove( adj_img.id )
			
			assert len( grid ) + len( unplaced_ids ) == len( images )
			
			print( 'Placed ({0},{1}) = {2}'.format( x, y, adj_img ) )
			
			if adj_img in corner_images:
				print( '  ^ corner' )

			# Make sure the newly-placed image is oriented correctly
			edge_num = dirs.index( dir ) + 1
			if edge_num == 4:
				edge_num = 0
				
			adj_img = align_image_to_another( cur_img, edge_num, adj_img )

			cur_img = adj_img

			if cur_img in corner_images:
				break
	
	# We have our entire border placed, so now place the interior images
	# starting in the upper-left corner
	x = 1
	y = 1
	
	max_x = max( [ c[ 0 ] for c in grid ] )
	max_y = max( [ c[ 1 ] for c in grid ] )
	
	print( '\nPlacing interior...' )
	
	for y in range( 1, max_y ):
		for x in range( 1, max_x ):
			cur_pos = ( x, y )
			
			# Find the image that's adjacent to both spots above and to the left of this grid position.
			# That's the only one that will fit at this position.
			cur_img = [ i for i in images.values( ) if i.id in unplaced_ids and grid[ ( x, y-1 ) ] in i.adjacent and grid[ ( x-1, y ) ] in i.adjacent ][ 0 ]
			
			# This is the correct image, but might need to be flipped/rotated to line up its pixels correctly.
			# Align it to the already-placed image to its left
			adj_img = grid[ (x-1, y) ]
			
			aligned_img = align_image_to_another( adj_img, 1, cur_img )

			if aligned_img is None:
				# Try the other orientation
				aligned_img = align_image_to_another( adj_img, 2, cur_img )
				
			cur_img = aligned_img
			
			grid[ cur_pos ] = cur_img
			unplaced_ids.remove( cur_img.id )
			
			print( 'Placed ({0},{1}) = {2}'.format( x, y, cur_img ) )



			
	# Now we have our full grid of arranged images.
	# Create a new array of pixels for the entire image, without the borders
	i_grid = numpy.array( [ ] )
	
	for i_y in range( max_y + 1 ):
		for p_y in range( 1, 9 ):
			row = ''
			for i_x in range( max_x + 1 ):
				img = grid[ (i_x, i_y) ]
				pixels = ''.join( img.data[ p_y ][ 1:-1 ] )
				print( pixels )
				row += pixels
				
			i_grid = numpy.append( i_grid, row )
	

	print( 'break' )
	
	return answer
	
"""
1951    2311    3079
2729    1427    2473
2971    1489    1171

1951	2729	2971
2311	1427	1489
3079	2473	1171
"""

### CLASSES ###

class Image( ):
	def __init__( self, id, data ):
		self.id = id
		self.data = data
		self.edges = self.get_edges( )
		self.adjacent = [ ]
		
	def get_edges( self ):
		edges = [ ]

		edges.append( tuple( self.data[ 0 ] ) )							# top
		edges.append( tuple( self.data[ 0:10, 9:10 ].flatten( ) ) )		# right
		
		#edges.append( tuple( self.data[ 9 ] ) )							# bottom
		#edges.append( tuple( self.data[ 0:10, 0:1 ].flatten( ) ) )		# left

		temp = tuple( reversed( self.data[ 9 ] ) )
		edges.append( temp )											# bottom
		temp = tuple( reversed( self.data[ 0:10, 0:1 ].flatten( ) ) )
		edges.append( temp )											# left
		
		return edges
		
		
	def rotate_90( self ):
		self.data = numpy.rot90( self.data )
		self.edges = self.get_edges( )
		
	def flip_x( self ):
		self.data = numpy.flip( self.data, axis = 1 )
		self.edges = self.get_edges( )
		
	def flip_y( self ):
		self.data = numpy.flip( self.data, axis = 0 )
		self.edges = self.get_edges( )
		
	def __repr__( self ):
		return '<Image {0}>'.format( self.id )
	


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	images = parse_input( )
	answer = main( images )
	
	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 17250897231301
