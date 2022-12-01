"""
--- Day 14: Docking Data ---
As your ferry approaches the sea port, the captain asks for your help again. The computer system that 
runs this port isn't compatible with the docking program on the ferry, so the docking parameters aren't 
being correctly initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses a strange bitmask system 
in its initialization program. Although you don't have the correct decoder chip handy, you can emulate 
it in software!

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. 
Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, 
a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) 
on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is 
applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit 
in the value, while an X leaves the bit in the value unchanged.

For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0

This program starts by specifying a bitmask (mask = ....). The mask it specifies will overwrite two bits in 
every written value: the 2s bit is overwritten with 0, and the 64s bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual 
bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)

So, because of the mask, the value 73 is written to memory address 8 instead. Then, the program tries to 
write 101 to address 7:

value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)

This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. 
Finally, the program tries to write 0 to address 8:

value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)

64 is written to address 8 instead, overwriting the value that was there previously.

To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization 
program completes. (The entire 36-bit address space begins initialized to the value 0 at every address.) In the 
above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a 
sum of 165.

Execute the initialization program. What is the sum of all values left in memory after it completes?
"""

### IMPORTS ###

import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'


### FUNCTIONS ###


	

### CLASSES ###


### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )
	
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	mask = None
	memory = { }
	i = 0
	
	while True:
		# Get new mask
		mask = lines[ i ].split( ' = ' )[ -1 ]
		i += 1
		
		print( '---' )
		
		# Loop through values lines
		while i < len( lines ) and 'mask' not in lines[ i ]:
			line = lines[ i ]

			# Parse out value and address
			parts = line.split( ' ' )
			value_dec = int( parts[ -1 ] )
			address = int( parts[ 0 ].split( '[' )[ 1 ][ :-1 ] )
			
			# Convert decimal to binary string
			value_bin_short = numpy.binary_repr( value_dec )
			value_bin = '0' * ( 36 - len( value_bin_short ) ) + value_bin_short
		
			print( 'value  = {0}'.format( value_bin ) )
			print( 'mask   = {0}'.format( mask ) )
			
			# Apply mask to value
			value_list = [ ]
			for j in range( len( value_bin ) ):
				if mask[ j ] == 'X':
					value_list.append( value_bin[ j ] )
				else:
					value_list.append( mask[ j ] )

			print( 'appl   = {0}'.format( ''.join( value_list ) ) )
			       
			#value_new = ''.join( value_list )
			
			# convert from binary string to decimal
			#value_np = numpy.array( [ int( x ) for x in value_list ] )
			#value_new = value_np.dot( 2 ** numpy.arange( value_np.size )[ ::-1 ] )
			
			pow_val = 0
			value_new = 0
			for j in range( 35, -1, -1 ):
				if value_list[ j ] == '1':
					value_new += pow( 2, pow_val )
				pow_val += 1
			
			print( 'result = {0}\n'.format( ''.join( value_list ) ) )
			print( 'value  = {0}'.format( value_new ) )
		
			# Write new value to memory
			memory[ address ] = value_new
			print( memory )
			
			i += 1
			
		if i >= len( lines ):
			break

	answer = sum( memory.values( ) )
	
	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 1060151173 too low
