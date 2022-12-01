"""
--- Day 9: Sensor Boost ---
You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress signal
coming from the asteroid belt. It must be the Ceres monitoring station!

In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest
BOOST program - Basic Operation Of System Test.

While BOOST (your puzzle input) is capable of boosting your sensors, for tenuous safety reasons, it
refuses to do so until the computer it runs on passes some checks to demonstrate it is a complete
Intcode computer.

Your existing Intcode computer is missing one key feature: it needs support for parameters in
relative mode.

Parameters in mode 2, relative mode, behave very similarly to parameters in position mode: the
parameter is interpreted as a position. Like position mode, parameters in relative mode can be read
from or written to.

The important difference is that relative mode parameters don't count from address 0. Instead,
they count from a value called the relative base. The relative base starts at 0.

The address a relative mode parameter refers to is itself plus the current relative base. When
the relative base is 0, relative mode parameters and position mode parameters with the same value
refer to the same address.

For example, given a relative base of 50, a relative mode parameter of -7 refers to memory
address 50 + -7 = 43.

The relative base is modified with the relative base offset instruction:

Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases
(or decreases, if the value is negative) by the value of the parameter.

For example, if the relative base is 2000, then after the instruction 109,19, the relative base
would be 2019. If the next instruction were 204,-34, then the value at address 1985 would be output.

Your Intcode computer will also need a few other capabilities:

The computer's available memory should be much larger than the initial program. Memory beyond the
initial program starts with the value 0 and can be read or written like any other memory. (It is
invalid to try to access memory at a negative address, though.)

The computer should have support for large numbers. Some instructions near the beginning of the BOOST
program will verify this capability.

Here are some example programs that use these features:

109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy of
itself as output.

1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
104,1125899906842624,99 should output the large number in the middle.

The BOOST program will ask for a single input; run it in test mode by providing it the value 1. It will
perform a series of checks on each opcode, output any opcodes (and the associated parameter modes) that
seem to be functioning incorrectly, and finally output a BOOST keycode.

Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning
opcodes when run in test mode; it should only output a single value, the BOOST keycode. What BOOST
keycode does it produce?
"""

### IMPORTS ###


### CONSTANTS ###

OP_ADD				= 1
OP_MULT				= 2
OP_INPUT				= 3
OP_OUTPUT			= 4
OP_JUMP_IF_TRUE	= 5
OP_JUMP_IF_FALSE	= 6
OP_IS_LESS_THAN	= 7
OP_IS_EQUAL			= 8
OP_REL_BASE_SHIFT	= 9
OP_HALT				= 99

OP_NAMES	= {
	OP_ADD:					'Add',
	OP_MULT: 				'Mult',
	OP_INPUT: 				'Input',
	OP_OUTPUT: 				'Output',
	OP_JUMP_IF_TRUE: 		'Jump if True',
	OP_JUMP_IF_FALSE: 	'Jump if False',
	OP_IS_LESS_THAN: 		'Is Less Than',
	OP_IS_EQUAL:			'Is Equal',
	OP_REL_BASE_SHIFT:	'Relative Base Shift',
	OP_HALT:					'Halt',
}

MODE_POSITION	= 0
MODE_IMMEDIATE	= 1
MODE_RELATIVE	= 2



### FUNCTIONS ###

def get_params( codes, i, relative_base, param_modes ):
	params = [ ]
	i += 1

	for mode in param_modes:
		if mode == MODE_POSITION:
			idx = codes.get( i, 0 )
			params.append( codes.get( idx, 0 ) )
		elif mode == MODE_IMMEDIATE:
			params.append( codes.get( i, 0 ) )
		elif mode == MODE_RELATIVE:
			print( 'i = {0}, codes[ i ] = {1}, rel_base = {2}'.format( i, codes.get( i, 0 ), relative_base ) )
			idx = codes.get( i, 0 ) + relative_base
			val = codes.get( idx, 0 )
			print( 'idx = {0}, val = {1}'.format( idx, val ) )
			params.append( val )

		i += 1

	return params


### CLASSES ###

