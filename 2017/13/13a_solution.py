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
	
	pos = 0
	severity = 0
	
	while pos <= max_depth:
		if pos in layers:
			layer = layers[ pos ]

			if layers[ pos ].scan_pos == 0:
				# Caught!
				severity += layer.depth * layer.range

		# move all scanners
		for layer in layers.values( ):
			layer.move( )
			
		pos += 1
		        
	print( 'severity =', severity )                    
	print( 'done' )