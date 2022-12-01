"""
--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, 
you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of 
addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses 
indicate that the expression inside must be evaluated before it can be used by the surrounding 
expression. Addition still finds the sum of the numbers on both sides of the operator, and 
multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication 
before addition, the operators have the same precedence, and are evaluated left-to-right regardless 
of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 
1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
			
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself. 
Evaluate the expression on each line of the homework; what is the sum of the resulting values?
"""

### IMPORTS ###

import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'


### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	return lines
			

def evaluate_recurse( section ):
	"""
	((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
	
	(2 + 4 * 9)
	(6 + 9 * 8 + 6)
	(A * B + 6)
	C + 2 + 4 * 2
	"""
	
	


def main( lines ):
	a = New_Int( 3 )
	b = New_Int( 8 )
	print( a + b )
	
	return total
	

### CLASSES ###

class New_Int( int ):
	def __add__( self, other ):
		return int( self ) * other
	
	def __radd__( self, other ):
		return self.__add__( other )
	
	#def __mul__( self, other ):
		#if isinstance( other, ( int, float ) ):
			#return __class__( self.data * other )
		#else:
			#return foo(self.data * other.data)
"""
a = tInt(2)
print (a + "5")
print ("5" + a)
"""

### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	lines = parse_input( )
	answer = main( lines )
	
	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 756 too low
