"""
Advent of Code 2017

input is: input.txt
example:
dtf dec -691 if if >= -1212

answer is 3880
"""


def parse_line( line ):
	name1, direction, value, junk, name2, operator, amt = line.strip( ).split( ' ' )

	value = int( value )
	amt = int( amt )

	line_parts = {
	    'name1': name1,
	    'direction': direction,
	    'value': value,
	    'junk': junk,
	    'name2': name2,
	    'operator': operator,
	    'amt': amt,
	}

	return line_parts


def evaluate_statement( name, operator, amt ):
	eval_str = 'DATA[ "{0}" ] {1} {2}'.format( name, operator, amt )

	result = eval( eval_str )
	print( DATA[ name ], ',', eval_str, ',', result )

	return result


if __name__ == '__main__':
	DATA = { }
	highest_val = 0

	for line in open( 'input.txt', 'r' ):
		print( '---\n' + line.strip( ) )

		parts = parse_line( line )

		if parts[ 'name1' ] not in DATA:
			DATA[ parts[ 'name1' ] ] = 0
		if parts[ 'name2' ] not in DATA:
			DATA[ parts[ 'name2' ] ] = 0

		if evaluate_statement( parts[ 'name2' ], parts[ 'operator' ], parts[ 'amt' ] ):
			if parts[ 'direction' ] == 'inc':
				op_str = '+'
			else:
				op_str = '-'

			exec_str = "DATA[ '{0}' ] = DATA[ '{0}' ] {1} {2}".format( parts[ 'name1' ], op_str, parts[ 'value' ] )
			print( exec_str )

			exec( exec_str )

		highest_val = max( highest_val, max( DATA.values( ) ) )

	print( 'highest =', highest_val )
	print( 'done' )

# wrong answers: 3863,