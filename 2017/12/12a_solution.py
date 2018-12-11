"""
Advent of Code 2017

input is: input.txt

0 <-> 454, 528, 621, 1023, 1199

answer is 378
"""

class Node( ):
	def __init__( self, id, links ):
		self.id = id
		self.links = links
		self.group = None


	def __repr__( self ):
		return '<Node {0}>'.format( self.id )


temp_nodes = [ ]

def get_links_recurse( node ):
	global temp_nodes
	
	if node in temp_nodes:
		# Already did this one
		return [ ]
	else:
		temp_nodes.append( node )
	
	links = [ ]
	for l_node in node.links:
		links.extend( get_links_recurse( l_node ) )

	links.append( node )
		
	return list( set( links ) )
	

if __name__ == '__main__':
	nodes = { }
	groups = { }
	
	for line in open( 'input.txt', 'r' ):
		line_split = line.strip( ).split( ' ' )
		
		# Make all our nodes using link IDs for now
		node_id = int( line_split[ 0 ].strip( ) )
		links = [ int( x.strip( ',' ) ) for x in line_split[ 2: ] ]

		node = Node( node_id, links )
		nodes[ node_id ] = node
		
	# Turn link IDs into nodes
	for node_id, node in nodes.items( ):
		link_nodes = [ ]
		for link_id in node.links:
			link_nodes.append( nodes[ link_id ] )
			
		node.links = link_nodes

	
	group_0 = get_links_recurse( node )

	print( 'group zero members =', len( group_0 ) )
	
	print( 'done' )