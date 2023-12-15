"""
Advent of Code 2023
Adam Pletcher
adam.pletcher@gmail.com

--- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks 
more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't 
worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks 
into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more 
sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could 
you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you 
can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble 
making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to 
use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with 
each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but 
numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into 
numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert 
a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil 
to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire 
ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, 
the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48

The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line 
means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same 
length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 
corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. 
This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. 
So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds 
to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51

With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location 
that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. 
To do this, you'll need to convert each seed number through other categories until you can find its corresponding 
location number. In this example, the corresponding types are:



So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: 
line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and 
the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed 
number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and 
contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, 
fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest 
location number that corresponds to any of the initial seed numbers?
"""

import numpy
import os
import threading
import time


output_filename = r'D:\temp\output.txt'


def parse_input():
	data = {'seeds': [ ], 'maps': [ ]}
	
	with open('input.txt', 'r') as file:
		lines = file.readlines()
		
	lines = [l.strip() for l in lines]

	seeds = [ ]
	maps = [ ]
	i = 0
	
	while i < len(lines):
		#print('line {0} of {1}'.format(i, len(lines)))
		line = lines[i]
		
		if not line:
			i += 1
			continue
		
		if i == 0:
			seed_entries = [int(x) for x in line.split(': ')[1].split(' ')]
			s = 0
			while s < len(seed_entries):
				seeds.append((seed_entries[s], seed_entries[s+1]))
				s += 2
		
			data['seeds'] = seeds
			i += 1
			continue

		if ':' in line:
			i += 1
			line = lines[i]
			cat_map = [ ]
			
			while line != '':
				dst, src, run = [int(x) for x in line.split(' ')]
				#src_range = numpy.arange(src, src + run, 1)
				diff = dst - src
				cat_map.append((src, run, diff))

				i += 1
				if i == len(lines):
					break
				
				line = lines[i]

			maps.append(cat_map)
				
	data['maps'] = maps
		
	return data


def get_closest_location(name, seeds_pair, data, cat_ranges_cache):		
	print(f'thread {name} starting...')

	closest_location = 999999999999
	
	seeds_start, seeds_run = seeds_pair
	seeds_end = seeds_start + seeds_run
	seed = seeds_start

	
	#print('seed range {0} of {1} = {2}-{3}'.format(c, len(data['seeds']), seeds_start, seeds_end))
	last_percent = '0.00%'
	
	while seed <= seeds_end:
		s = seed
		
		percent = '{0:0.2f}%'.format((s - seeds_start) / (seeds_end - seeds_start) * 100.0)
		if percent != last_percent:
			print('Thread {0} - {1}'.format(name, percent))
			last_percent = percent
			
		#print('\nseed {0}...'.format(s))
		
		"""
		Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
		Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
		Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
		Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
		"""				
		
		for cat_maps in data['maps']:
			#print('cat')

			#cat_maps2 = cat_maps
			#cat_maps2 = [m for m in cat_maps if not seeds_start > m[0]+m[1] and not seeds_end < m[0]]
			cat_maps2 = [m for m in cat_maps if not s > m[0]+m[1] and not s < m[0]]
			
			#cat_ranges = [(range(cur_map[0], cur_map[0] + cur_map[1]), cur_map[2]) for cur_map in cat_maps2]
			#cat_ranges = [cat_ranges_cache[r] for r in cat_maps2]

			if cat_maps2:
				s += cat_ranges_cache[cat_maps2[0]][1]

		
		seed += 1
				
		if s < closest_location:
			closest_location = s - 1
			
	print('thread {0} DONE ='.format(name), closest_location)
	
	with open(output_filename, 'a') as out_file:
		out_file.write('thread {0} = {1}\n'.format(name, closest_location))
		
	return closest_location



if __name__ == '__main__':
	if os.path.exists(output_filename):
		os.remove(output_filename)
	
	data = parse_input()
	
	cat_ranges_cache = { }

	for cat_maps in data['maps']:
		for cat_map in cat_maps:
			if cat_map in cat_ranges_cache:
				pass
				#print('foo')
			else:
				cat_ranges_cache[cat_map] = (range(cat_map[0], cat_map[0] + cat_map[1]), cat_map[2])
				#print('foo')
				
	i = 1
	threads = [ ]
	
	for seeds_pair in data['seeds']:
		t = threading.Thread(target=get_closest_location, args=(i, seeds_pair, data, cat_ranges_cache))
		threads.append(t)
		#t.start()
		i += 1
								  
		#closest_location = get_closest_location(seeds_pair, data)
		#print('closest location =', closest_location)
	
	max_threads = 5
	
	while True:
		#active_threads = [t for t in threads if t.is_alive()]
		active_threads = threading.enumerate()
		#print('active =', active_threads)
		
		if threads:
			if len(active_threads) < max_threads:
				t = threads.pop(0)
				t.start()
		else:
			if len(active_threads) == 1:
				# All done
				break

		#time.sleep(0.05)
		
		
	#for i, t in enumerate(threads):
		#t.join()
		#print('Main: thread {0} done!'.format(i+1))

# too high 17729183
# thread  1 = 709155282
# thread  2 = 298575530
# thread  3 = 426952358
# thread  4 = 119414365
# thread  6 = 268768047
# thread  7 = 382895070
# thread  8 = 176041861
# thread  9 = 179092548
# thread  5 = 17729183
# thread 10 = 199427217

# Answer = 17729182