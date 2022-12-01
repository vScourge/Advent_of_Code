"""
--- Day 7: Amplification Circuit ---
Based on the navigational maps, you're going to need to send more power to your ship's thrusters to reach Santa in time.
To do this, you'll need to configure a series of amplifiers already installed on the ship.

There are five amplifiers connected in series; each one receives an input signal and produces an output signal. They are
connected such that the first amplifier's output leads to the second amplifier's input, the second amplifier's output leads
to the third amplifier's input, and so on. The first amplifier's input value is 0, and the last amplifier's output leads
to your ship's thrusters.

    O-------O  O-------O  O-------O  O-------O  O-------O
0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O

The Elves have sent you some Amplifier Controller Software (your puzzle input), a program that should run on your existing
Intcode computer. Each amplifier will need to run a copy of the program.

When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier for
its current phase setting (an integer from 0 to 4). Each phase setting is used exactly once, but the Elves can't remember
which amplifier needs which phase setting.

The program will then call another input instruction to get the amplifier's input signal, compute the correct output signal,
and supply it back to the amplifier with an output instruction. (If the amplifier has not yet received an input signal, it
waits until one arrives.)

Your job is to find the largest output signal that can be sent to the thrusters by trying every possible combination of phase
settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.

For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which would mean setting amplifier A to phase
setting 3, amplifier B to setting 1, C to 2, D to 4, and E to 0. Then, you could determine the output signal that gets sent
from amplifier E to the thrusters with the following steps:

Start the copy of the amplifier controller software that will run on amplifier A. At its first input instruction, provide
it the amplifier's phase setting, 3. At its second input instruction, provide it the input signal, 0. After some
calculations, it will use an output instruction to indicate the amplifier's output signal.

Start the software for amplifier B. Provide it the phase setting (1) and then whatever output signal was produced from
amplifier A. It will then produce a new output signal destined for amplifier C.

Start the software for amplifier C, provide the phase setting (2) and the value from amplifier B, then collect its output signal.

Run amplifier D's software, provide the phase setting (4) and input value, and collect its output signal.

Run amplifier E's software, provide the phase setting (0) and input value, and collect its output signal.

The final output signal from amplifier E would be sent to the thrusters. However, this phase setting sequence may not
have been the best one; another sequence might have sent a higher signal to the thrusters.

Here are some example programs:

Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0

Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0

Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0

Try every combination of phase settings on the amplifiers. What is the highest signal that can be sent to the thrusters?
"""

### IMPORTS ###

import itertools


### CONSTANTS ###

OP_ADD				= 1
OP_MULT				= 2
OP_INPUT				= 3
OP_OUTPUT			= 4
OP_JUMP_IF_TRUE	= 5
OP_JUMP_IF_FALSE	= 6
OP_IS_LESS_THAN	= 7
OP_IS_EQUAL			= 8
OP_HALT				= 99

MODE_POSITION	= 0
MODE_IMMEDIATE	= 1


### FUNCTIONS ###

def get_params( codes, i, param_modes ):
	params = [ ]
	i += 1

	for mode in param_modes:
		if mode == MODE_POSITION:
			idx = codes[ i ]
			params.append( codes[ idx ] )
		elif mode == MODE_IMMEDIATE:
			params.append( codes[ i ] )

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

		i = 0

		while True:
			#print( 'codes1 =', ','.join( [ str( x ) for x in codes.values( ) ] ) )
			#print( 'i =', i )

			# parse instructions
			op_str = ( '0000' + str( codes[ i ] ) )[ -5: ]
			#print( 'op_str =', op_str )

			opcode = int( op_str[ 3: ] )
			#print( 'opcode =', opcode )

			if opcode == OP_HALT:
				break

			param_modes = list( reversed( [ int( m ) for m in op_str[ :3 ] ] ) )

			if opcode in ( OP_INPUT, OP_OUTPUT ):
				# Only need one param for these
				param_modes = param_modes[ :1 ]
			elif opcode in ( OP_JUMP_IF_TRUE, OP_JUMP_IF_FALSE ):
				# Only need two params for these
				param_modes = param_modes[ :2 ]

			#print( 'param_modes =', param_modes )

			params = get_params( codes, i, param_modes )
			#print( 'params =', params )

			if opcode == OP_ADD:
				val = params[ 0 ] + params[ 1 ]
				codes[ codes[ i+3 ] ] = val
				i += 4

			elif opcode == OP_MULT:
				val = params[ 0 ] * params[ 1 ]
				codes[ codes[ i+3 ] ] = val
				i += 4

			elif opcode == OP_INPUT:
				codes[ codes[ i+1 ] ] = self._inputs[ input_idx ]
				i += 2
				input_idx += 1

			elif opcode == OP_OUTPUT:
				output = codes[ codes[ i+1 ] ]
				#print( 'output =', output )
				i += 2

			elif opcode == OP_JUMP_IF_TRUE:
				if params[ 0 ]:
					i = params[ 1 ]
				else:
					i += 3

			elif opcode == OP_JUMP_IF_FALSE:
				if not params[ 0 ]:
					i = params[ 1 ]
				else:
					i += 3

			elif opcode == OP_IS_LESS_THAN:
				if params[ 0 ] < params[ 1 ]:
					codes[ codes[ i+3 ] ] = 1
				else:
					codes[ codes[ i+3 ] ] = 0

				i += 4

			elif opcode == OP_IS_EQUAL:
				if params[ 0 ] == params[ 1 ]:
					codes[ codes[ i+3 ] ] = 1
				else:
					codes[ codes[ i+3 ] ] = 0

				i += 4

			#print( 'codes2 =', ','.join( [ str( x ) for x in codes.values( ) ] ) )
			#print( '---' )

		#print( 'OUTPUT =', output )

		self.output = output
		self._codes = codes

		return output


### MAIN ###

if __name__ == "__main__":
	max_signal = 0
	program = open( 'input.txt', 'r' ).read( )
	phases = [ 0, 1, 2, 3, 4 ]

	for phases_perm in itertools.permutations( phases ):
		cur_signal = 0
		for phase in phases_perm:
			comp = Computer( program, [ phase, cur_signal ] )
			cur_signal = comp.run( )

		if cur_signal > max_signal:
			max_signal = cur_signal


	print( 'max signal =', max_signal )

# answer
# 43210
