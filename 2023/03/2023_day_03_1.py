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


def get_adjacent_symbols(data, coord, number):
	# Pad data grid by 1 char of '.', so we can slice it easier
	data2 = numpy.pad(data, ((1, 1), (1, 1)), 'constant', constant_values='.')

	ny = coord[0]+1
	nx = coord[1]+1
	
	data_slice = data2[ny-1:ny+2, nx-1:nx+len(str(number))+1]
	data_list = list(data_slice.ravel())
	symbols = [c for c in data_list if not c.isdigit() and c != '.']
	
	return symbols
		
		
if __name__ == '__main__':
	total = 0
	data = parse_input()
	numbers = get_numbers(data)

	for coord, number in numbers.items():
		symbols = get_adjacent_symbols(data, coord, number)
		
		if symbols:
			total += number
	
	print('total =', total)


