"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging
so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.

Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open 
it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes 
instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5

The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, 
increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the 
coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper 
and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold 
the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is 
fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is 
complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........

Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, 
those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the 
result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....

Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....

The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example 
above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?

--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
"""

import collections
import string
import sys
import numpy


def parse_input( ):
	coords = [ ]
	folds = [ ]
	
	for line in open( 'input.txt', 'r' ):
		line = line.strip( )
		
		if line == '':
			continue
		
		if line.startswith( 'f' ):
			temp = line.split( ' ' )[ -1 ]
			fold_data = list( temp.split( '=' ) )
			fold_data[ 1 ] = int( fold_data[ 1 ] )
			folds.append( fold_data )
		else:
			coords.append( tuple( [ int( x ) for x in line.split( ',' ) ] ) )
			

	# Find the max x and y, so we can make our array that size
	max_x = max( [ c[ 0 ] for c in coords ] )
	max_y = max( [ c[ 1 ] for c in coords ] )
	
	## Make sure we have an odd number of rows & columns
	#if max_x % 2 == 0:
		#max_x += 1
	#if max_y % 2 == 0:
		#max_y += 1
	
	data = numpy.array( [ ], dtype = numpy.int32 )
	
	for y in range( max_y + 1 ):
		row = [ ]
		
		for x in range( max_x + 1 ):
			coord = ( x, y )
			if coord in coords:
				row.append( 1 )
			else:
				row.append( 0 )
				
		data = numpy.append( data, row )
		
	data = numpy.reshape( data, ( max_y+1, max_x+1 ) )
	
	return ( data, folds )


def print_data( data ):
	for row in data:
		row_str = ''
		for val in row:
			if val:
				row_str += '#'
			else:
				row_str += '.'
	
		print( row_str )


data, folds = parse_input( )

#print( '\noriginal ---' )
#print_data( data )
c = 0

for fold in folds:
	c += 1
	axis, point = fold

	# Make a copy of the right/bottom side of the fold
	if axis == 'y':
		data2 = numpy.copy( data[ point+1:, 0:len(data[0] ) ] )
	else:
		data2 = numpy.copy( data[ 0:len(data[0]), point+1: ] )

	#print( '' )
	#print( 'fold: {0}'.format( fold ) )
	#print_data( data2 )

	# "cut" that part out of the original data 
	if axis == 'y':
		data = data[ 0:point, 0:len(data[ 0 ]) ]
	else:
		data = data[ 0:len(data), 0:point ]

	#print( '\ncut data:' )
	#print_data( data )

	#print( '\nunpadded data2:' )
	#print_data( data2 )
	
	assert len( data2 ) <= len( data )
	assert len( data2[ 0 ] ) <= len( data[ 0 ] )
	
	# If data and data2 aren't same shape, insert a row or column of zeroes
	if axis == 'y':
		if len( data2 ) < len( data ):
			vals = [ 0 for i in range( len( data[ 0 ] ) ) ]
			
			while len( data2 ) < len( data ):
				data2 = numpy.insert( data2, len( data2 ), vals, axis = 0 )
	else:
		if len( data2[ 0 ] ) < len( data[ 0 ] ):
			vals = [ 0 for i in range( len( data ) ) ]
	
			while len( data2[ 0 ] ) < len( data[ 0 ] ):
				data2 = numpy.insert( data2, len( data2[ 0 ] ), vals, axis = 1 )
		
	#print( '\npadded data2:' )
	#print_data( data2 )

	# Flip the right/bottom part of fold
	if axis == 'y':
		a = 0
	else:
		a = 1
		
	data2 = numpy.flip( data2, a )
				
	# Overlay, so the dots from data2 are now in data
	for y in range( len( data ) ):
		for x in range( len( data[ 0 ] ) ):
			if data2[ y,x ]:
				data[ y,x ] = 1

	print( '\nfold', c, '----' )
	print_data( data )
	
	## Return data after just the first fold
	#print( numpy.count_nonzero( data ) )
	#break

#print_data( data )
print( '\ndone!' )

# ZKAUCFUC
