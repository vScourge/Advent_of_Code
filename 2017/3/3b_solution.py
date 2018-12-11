"""
Advent of Code 2017

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

Input was:
368078

Answer is:
65, (-4, -4) =
369601
"""

DIR_RIGHT = 1
DIR_UP = 2
DIR_LEFT = 3
DIR_DOWN = 4

i = 1
data = { (0,0): 1 }	# key = coords, val = position
data_vals = { (0,0): 1 }

x = 0
y = 0
minmax_x = [ 0, 0 ]
minmax_y = [ 0, 0 ]
cur_dir = DIR_RIGHT

while i <= 368078:
	data[ (x,y) ] = i

	# Calcuate sum of surrounding numbers
	if x == 0 and y == 0:
		total = 1
	else:
		total = 0

	if (x+1,y) in data_vals:
		total += data_vals[ (x+1,y) ]
	if (x+1,y-1) in data_vals:
		total += data_vals[ (x+1,y-1) ]
	if (x,y-1) in data_vals:
		total += data_vals[ (x,y-1) ]
	if (x-1,y-1) in data_vals:
		total += data_vals[ (x-1,y-1) ]
	if (x-1,y) in data_vals:
		total += data_vals[ (x-1,y) ]
	if (x-1,y+1) in data_vals:
		total += data_vals[ (x-1,y+1) ]
	if (x,y+1) in data_vals:
		total += data_vals[ (x,y+1) ]
	if (x+1,y+1) in data_vals:
		total += data_vals[ (x+1,y+1) ]

	data_vals[ (x,y) ] = total

	print( '{0}, {1} = {2}'.format( i, (x,y), total ) )

	if total > 368078:
		print( 'DONE' )
		break

	# Advance position around the spiral
	if cur_dir == DIR_RIGHT:
		x += 1
	elif cur_dir == DIR_UP:
		y -= 1
	elif cur_dir == DIR_LEFT:
		x -= 1
	else:
		y += 1

	# If we're at the "end" of this spiral direction, make a turn
	if x > minmax_x[ 1 ]:
		minmax_x[ 1 ] = x
		cur_dir += 1
	elif y < minmax_y[ 0 ]:
		minmax_y[ 0 ] = y
		cur_dir += 1
	elif x < minmax_x[ 0 ]:
		minmax_x[ 0 ] = x
		cur_dir += 1
	elif y > minmax_y[ 1 ]:
		minmax_y[ 1 ] = y
		cur_dir += 1

	if cur_dir > 4:
		cur_dir = 1

	i += 1

