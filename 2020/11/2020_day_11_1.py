"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes 
directly to the tropical island where you can finally start your vacation. As you reach the 
waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're 
pretty sure you can predict the best place to sit. You make a quick map of the seat 
layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), 
or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are 
entirely predictable and always follow a simple set of rules. All decisions are based on the 
number of occupied seats adjacent to a given seat (one of the eight positions immediately up, 
down, left, right, or diagonal from the seat). The following rules are applied to every seat 
simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications 
of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change 
state. How many seats end up occupied?
"""

### IMPORTS ###

import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'


### FUNCTIONS ###

def parse_input( ):
	"""
	Parse input file, returning 2D array of seats
	"""
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	seat_list = [ [ '.' for i in range( 94 ) ] ]
	
	for line in lines:
		row_seats = [ '.' ]
		
		for letter in line:
			row_seats.append( letter )
		
		row_seats.append( '.' )
		
		seat_list.append( row_seats )
		
	seat_list.append( [ '.' for i in range( 94 ) ] )
		
	cur_seats = numpy.array( seat_list )
	
	return cur_seats

	
def count_occupied_seats( seats, x, y ):
	"""
	Count occupied seats adjacent to the one supplied
	"""
	seat = seats[ y ][ x ]
	
	adj_seats = [
	    seats[ y-1 ][ x-1 ],
	    seats[ y-1 ][ x ],
	    seats[ y-1 ][ x+1 ],
	    seats[ y ][ x-1 ],
	    seats[ y ][ x+1 ],
	    seats[ y+1 ][ x-1 ],
	    seats[ y+1 ][ x ],
	    seats[ y+1 ][ x+1 ]
	]
		
	count = adj_seats.count( '#' )
	return count
	

def print_seats( seats ):
	for y in range( len( seats ) ):
		print( ''.join( seats[ y ] ) )

	
### CLASSES ###

### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )
	
	cur_seats = parse_input( )
			
	while True:
		seats = cur_seats.copy( )
		
		for y in range( 1, len( seats ) - 1 ):
			for x in range( 1, len( seats[ 0 ] ) -1 ):
				seat = cur_seats[ y ][ x ]
				
				if seat == '.':
					continue
				
				occupied = count_occupied_seats( cur_seats, x, y )
				
				if seat == 'L' and occupied == 0:
					# Take this seat
					seats[ y ][ x ] = '#'

				elif seat == '#' and occupied >= 4:
					seats[ y ][ x ] = 'L'			
		
		#print( '---' )
		#print_seats( seats )
		
		if numpy.array_equal( cur_seats, seats ):
			break
		
		cur_seats = seats.copy( )
		
	count = 0
	for y in range( len( cur_seats ) ):
		count += ''.join( cur_seats[ y ] ).count( '#' )
		
	print( 'answer =', count )
	print( 'done in {0:.4f}'.format( time.perf_counter( ) - time_start ) )

# 2254 
