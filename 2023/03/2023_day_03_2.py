"""
Advent of Code 2023
Adam Pletcher
adam.pletcher@gmail.com

--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water 
source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! 
The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. 
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers 
and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a 
"part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 
58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the 
engine schematic?

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the 
closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone 
labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding 
a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit 
the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is 
adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out 
which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear 
ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a 
gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

import numpy

def parse_input():
	list_data = [ ]
	
	for line in open('input.txt', 'r'):
		list_line = [c for c in line.strip()]
		list_data.append(list_line)
		
	data = numpy.array(list_data)
			
	return data
		

def get_numbers(data):
	numbers = { }
	cx = 0
	cy = 0
	
	while cy < len(data):
		char = data[cy, cx]
		num_str = ''
		coord = None
		
		while char.isdigit():
			if not coord:
				# First digit in number
				coord = (cy, cx)
				
			num_str += char

			cx += 1
			
			if cx == len(data[0]):
				cy += 1
				cx = 0
				break
		
			char = data[cy, cx]
				
		if num_str:
			numbers[coord] = int(num_str)
		else:
			cx += 1
			
			if cx == len(data[0]):
				cy += 1
				cx = 0

				if cy == len(data):
					break
		
	return numbers


def get_adjacent_numbers(data, numbers, coord):
	adj_numbers = [ ]
	cy, cx = coord
	
	min_y = max(cy-1, 0)
	min_x = max(cx-1, 0)
	max_y = min(cy+1, len(data))+1
	max_x = min(cx+1, len(data[0]))+1
	
	for y in range(min_y, max_y):
		for x in range(min_x, max_x):
			if (y, x) == coord:
				continue

			#print((y,x))
			
			number = get_number_from_coord((y, x), numbers)
			
			if number and number not in adj_numbers:
				adj_numbers.append(number)

	return adj_numbers


def get_number_from_coord(coord, numbers):
	y, x = coord
	
	for num_coord, number in numbers.items():
		#if coord == num_coord:
			#return number
		
		if y != num_coord[0]:
			continue
		
		for cx in range(0, len(str(number))):
			if (y, num_coord[1]+cx) == coord:
				return num_coord
			
	return None
		
	
		
if __name__ == '__main__':
	total = 0
	data = parse_input()
	numbers = get_numbers(data)

	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y, x] == '*':
				adj_number_coords = get_adjacent_numbers(data, numbers, (y, x))
				adj_numbers = [numbers[c] for c in adj_number_coords]

				print('gear', (y,x), '=', adj_numbers)
				
				if len(adj_numbers) == 2:
					# found a gear ratio
					total += adj_numbers[0] * adj_numbers[1]
					
					
	print('total =', total)


# 86472737 too low
