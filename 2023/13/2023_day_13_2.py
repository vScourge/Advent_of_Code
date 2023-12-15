"""
Advent of Code 2023
Adam Pletcher
adam.pletcher@gmail.com

--- Day 13: Point of Incidence ---
With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the 
edge of Lava Island.

There's just one problem: you don't see any lava.

You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, 
you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of 
large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?

As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames 
keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into 
the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where 
you're about to run into a mirror.

You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully 
analyzing these patterns, you can figure out where the mirrors are!

For example:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between 
two rows or across a vertical line between two columns.

In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns 
point at the line between the columns:

123456789
    ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><   
123456789

In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not 
perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; 
every other column has a reflected column within the pattern and must match exactly: 
column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7

This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, 
but since that's not in the pattern, row 1 doesn't need to match anything. 
The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, 
also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the 
first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above 
it, a total of 405.

Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of 
your notes?

--- Part Two ---
You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, 
because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the 
opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. 
(The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, 
horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7

With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. 
Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, 
row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7

Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first 
pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, 
summarizing to the value 400.

In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing 
the new reflection line in each pattern in your notes?
"""

import numpy
import copy

def parse_input():
	data = [ ]
	pattern = [ ]

	with open('input.txt', 'r') as in_file:
		lines = in_file.readlines()
	i = 0
	
	while True:
		if i == len(lines):
			break
		
		line = lines[i].strip()
		
		if not line or i == len(lines)-1:
			data.append(numpy.array(pattern))
			pattern = [ ]
			i += 1
			continue

		row = numpy.array([x for x in line])
		pattern.append(row)
		i += 1
		
	return data


def find_horizontal(pat, orig_val):
	total = 0
	
	# Horizontal mirror
	for x in range(len(pat[0])-1):
		pat1 = pat[0:, 0:x+1]
		pat2 = pat[0:, x+1:x+2+x]

		s = len(pat1[0]) - len(pat2[0])
		#print(s)
		pat1 = pat1[0:, s:]

		#print(pat)
		#print(pat1)
		#print(pat2)
		
		# Flip pat1 and compare, see if this is the reflection point
		pat1_flip = numpy.flip(pat1, 1)

		val = s + len(pat1[0])
		
		if val != orig_val and all((pat1_flip == pat2).ravel()):
			# Vertical reflection line found, so add # cols to left to total
			total += val
			break
		
	return total
	
	
def find_vertical(pat, orig_val):
	total = 0
	
	# Vertical mirror
	for y in range(len(pat)-1):
		pat1 = pat[0:y+1, 0:]
		pat2 = pat[y+1:y+2+y, 0:]

		s = len(pat1) - len(pat2)
		#print(s)
		pat1 = pat1[s:, 0:]

		#print(pat)
		#print(pat1)
		#print(pat2)
		
		# Flip pat1 and compare, see if this is the reflection point
		pat1_flip = numpy.flip(pat1, 0)

		val = (s + len(pat1)) * 100
		
		if val != orig_val and all((pat1_flip == pat2).ravel()):
			# Vertical reflection line found, so add # cols to left to total
			total += val
			break
		
	return total	


def test_pattern(pat, orig_val):
	total = 0
	found = False
	
	for y in range(len(pat)):
		if found:
			break
		
		for x in range(len(pat[0])):
			if pat[y][x] == '#':
				pat[y][x] = '.'
			else:
				pat[y][x] = '#'
				
			val = find_horizontal(pat, orig_val)
			
			if val and val != orig_val:
				print(f'SMUDGE H {val}:')
				print(pat)
				
				total += val
				found = True
				break
			
			val = find_vertical(pat, orig_val)
			
			if val and val != orig_val:
				print(f'SMUDGE V {val}:')
				print(pat)

				total += val
				found = True
				break

			# Flip char back again
			if pat[y][x] == '#':
				pat[y][x] = '.'
			else:
				pat[y][x] = '#'
			
	return total
	

if __name__ == '__main__':
	data = parse_input()
	total = 0
	c = 0
	
	for pat in data:
		c += 1
		answer1 = 0
		
		val = find_horizontal(pat, -1)
		
		if val:
			print(f'ORIGINAL H {val}:')
			print(pat)

			answer1 = val
		else:
			val = find_vertical(pat, -1)
		
			if val:
				print(f'ORIGINAL V {val}:')
				print(pat)

				answer1 = val

		# Test for smudges
		answer2 = 0
		val = test_pattern(pat, answer1)
		
		if val:
			answer2 = val

		
		if answer2:
			print(answer2)
			total += answer2
		else:
			print(answer1)
			total += answer1


	print(f'total = {total}')
	
# 27722 too low	
# 34795
