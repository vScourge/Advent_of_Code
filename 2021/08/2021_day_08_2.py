"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate 
another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays 
in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still 
trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. 
Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: 
the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, 
you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, 
and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, 
the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns 
correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. 

Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. 
Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. 
Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value 
(cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of 
signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, 
there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?


--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
 
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1

Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3

Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. 
What do you get if you add up all of the output values?


  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 
"""

"""
each digit is uniquely defined by:
- how many segments it has
- how many segments overlap with 4
- how many segments overlap with 7

So just a little lookup table of 10 3-tuples.
"""


import numpy

# key is digit, value is number of segments in digit
seg_counts = {
	0: 6,
	1: 2,	#
	2: 5,
	3: 5,
	4: 4,	#
	5: 5,
	6: 6,
	7: 3,	#
	8: 7,	#
	9: 6
}

digits = {
	'abcefg': 0, 
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

def fill_signal_map( signals ):
	# This is the answer key. Incomplete unless all 9 signals
	# have valid translation values.
	# Keys are the true segment letters, values are the encoded values
	signal_map = {
		'a': None,
		'b': None,
		'c': None,
		'd': None,
		'e': None,
		'f': None,
		'g': None,
	}
	
	# First, find the signal with only two characters. This is the 1 digit
	one = [ s for s in signal if len( s ) == 2 ][ 0 ]
	
	# Find the three signals with 6 segments. These are 0, 6 and 9 digits
	sixes = [ s for s in signal if len( s ) == 6 ]
	
	# The 0 and 9 digits will have both of the segments used by 1 digit.
	# The 6 digit will not have both of those, so let's find it.
	six = None
	
	for s in sixes:
		if one[ 0 ] not in s:
			six = s
			signal_map[ 'c' ] = one[ 0 ]
			signal_map[ 'f' ] = one[ 1 ]
			break
		elif one[ 1 ] not in s:
			six = s
			signal_map[ 'c' ] = one[ 1 ]
			signal_map[ 'f' ] = one[ 0 ]
			break
		
	# Now we know 'f' and 'c', so let's find the 7 digit so we can determine 'a'
	seven = [ s for s in signal if len( s ) == 3 ][ 0 ]
	temp = ( signal_map[ 'c' ], signal_map[ 'f' ] )
	signal_map[ 'a' ] = [ c for c in seven if c not in temp ][ 0 ]

	# Find the three signals with 5 segments, these are 2, 3 and 5	
	fives = [ s for s in signal if len( s ) == 5 ]
	
	# 5 and 6 are identical, except that 5 is missing "e" segment
	six_set = set( six )
	
	for s in fives:
		diff = six_set.difference( set( s ) )
		if len( diff ) == 1:
			five = s
			signal_map[ 'e' ] = list( diff )[ 0 ] 
			break
			
	# We know six. And 0 and 9 are same, except 0 has 'e' and 9 has 'd'
	# We know signal for 'e' at this point, so we can deduce what 'd' is.
	zero_nine = [ x for x in sixes ]
	zero_nine.remove( six )
	
	if signal_map[ 'e' ] in zero_nine[ 0 ]:
		zero, nine = zero_nine
	else:
		nine, zero = zero_nine
	
	signal_map[ 'd' ] = [ x for x in nine if x not in zero ][ 0 ]

	# Four is only one with 4 signals.
	# Add 'a' signal to four, and compare it to nine to get 'g'
	four = [ s for s in signals if len( s ) == 4 ][ 0 ]
	temp = four + signal_map[ 'a' ]
	
	signal_map[ 'g' ] = [ x for x in nine if x not in temp ][ 0 ]
	
	# Now we only need to find 'b'
	# Three and five are same, except three has 'c' and five has 'b'
	# And we know what five is already.
	temp = [ s for s in fives if signal_map[ 'e' ] not in s ]
	temp.remove( five )
	three = temp[ 0 ]
	
	# Now we know three, we compare that to nine to find 'b'
	signal_map[ 'b' ] = list( set( nine ).difference( set( three ) ) )[ 0 ]
	
	# Done!
	return signal_map
	

	
	

def parse_input( ):
	data = [ ]
	
	for line in open( 'input.txt', 'r' ):
		str1, str2 = line.strip( ).split( ' | ' )
		
		signals = str1.split( ' ' )
		output = str2.split( ' ' )
		
		data.append( ( signals, output ) )
		
	return data
	
	
	
# Main

data = parse_input( )
answer = 0

for signal, output in data:
	signal_map = fill_signal_map( signal )
	
	print( signal_map )

	digit_str = ''
	
	# Make reverse signal map, with keys as encoded segment values, and values as real signal IDs
	rev_signal_map = { v: k for k, v in signal_map.items( ) }
	
	num_str = ''
	
	for out_str in output:
		decoded_signal = ''.join( sorted( [ rev_signal_map[ x ] for x in out_str ] ) )
		
		digit = digits.get( decoded_signal )
		num_str += str( digit )
		
		print( out_str, decoded_signal, '=', digit )
		
	answer += int( num_str )
	
print( 'answer =', answer )
# 996280