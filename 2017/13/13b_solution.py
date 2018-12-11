"""
Advent of Code 2017

input is: input.txt


"""

DIR_DOWN	= 0
DIR_UP		= 1


class Layer( ):
	def __init__( self, depth, range ):
		self.depth = depth
		self.range = range

		self.scan_pos = 0
		self.scan_dir = DIR_DOWN


	def move( self ):
		if self.scan_dir == DIR_DOWN:
			self.scan_pos += 1

			if self.scan_pos == self.range - 1:
				self.scan_dir = DIR_UP
		else:
			self.scan_pos -= 1
			
			if self.scan_pos == 0:
				self.scan_dir = DIR_DOWN


	def __repr__( self ):
		return '<Layer {0}>'.format( self.depth )


def delay_then_run( layers, delay ):
	pos = -1
	count = 0

	# Reset all scanners
	for layer_id in layers:
		layer = layers[ layer_id ]
		layer.scan_pos = 0
		layer.scan_dir = DIR_DOWN
		
	while pos <= max_depth:
		if count >= delay:
			pos += 1

		if pos in layers:
			layer = layers[ pos ]

			if layers[ pos ].scan_pos == 0:
				print( 'delay {0}, caught on layer {1}'.format( delay, pos ) )
				return False

		# move all scanners
		for layer in layers.values( ):
			layer.move( )

		count += 1

	return True


if __name__ == '__main__':
	layers = { }
	max_depth = 0
	
	# Build dict of layer objects
	for line in open( 'input.txt', 'r' ):
		split = line.split( ':' )
		
		layer_depth = int( split[ 0 ] )
		layer_range = int( split[ 1 ].strip( ) )
	
		layers[ layer_depth ] = Layer( layer_depth, layer_range )
		
		max_depth = max( max_depth, layer_depth )
	
	# Delay N picoseconds before run, and keep repeating with longer
	# delays until we make it across
	delay = 0
	
	while True:
		success = delay_then_run( layers, delay )
		
		if success:
			break
		
		delay += 1
		        
	print( 'delay =', delay )                    
	print( 'done' )