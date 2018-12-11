"""
--- Day 10: The Stars Align ---
It's no use; your navigation system simply isn't capable of providing walking directions in the arctic circle, and certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of light in the sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points move slowly enough that it takes hours to align them, but have so much momentum that they only stay aligned for a second. If you blink at the wrong time, it might be hours before another message appears.

You can see these points of light floating in the distance, and record their position in the sky and their velocity, the relative change in position per second (your puzzle input). The coordinates are all given from your perspective; given enough time, those positions and velocities will move the points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.

For example, suppose you note the following points:

position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
Each line represents one point. Positions are given as <X, Y> pairs: X represents how far left (negative) or right (positive) the point appears, while Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's velocity is added to its position. So, a point with velocity <1, -2> is moving to the right, but is moving upward twice as quickly. If this point's initial position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:

Initially:
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........

After 1 second:
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................

After 2 seconds:
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................

After 3 seconds:
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................

After 4 seconds:
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................
After 3 seconds, the message appeared briefly: HI. Of course, your message will be much longer and will take many more seconds to appear.

What message will eventually appear in the sky?

--- Part Two ---
Good thing you didn't have to wait, because that would have taken a long time - much longer than the 3 seconds in the example above.

Impressed by your sub-hour communication capabilities, the Elves are curious: exactly how many seconds would they have needed to wait for that message to appear?
"""

import sys
import time


### CLASSES ###

class Point( ):
	def __init__( self, x, y, vx, vy ):
		self.sx = x
		self.sy = y
		self.x = x
		self.y = y
		
		self.vx = vx
		self.vy = vy
		
	def __repr__( self ):
		return '<Point ({0},{1})>'.format( self.x, self.y )
	
	
### FUNCTIONS ###

def get_area( bbox ):
	width = bbox[ 2 ] - bbox[ 0 ]
	height = bbox[ 3 ] - bbox[ 1 ]
	
	return width * height


def draw_data( points, bbox ):
	# Arrange points in new list
	# last_bbox = ( min_x, min_y, max_x, max_y )
	
	data = [ ]
	print( '--------------------------------' )
	
	for point in points:
		data.append( ( point.x - bbox[ 0 ], point.y - bbox[ 1 ] ) )
		#data.append( ( point.x, point.y ) )
		
	for y in range( bbox[ 3 ] - bbox[ 1 ] + 2 ):
	#for y in range( bbox[ 3 ] ):
		row = ''
		for x in range( bbox[ 2 ] - bbox[ 0 ] + 2 ):
		#for x in range( bbox[ 2 ] ):
			if ( x, y ) in data:
				row += '*'
			else:
				row += ' '
		print( row )
			
	#print( 'done' )

	
### MAIN ###

if __name__ == "__main__":
	"""
	position=<-30302,  30614> velocity=< 3, -3>
	position=<-20164, -10027> velocity=< 2,  1>
	"""

	points = [ ]
	secs = 0
	
	for line in open( 'input.txt', 'r' ):
		x = int( line[ 10:16 ].strip( ) )
		y = int( line[ 17:24 ].strip( ) )
		vx = int( line[ 36:38 ].strip( ) )
		vy = int( line[ 40:42 ].strip( ) )
		
		points.append( Point( x, y, vx, vy ) )	
	
	# Find average initial pos
	avg_x = sum( [ p.x for p in points ] ) / len( points )
	avg_y = sum( [ p.y for p in points ] ) / len( points )
	
	last_bbox = ( -99999, -99999, 99999, 99999 )
	last_area = sys.maxsize
	last_points = [ ]
	
	while True:
		secs += 1
		
		for point in points:
			point.x += point.vx
			point.y += point.vy
			
		min_x = min( [ p.x for p in points ] )
		min_y = min( [ p.y for p in points ] )
		max_x = max( [ p.x for p in points ] )
		max_y = max( [ p.y for p in points ] )
		
		this_area = get_area( ( min_x, min_y, max_x, max_y ) )
		this_bbox = ( min_x, min_y, max_x, max_y )
		
		if this_area < last_area:
			last_area = this_area
			last_bbox = this_bbox
			last_points = points
			
			print( 'area = {0}, secs = {1}'.format( this_area, secs ) )
			
			if this_area == 549:
				draw_data( last_points, last_bbox )
				break
		#else:
			## We've hit minimum area
			##points = last_points
			##bbox = last_bbox
			#draw_data( last_points, last_bbox )
			#break
		
		
	print( 'done' )