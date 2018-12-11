"""
Advent of Code 2017

input is: input.txt
answer is VEBTPXCHLI

"""
import string

DIR_D = ( 0, 1 )
DIR_L = ( -1, 0 )
DIR_U = ( 0, -1 )
DIR_R = ( 1, 0 )


if __name__ == '__main__':
	data = { }

	y = 0
	x = 0

	ignore_chars = ( '\n', ' ' )
	trail = ''
	steps = 0
	start_coord = None

	# Build game board data
	for line in open( 'input.txt', 'r' ):
		for char in line:
			if char in ignore_chars:
				x += 1
				continue

			if not start_coord:
				start_coord = (x,y)

			data[ (x,y) ] = char
			x += 1

		x = 0
		y += 1

	# Start walking it
	# Find starting pos
	cpos = start_coord
	cdir = DIR_D

	while True:
		print( cpos )

		if cpos not in data:
			print( 'answer1 =', trail )
			print( 'answer2 =', steps - 1 )
			break

		while cpos in data and data[ cpos ] != '+':
			if data[ cpos ] in string.ascii_uppercase:
				trail += data[ cpos ]

			cpos = ( cpos[ 0 ] + cdir[ 0 ], cpos[ 1 ] + cdir[ 1 ] )
			print( cpos )
			steps += 1

		# turn
		if cdir == DIR_D or cdir == DIR_U:
			if data.get( ( cpos[ 0 ] - 1, cpos[ 1 ] ) ):
				cdir = DIR_L
			else:
				cdir = DIR_R

		else:
			if data.get( ( cpos[ 0 ], cpos[ 1 ] - 1 ) ):
				cdir = DIR_U
			else:
				cdir = DIR_D

		cpos = ( cpos[ 0 ] + cdir[ 0 ], cpos[ 1 ] + cdir[ 1 ] )
		steps += 1


	print( 'done' )

# 18704 and 18703 too high