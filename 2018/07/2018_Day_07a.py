"""
Step X must be finished before step Z can begin.
"""

import string

### CLASSES ###

class Step( ):
	def __init__( self, id ):
		self.id = id
		self.reqs = [ ]	# Other steps that are prerequisites
		
	def __repr__( self ):
		return '<Step {0}>'.format( self.id )
		
		

### FUNCTIONS ###

def parse_input( ):
	steps = { }
	
	for line in open( 'input.txt', 'r' ):
		id = line[ 36 ]
		req = line[ 5 ]
		
		step = steps.get( id )
		
		if not step:
			step = Step( id )
			steps[ id ] = step
			
			if req not in steps:
				steps[ req ] = Step( req )
			
		step.reqs.append( req )
		
	
	for id in steps:
		steps[ id ].reqs = sorted( steps[ id ].reqs )

	return steps

def remove_completed_reqs( steps ):
	for id, step in steps.items( ):
		temp_list = [ ]
		for req in step.reqs:
			if req in steps:
				temp_list.append( req )
				
		step.reqs = temp_list
	
	return steps

	
### MAIN ###

if __name__ == "__main__":
	steps = parse_input( )
	ordered_steps = [ ]
	
	while steps:
		print( '---------' )
		for key in sorted( steps.keys( ) ):
			print( '{0} - {1}'.format( key, steps[ key ].reqs ) )
			
		for key in sorted( steps.keys( ) ):
			step = steps[ key ]

			if not step.reqs:
				ordered_steps.append( key )
				steps.pop( key )
				steps = remove_completed_reqs( steps )
				break


	print( ''.join( ordered_steps ) )
	
	print( 'done' )