"""
--- Day 23: Crab Cups ---
The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.

The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, 
there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled 
3, 2, 4, 1, 5, and then back to 3 again.

Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.

Each move, the crab does the following actions:

The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, 
  the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, 
  it wraps around to the highest value on any cup's label instead.
The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
The crab selects a new current cup: the cup which is immediately clockwise of the current cup.

For example, suppose your cup labeling were 389125467. If the crab were to do merely 10 moves, the following changes would occur:

-- move 1 --
cups: (3) 8  9  1  2  5  4  6  7 
pick up: 8, 9, 1
destination: 2

-- move 2 --
cups:  3 (2) 8  9  1  5  4  6  7 
pick up: 8, 9, 1
destination: 7

-- move 3 --
cups:  3  2 (5) 4  6  7  8  9  1 
pick up: 4, 6, 7
destination: 3

-- move 4 --
cups:  7  2  5 (8) 9  1  3  4  6 
pick up: 9, 1, 3
destination: 7

-- move 5 --
cups:  3  2  5  8 (4) 6  7  9  1 
pick up: 6, 7, 9
destination: 3

-- move 6 --
cups:  9  2  5  8  4 (1) 3  6  7 
pick up: 3, 6, 7
destination: 9

-- move 7 --
cups:  7  2  5  8  4  1 (9) 3  6 
pick up: 3, 6, 7
destination: 8

-- move 8 --
cups:  8  3  6  7  4  1  9 (2) 5 
pick up: 5, 8, 3
destination: 1

-- move 9 --
cups:  7  4  1  5  8  3  9  2 (6)
pick up: 7, 4, 1
destination: 5

-- move 10 --
cups: (5) 7  4  1  8  3  9  2  6 
pick up: 7, 4, 1
destination: 3

-- final --
cups:  5 (8) 3  7  4  1  9  2  6 
In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the current cup is marked with ( ).

After the crab is done, what order will the cups be in? Starting after the cup labeled 1, collect the other cups' labels clockwise into a 
single string with no extra characters; each number except 1 should appear exactly once. In the above example, after 10 moves, the cups 
clockwise from 1 are labeled 9, 2, 6, 5, and so on, producing 92658374. If the crab were to complete all 100 moves, 
the order after cup 1 would be 67384529.

Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?

Your puzzle input is 792845136.


--- Part Two ---
Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the 
crab starts arranging many cups in a circle on your raft - one million (1000000) in total.

Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing 
fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. 
(For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until 
one million is reached.) In this way, every number from one through one million is used exactly once.

After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do 
merely 100 moves; the crab is going to do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. 
You can have them if you predict what the labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?
"""

### IMPORTS ###

import collections
import cProfile
import math
import numpy
import pstats
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'



### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	return lines[ 0 ]


def main( labels ):
	"""
	"""
	time_start = time.perf_counter( )
	
	cups = collections.deque( )
	
	for l in labels:
		cups.append( int( l ) )
		
	min_label = min( cups )
	max_label = max( cups )

	# Add all numbers up to 1M
	for i in range( max_label + 1, 1000000 + 1 ):
		cups.append( i )
	
	cur_cup = cups[ 0 ]
	move = 0
	
	while move < 10000000:
		move += 1
		
		if move % 10 == 0:
			elapsed_secs = time.perf_counter( ) - time_start
			secs_per_move = elapsed_secs / move
			hours_remaining = secs_per_move * ( 10000000 - move ) / 60.0 / 60.0

			print( 'move {0} ({1:.02f}%), {2:.02f} hours remaining'.format( move, move / 10000000 * 100.0, hours_remaining ) )
			
			profiler = cProfile.Profile( )
			profiler.enable( )
			
		
		#print( '\n-- move {0} --'.format( move ) )
		#print( 'cups: {0}'.format( ' '.join( [ str( c ) for c in list( cups )[ :50 ] ] ) ) )
		
		while cups[ -1 ] != cur_cup:
			cups.rotate( 1 )
			
		#idx = cups.index( cur_cup )
		#cups.rotate( len( cups ) - idx - 1 )
		
		# Remove 3 cups to right (clockwise) of current cup
		removed = [
		    cups.popleft( ),
		    cups.popleft( ),
		    cups.popleft( )
		]
		
		#print( 'pick up: {0}'.format( ' '.join( [ str( r ) for r in removed ] ) ) )
		
		# find destination cup
		dest_cup = None
		i = cur_cup - 1
		
		while dest_cup is None:
			if i in cups:
				dest_cup = i
				continue

			i -= 1
			if i < min_label:
				i = max_label
		
		#print( 'destination:', dest_cup )
		
		# Got our destination cup, so insert cups to right of it
		while cups[ -1 ] != dest_cup:
			cups.rotate( 1 )
			
		#idx = cups.index( dest_cup )
		
		#if idx != len( cups ) - 1:
			## Have to do some rotating to get dest cup to end
			#cups.rotate( len( cups ) - idx - 1 )
		
		# Add our removed cups		
		for r_cup in removed:
			cups.append( r_cup )
			
		# Rotate to get current cup at head again, then pick new current cup
		while cups[ 0 ] != cur_cup:
			cups.rotate( )
			
		#idx = cups.index( cur_cup )
		#cups.rotate( len( cups ) - idx )

		cur_cup = cups[ 1 ]
		
		# print answer?
		#print( 'cups: {0}'.format( ' '.join( [ str( c ) for c in list( cups )[ :50 ] ] ) ) )
		
		if move % 1000 == 0:
			profiler.disable( )
			stats = pstats.Stats( profiler )
			stats.dump_stats( r'C:\Users\Home\Dropbox (Personal)\misc\profile.pstats' )	

	print( '\n-- final --' )
	#print( 'cups: {0}'.format( ' '.join( [ str( c ) for c in cups ] ) ) )

	idx = cups.index( 1 )
	
	idx1 = idx + 1
	if idx1 >= len( cups ):
		idx1 = idx1 - len( cups )
	idx2 = idx + 2
	if idx2 >= len( cups ):
		idx2 = idx2 - len( cups )
		
	val1 = cups[ idx1 ]
	val2 = cups[ idx2 ]
	#print( 'answer = {0} * {1} = {2}'.format( val1, val2, val1 * val2 ) )
	
		    
	## Calculate score
	## Rotate so "1" is at end (on right)
	#idx = cups.index( 1 )
	#cups.rotate( len( cups ) - idx - 1 )
	
	#score = ''.join( [ str( c ) for c in cups ] )[ :-1 ]
	
	return val1 * val2
	
# test answer = 67384529

### CLASSES ###


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	labels = parse_input( )
	
	answer = main( labels )

	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 30033 not right
