"""
Advent of Code 2017

input is: input.txt
answer is 

snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

"""

import string

if __name__ == '__main__':
	data = open( 'input.txt', 'r' ).read( ).split( '\n' )
	reg = { }
	
	for l in string.ascii_lowercase:
		reg[ l ] = 0
		
	last_snd = None
	i = 0

	
	while True:
		instr = data[ i ]
		
		ins = instr.split( ' ' )
		cmd = ins[ 0 ]
		arg1 = ins[ 1 ]
		
		print( 'cmd =', cmd )
		
		if cmd == 'snd':
			last_snd = reg[ arg1 ]
			i += 1
			continue

		if cmd == 'rcv':
			if reg[ arg1 ]:
				print( 'sound =', last_snd )
				break

		if ins[ 2 ].isalpha( ):
			arg2 = reg[ ins[ 2 ] ]
		else:
			arg2 = int( ins[ 2 ] )
		
		if cmd == 'set':
			reg[ arg1 ] = arg2
			
		if cmd == 'add':
			reg[ arg1 ] += arg2
			
		if cmd == 'mul':
			reg[ arg1 ] *= arg2
			
		if cmd == 'mod':
			reg[ arg1 ] = reg[ arg1 ] % arg2
		
		elif cmd == 'jgz':
			if reg[ arg1 ]:
				i += arg2
				continue
			
		i += 1
		
		
	
	print( 'done' )

