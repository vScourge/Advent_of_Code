"""
Advent of Code 2017

input is: input.txt

Here are some self-contained pieces of garbage:

<>, empty garbage.
<random characters>, garbage containing random characters.
<<<<>, because the extra < are ignored.
<{!>}>, because the first > is canceled.
<!!>, because the second ! is canceled, allowing the > to terminate the garbage.
<!!!>>, because the second ! and the first > are canceled.
<{o"i!a,<{i<a>, which ends at the first >.
Here are some examples of whole streams and the number of groups they contain:

{}, 1 group.
{{{}}}, 3 groups.
{{},{}}, also 3 groups.
{{{},{},{{}}}}, 6 groups.
{<{},{},{{}}>}, 1 group (which itself contains garbage).
{<a>,<a>,<a>,<a>}, 1 group.
{{<a>},{<a>},{<a>},{<a>}}, 5 groups.
{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).

Answer 1 is 21037
Answer 2 is 9495
"""

import re

class Group( ):
	def __init__( self, outer, inner = None, score = 0 ):
		self.outer = outer
		self.score = score

		if inner:
			self.inner = inner
		else:
			self.inner = [ ]


if __name__ == '__main__':
	regex = re.compile( '<(.*?)>' )

	data = open( 'input.txt', 'r' ).read( ).strip( )

	i = 0

	groups = [ ]
	garbage = ''
	garbage_count = 0
	group_count = 0
	last_char = ''
	depth = 0
	score = 0

	while True:
		if i >= len( data ):
			# reached the end
			break

		char = data[ i ]

		if char == '!':
			# Ignore this, plus next character
			i += 1

		elif char == '{':
			if garbage:
				garbage += char
			else:
				group_count += 1
				groups.append( char )

		elif char == ',' and garbage:
			garbage += char

		elif char == '<':
			garbage += char

		elif char == '>':
			garbage += char
			garbage_count += len( garbage ) - 2
			print( 'garbage: {0}, {1}, {2}'.format( garbage, len( garbage ) - 2, garbage_count ) )
			groups[ -1 ] += garbage
			garbage = ''

		elif char == '}':
			if garbage:
				garbage += char
			else:
				score += len( groups )
				groups[ -1 ] += char
				print( 'group: {0}'.format( groups[ -1 ] ) )
				groups = groups[ :len( groups ) - 1 ]
				group_count += 1

		else:
			if garbage:
				garbage += char
			else:
				groups[ -1 ] += char

		i += 1

"""
{{},{{{{{},{{<!!!>!<"<!>,<!!!>!>},<!>,<'e">},
"""
print( '\nAnswer 1: score =', score )
print( 'Answer 2: garbage_count =', garbage_count )
print( 'done' )

# 9440 too low