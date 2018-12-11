"""
Advent of Code 2017

input is: input.txt

answer is 3834136

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


def scanner_pos_at_round( layer, round_num ):
	"""
	Predict where a scanner will be at a certain round number
	"""
	pos = round_num % ( layer.range * 2 - 2 )
	return pos
		


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
	
	delay = 0
	depths = sorted( layers.keys( ) )
	
	while True:
		made_it = True
		
		for depth in depths:
			layer = layers[ depth ]
			round_num = delay + depth
			
			if scanner_pos_at_round( layer, round_num ) == 0:
				print( 'Caught depth {0} round {1}'.format( layer.depth, round_num ) )
				made_it = False
				delay += 1
				break

		if made_it:
			# success!
			break
    
	print( 'delay =', delay )                    
	print( 'done' )