class Computer( ):
	def __init__( self, program, inputs ):
		self._program = program
		self._inputs = inputs

		self.output = None

		self._codes = self._parse_program( )


	def _parse_program( self ):
		vals = [ int( n ) for n in self._program.split( ',' ) ]
		codes = { }
		idx = 0

		for v in vals:
			codes[ idx ] = v
			idx += 1

		return codes


	def run( self ):
		codes = self._codes
		output = None
		input_idx = 0
		relative_base = 0

		i = 0

		while True:
			print( 'i =', i )
			print( 'codes1 =', ','.join( [ str( x ) for x in list( codes.values( ) )[ i:i+4 ] ] ) )

			# parse instructions
			op_str = ( '0000' + str( codes.get( i, 0 ) ) )[ -5: ]
			print( 'op_str =', op_str )

			opcode = int( op_str[ 3: ] )
			print( 'opcode = {0}, {1}'.format( opcode, OP_NAMES[ opcode ] ) )

			if opcode == OP_HALT:
				break

			param_modes = list( reversed( [ int( m ) for m in op_str[ :3 ] ] ) )

			if opcode in ( OP_INPUT, OP_OUTPUT, OP_REL_BASE_SHIFT ):
				# Only need one param for these
				param_modes = param_modes[ :1 ]
			elif opcode in ( OP_JUMP_IF_TRUE, OP_JUMP_IF_FALSE ):
				# Only need two params for these
				param_modes = param_modes[ :2 ]

			print( 'param_modes =', param_modes )

			params = get_params( codes, i, relative_base, param_modes )
			print( 'params =', params )

			if opcode == OP_ADD:
				val = params[ 0 ] + params[ 1 ]
				idx = codes.get( i+3, 0 )
				print( 'Adding {0} + {1} = {2}, writing to idx {3}'.format( params[ 0 ], params[ 1 ], val, idx ) )
				codes[ idx ] = val
				i += 4

			elif opcode == OP_MULT:
				val = params[ 0 ] * params[ 1 ]
				idx = codes.get( i+3, 0 )
				print( 'Mult {0} * {1} = {2}, writing to idx {3}'.format( params[ 0 ], params[ 1 ], val, idx ) )
				codes[ idx ] = val
				i += 4

			elif opcode == OP_INPUT:
				idx = params[ 0 ]
				print( 'Writing input value {0} to idx {1}'.format( self._inputs[ input_idx ], idx ) )
				codes[ idx ] = self._inputs[ input_idx ]
				i += 2
				input_idx += 1

			elif opcode == OP_OUTPUT:
				#output = codes.get( codes.get( i+1, 0 ), 0 )
				output = params[ 0 ]
				print( 'output =', output )
				i += 2

			elif opcode == OP_JUMP_IF_TRUE:
				if params[ 0 ]:
					print( 'Value {0} is True, jumping to {1}'.format( params[ 0 ], params[ 1 ] ) )
					i = params[ 1 ]
				else:
					print( 'Value {0} is False, not jumping'.format( params[ 0 ] ) )
					i += 3

			elif opcode == OP_JUMP_IF_FALSE:
				if not params[ 0 ]:
					print( 'Value {0} is False, jumping to {1}'.format( params[ 0 ], params[ 1 ] ) )
					i = params[ 1 ]
				else:
					print( 'Value {0} is True, not jumping'.format( params[ 0 ] ) )
					i += 3

			elif opcode == OP_IS_LESS_THAN:
				#idx = codes.get( i+3, 0 )
				idx = params[ 2 ]

				if params[ 0 ] < params[ 1 ]:
					print( 'Value {0} is less than {1}, writing 1 to idx {2}'.format( params[ 0 ], params[ 1 ], idx ) )
					codes[ idx ] = 1
				else:
					print( 'Value {0} is not less than {1}, writing 0 to idx {2}'.format( params[ 0 ], params[ 1 ], idx ) )
					codes[ idx ] = 0

				i += 4

			elif opcode == OP_IS_EQUAL:
				#idx = codes.get( i+3, 0 )
				idx = params[ 2 ]

				if params[ 0 ] == params[ 1 ]:
					print( 'Value {0} is equal to {1}, writing 1 to idx {2}'.format( params[ 0 ], params[ 1 ], idx ) )
					codes[ idx ] = 1
				else:
					print( 'Value {0} is not equal to {1}, writing 0 to idx {2}'.format( params[ 0 ], params[ 1 ], idx ) )
					codes[ idx ] = 0

				i += 4

			elif opcode == OP_REL_BASE_SHIFT:
				print( 'Shifting relative base {0} + {1} = {2}'.format( relative_base, params[ 0 ], relative_base + params[ 0 ] ) )
				relative_base += params[ 0 ]
				i += 2

			#print( 'codes2 =', ','.join( [ str( x ) for x in codes.values( ) ] ) )
			print( '---' )

		#print( 'OUTPUT =', output )

		self.output = output
		self._codes = codes

		return output


### MAIN ###

if __name__ == "__main__":
	program = open( 'input1.txt', 'r' ).read( )

	comp = Computer( program, [ 1 ] )
	output = comp.run( )

	print( '\nOUTPUT =', output )

# answer
# 43210
