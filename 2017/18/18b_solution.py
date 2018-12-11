"""
Advent of Code 2017

input is: input.txt
answer is 5969?

set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.
"""

import string
import queue

PROG1 = 0
PROG2 = 1

class Prog( ):
	def __init__( self, id, cmds ):
		self.id = id
		self.cmds = cmds

		self.reg = { }

		for x in string.ascii_lowercase:
			self.reg[ x ] = 0

		self.reg[ 'p' ] = self.id

		self.cmd_idx = 0
		self.q = queue.Queue( )
		self.receiving = False
		self.other_prog = None
		self.cmds_sent = 0
		self.terminated = False


	def check_for_terminate( self ):
		if self.cmd_idx >= len( self.cmds ) or self.cmd_idx < 0:
			self.terminated = True


	def process( self ):
		instr = self.cmds[ self.cmd_idx ]

		print( 'prog{0} "{1}", idx = {2}, q = {3}, sent = {4}'.format( self.id + 1, instr, self.cmd_idx, self.q.qsize( ), self.cmds_sent ) )

		ins = instr.split( ' ' )
		cmd = ins[ 0 ]
		arg1 = ins[ 1 ]

		if cmd == 'snd':
			self.other_prog.q.put( int( self.reg[ arg1 ] ) )
			self.cmds_sent += 1
			self.cmd_idx += 1
			return

		if cmd == 'rcv':
			if self.q.empty( ):
				self.receiving = True
				return

			self.reg[ arg1 ] = int( self.q.get_nowait( ) )
			self.receiving = False

			self.cmd_idx += 1
			return

		if ins[ 2 ].isalpha( ):
			arg2 = self.reg[ ins[ 2 ] ]
		else:
			arg2 = int( ins[ 2 ] )

		if cmd == 'set':
			self.reg[ arg1 ] = arg2

		if cmd == 'add':
			self.reg[ arg1 ] += arg2

		if cmd == 'mul':
			self.reg[ arg1 ] *= arg2

		if cmd == 'mod':
			self.reg[ arg1 ] = self.reg[ arg1 ] % arg2

		elif cmd == 'jgz':
			if arg1.isalpha( ):
				arg1 = self.reg[ arg1 ]
			else:
				arg1 = int( arg1 )

			if arg1:
				self.cmd_idx += arg2
				return

		self.cmd_idx += 1


def main( ):
	data = open( 'input.txt', 'r' ).read( ).split( '\n' )

	prog1 = Prog( 0, data )
	prog2 = Prog( 1, data )

	prog1.other_prog = prog2
	prog2.other_prog = prog1

	while True:
		if not prog1.terminated:
			prog1.process( )
		if not prog1.terminated:
			prog2.process( )

		# check for termination
		prog1.check_for_terminate( )
		prog2.check_for_terminate( )

		# check for deadlock
		if prog1.receiving and prog2.receiving:
			break

		if prog1.cmds_sent > 5975:
			print( 'FAILED' )
			break

	print( 'prog1 sends =', prog1.cmds_sent )


if __name__ == '__main__':
	main( )

	print( 'done' )

