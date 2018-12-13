"""
--- Day 12: Subterranean Sustainability ---
The year 518 is significantly more underground than your history books implied. Either that, or you've arrived in a vast cavern network under the North Pole.

After exploring a little, you discover a long tunnel that contains a row of small pots as far as you can see to your left and right.
 A few of them contain plants - someone is trying to grow things in these geothermally-heated caves.

The pots are numbered, with 0 in front of you. To the left, the pots are numbered -1, -2, -3, and so on; to the right, 1, 2, 3....
Your puzzle input contains a list of pots from 0 to the right and whether they do (#) or do not (.) currently contain a plant, the
initial state. (No other pots currently contain plants.) For example, an initial state of #..##.... indicates that pots 0, 3, and 4
currently contain plants.

Your puzzle input also contains some notes you find on a nearby table: someone has been trying to figure out how these plants spread
to nearby pots. Based on the notes, for each generation of plants, a given pot has or does not have a plant based on whether that
pot (and the two pots on either side of it) had a plant in the last generation. These are written as LLCRR => N, where L are pots to
the left, C is the current pot being considered, R are the pots to the right, and N is whether the current pot will have a plant in
the next generation. For example:

A note like ..#.. => . means that a pot that contains a plant but with no plants within two pots of it will not have a plant in it
during the next generation.

A note like ##.## => . means that an empty pot with two plants on each side of it will remain empty in the next generation.
A note like .##.# => # means that a pot has a plant in a given generation if, in the previous generation, there were plants in that
pot, the one immediately to the left, and the one two pots to the right, but not in the ones immediately to the right and two to the left.

It's not clear what these plants are for, but you're sure it's important, so you'd like to make sure the current configuration of
plants is sustainable by determining what will happen after 20 generations.

For example, given the following input:

initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
For brevity, in this example, only the combinations which do produce a plant are listed. (Your input includes all possible
combinations.) Then, the next 20 generations will look like this:

                 1         2         3
       0         0         0         0
 0: ...#..#.#..##......###...###...........
 1: ...#...#....#.....#..#..#..#...........
 2: ...##..##...##....#..#..#..##..........
 3: ..#.#...#..#.#....#..#..#...#..........
 4: ...#.#..#...#.#...#..#..##..##.........
 5: ....#...##...#.#..#..#...#...#.........
 6: ....##.#.#....#...#..##..##..##........
 7: ...#..###.#...##..#...#...#...#........
 8: ...#....##.#.#.#..##..##..##..##.......
 9: ...##..#..#####....#...#...#...#.......
10: ..#.#..#...#.##....##..##..##..##......
11: ...#...##...#.#...#.#...#...#...#......
12: ...##.#.#....#.#...#.#..##..##..##.....
13: ..#..###.#....#.#...#....#...#...#.....
14: ..#....##.#....#.#..##...##..##..##....
15: ..##..#..#.#....#....#..#.#...#...#....
16: .#.#..#...#.#...##...#...#.#..##..##...
17: ..#...##...#.#.#.#...##...#....#...#...
18: ..##.#.#....#####.#.#.#...##...##..##..
19: .#..###.#..#.#.#######.#.#.#..#.#...#..
20: .#....##....#####...#######....#.#..##.

The generation is shown along the left, where 0 is the initial state. The pot numbers are shown along the top, where 0
labels the center pot, negative-numbered pots extend to the left, and positive pots extend toward the right. Remember,
the initial state begins at pot 0, which is not the leftmost pot used in this example.

After one generation, only seven plants remain. The one in pot 0 matched the rule looking for ..#.., the one in pot 4
matched the rule looking for .#.#., pot 9 matched .##.., and so on.

In this example, after 20 generations, the pots shown as # contain plants, the furthest left of which is pot -2, and the
furthest right of which is pot 34. Adding up all the numbers of plant-containing pots after the 20th generation produces 325.

After 20 generations, what is the sum of the numbers of all pots which contain a plant?

--- Part Two ---
You realize that 20 generations aren't enough. After all, these plants will need to last another 1500 years to even reach your timeline, not to mention your future.

After fifty billion (50000000000) generations, what is the sum of the numbers of all pots which contain a plant?
"""

import sys
import time

import numpy


### CLASSES ###

class Note( ):
	def __init__( self, line ):
		self.pattern = [ c == '#' for c in line[ :5 ] ]
		self.result = line[ -1 ] == '#'
		self.line = line

		a = 3

	def __repr__( self ):
		return '<Note {0}>'.format( self.line )


### FUNCTIONS ###


### MAIN ###

if __name__ == "__main__":
	"""
	initial state: #....##.#.#.####..#.######..##.#.########..#...##...##...##.#.#...######.###....#...##..#.#....##.##

	.#.## => #
	"""

	notes = [ ]

	for line in open( 'input.txt', 'r' ):
		if 'initial' in line:
			gen0 = '....' + line[ 15: ].strip( ) + '.............'
			zero = 4
		elif line == '\n':
			continue
		else:
			note = Note( line.strip( ) )
			notes.append( note )

	gen1 = '.' * len( gen0 )

	for g in range( 50000000000 ):
		# print( '--------\ng =', g )
		for i in range( 2, len( gen0 ) ):
			# print( 'i =', i )
			pot = gen0[ i ]
			pot_pattern = [ c == '#' for c in gen0[ i-2:i ] + pot + gen0[ i+1:i+3 ] ]
			_ = 1

			for note in notes:
				if note.pattern == pot_pattern and note.result:
					# print( note )
					# print( 'gen0 =', gen0 )
					# print( 'gen1 =', gen1 )
					gen1 = gen1[ :i ] + '#' + gen1[ i+1: ]
					# print( 'gen1 =', gen1 )
					# print( ( 7 + i ) * ' ' + '^' )
					break

		# print( '--\n{0}\n{1}'.format( gen0, gen1 ) )
		# gen0 = '....' + gen1
		if gen1[ :4 ].count( '.' ) < 4:
			gen1 = '....' + gen1
			zero += 4
		if gen1[ -4: ].count( '.' ) < 4:
			gen1 += '....'

		gen0 = gen1
		gen1 = '.' * len( gen0 )

		if g % 100 == 0:
			total = 0
			p = -zero
			for i in range( len( gen0 ) ):
				try:
					if gen0[ i ] == '#':
						total += p
				except IndexError:
					break

				p += 1

			print( 'g = {0}, total = {1}'.format( g, total ) )


	print( 'total of pot-containing plants = {0}'.format( total ) )
	print( 'done' )

"""
So this doesn't print the literal answer, but it prints out what becomes a pattern.
After the first 100 generations or so, it goes up 1500 plants every 100 generations,
or 15 per generation.  Some math to account for the uneven start, and the fact we're
applying the pattern starting at generation 100...

( 50000000000 - 100 ) * 15 + 2197 = 
750000000697 <- ANSWER
"""