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
"""

### IMPORTS ###

import math
import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'

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


def main( images ):
	"""
	"""
	# edges dict key is tuple of edge data, value is list of image IDs that have that same edge
	all_edges = { }
	
	for image in images.values( ):
		assert len( image.edges ) == 4

		for edge in image.edges:
			both_edges = [ edge, tuple( reversed( edge ) ) ]
			
			for this_edge in both_edges:
				if this_edge not in all_edges:
					all_edges[ this_edge ] = [ image.id ]
				elif image.id not in all_edges[ this_edge ]:
					all_edges[ this_edge ].append( image.id )
			
	corner_images = [ ]
	
	for image in images.values( ):
		matching_edges = [ ]
		
		for edge in image.edges:
			if edge in all_edges:
				matching_edges.extend( [ id for id in all_edges[ edge ] if id != image.id ] )

		print( image.id, len( matching_edges ) )
		
		if len( matching_edges ) == 2:
			corner_images.append( image )	

	answer = 1
	for image in corner_images:
		answer *= image.id
		
	return answer
	

### CLASSES ###

class Image( ):
	def __init__( self, id, data ):
		self.id = id
		self.data = data
		self.edges = self.get_edges( )
		
	def get_edges( self ):
		edges = [ ]

		edges.append( tuple( self.data[ 0 ] ) )				# top
		edges.append( tuple( self.data[ 0:10, 9:10 ].flatten( ) ) )		# right
		edges.append( tuple( self.data[ 9 ] ) )				# bottom
		edges.append( tuple( self.data[ 0:10, 0:1 ].flatten( ) ) )		# left
		
		return edges
		
              
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
