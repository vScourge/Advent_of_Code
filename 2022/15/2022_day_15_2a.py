"""
Advent of Code 2022
Adam Pletcher
adam.pletcher@gmail.com

--- Day 15: Beacon Exclusion Zone ---
You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You 
don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you 
imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the 
source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button 
on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins 
monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each sensor 
knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on to the 
one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons are 
the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). 
For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3

So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to 
it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its 
closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. 
There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions 
marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress 
beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot 
possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10,
you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that 
row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.

In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain 
a beacon?

--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not
detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger
than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying
its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this
reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for
this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""

import numpy
import sys
import time


class Point2:
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.other = None
		self.distance = 0
		self.points = numpy.array([])
		
	def __repr__(self):
		return '<Point2 ({0},{1})>'.format(self.y, self.x)
	


def get_distance(p1, p2):
	return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def parse_input( ) -> tuple:
	beacons = [ ]
	sensors = [ ]
	
	for line in open('input.txt', 'r'):
		part1, part2 = line.strip().split(':')
		part1a, part1b = part1.split(',')
		sensor = Point2(int(part1b.split('=')[-1]), int(part1a.split('=')[-1]))
		sensors.append(sensor)
		
		part2a, part2b = part2.split(',')
		beacon = Point2(int(part2b.split('=')[-1]), int(part2a.split('=')[-1]))
		beacons.append(beacon)
		
		sensor.other = beacon
		beacon.other = sensor

		distance = get_distance(beacon, sensor)
		sensor.distance = distance
		beacon.distance = distance

	## Make grid of required size, filled with empty char
	#grid = numpy.full((max_y-min_y+1, max_x-min_x+1), fill_value = '.')	
	
	return (sensors, beacons)


def print_grid(grid) -> None:
	print('')
	for row in grid:
		print(''.join(row))

		

if __name__ == '__main__':
	time_start = time.time()
	
	sensors, beacons = parse_input()
	
	# Count the points along a given y/row that a beacon can't exist
	
	# First get the max distances any beacon is from its sensor.
	# This will help us get the largest radius needed to test along our row
	max_dist = max([n.distance for n in beacons])
	min_x = max(min([n.x - n.distance - max_dist for n in sensors]), 0)
	max_x = min(max([n.x + n.distance + max_dist for n in sensors]), 4000000)
	min_y = max(min([n.y - n.distance - max_dist for n in sensors]), 0)
	max_y = min(max([n.y + n.distance + max_dist for n in sensors]), 4000000)

	# For each sensor, build its list of grid spots within its range
	for sensor in sensors:
		for y in range(sensor.y - sensor.distance, sensor.y + sensor.distance):
			for x in range(sensor.x - sensor.distance, sensor.x + sensor.distance):
				if get_distance(sensor, Point2(y, x)) <= sensor.distance:
					numpy.append(sensor.points, (y, x))
	
	#y = 2000000
	grid_points = set()
	points = set()
	occupied = [(p.y, p.x) for p in sensors + beacons]
	c = 1
	last_progress = ''
	
	for y in range(min_y, max_y):
		for x in range(min_x, max_x):
			if (y, x) in occupied:
				continue
			
			progress = '{0:0.5f}%'.format(c / (max_x * max_y) * 100)
			if progress != last_progress:
				print(progress)
				last_progress = progress
				
			c += 1
			
			point = Point2(y, x)
			grid_points.add(point)
			
			for sensor in sensors:
				#print('point = {0}, sensor = {1}, dist = {2}'.format(point, sensor, sensor.distance))
				if get_distance(sensor, point) <= sensor.distance:
					points.add(point)
					break

	open_point = list(grid_points.difference(points))[0]
	answer = open_point.x * 4000000 + open_point.y
	
	print('answer =', answer)
	print('time = {0:0.2f}'.format(time.time() - time_start))

# 5379909 too high