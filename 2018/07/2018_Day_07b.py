"""
Step X must be finished before step Z can begin.
"""

import string

### CLASSES ###

class Elf( ):
	def __init__( self, id ):
		self.id = id
		self.step = None
		self.secs_left = 0
		
	def __repr__( self ):
		return '<Elf {0},{1}>'.format( self.id, self.step )

		
class Step( ):
	def __init__( self, id ):
		self.id = id
		self.reqs = [ ]	# Other steps that are prerequisites
		self.elf = None
		
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

def get_available_elf( elves ):
	for id, elf in elves.items( ):
		if not elf.step:
			return elf
		
	return None
		
	
### MAIN ###

if __name__ == "__main__":
	steps = parse_input( )
	
	elves = { }
	for i in range( 5 ):
		elves[ i ] = Elf( i )
	
	total_secs = 0
	
	while steps:
		print( '---------' )
		print( total_secs, len( steps ) )
		for elf in elves.values( ):
			if elf.step:
				print( elf, elf.secs_left )
				
		#for key in sorted( steps.keys( ) ):
			#print( '{0} - {1}'.format( key, steps[ key ].reqs ) )

		# tick down secs on elves that are busy
		for elf in elves.values( ):
			if elf.step:
				elf.secs_left -= 1

				if elf.secs_left == 0:
					steps.pop( elf.step )
					elf.step = None
					steps = remove_completed_reqs( steps )
			
		for key in sorted( steps.keys( ) ):
			step = steps[ key ]

			if not step.reqs and step.elf is None:
				# get elf to start this step
				elf = get_available_elf( elves )

				if elf:
					elf.step = step.id
					step.elf = elf.id
					elf.secs_left = 60 + string.ascii_uppercase.index( step.id ) + 1

		total_secs += 1


	print( total_secs - 1 )
	
	print( 'done' )