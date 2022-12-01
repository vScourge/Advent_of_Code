def pathfind( start, goal ):
	"""
	http://ai-depot.com/Tutorial/PathFinding.html
	https://web.archive.org/web/20200204071343/http://ai-depot.com/Tutorial/PathFinding.html
	"""

	paths = [ ( start, ) ]

	while True:
		cur_path = paths.pop( 0 )
		new_paths = [ ]

		# Get links for spot on end of list, but get them in
		# "reading order".
		#if cur_path[ -1 ].links:
			#links = cur_path[ -1 ].links + [ cur_path[ -1 ].links ]
		#else:
			#links = [ cur_path[ -1 ].links ]

		links = cur_path[ -1 ].links

		#links = [ l for l in cur_path[ -1 ].links.values( ) if l and l.contents == EMPTY ]

		for link in links:
			new_paths.append( tuple( list( cur_path ) + [ link ] ) )

		# Remove any with loops
		#new_paths = [ p for p in new_paths if len( set( p ) ) == len( p ) ]

		# If we're looking for the shortest path...
		# Sort new paths by distance from last node to goal node
		#new_paths = sorted( new_paths, key = lambda p: len( p ) )

		paths += new_paths

		# If we run out of paths, we've failed
		if not paths:
			return [ ]

		# If a path has the goal at end, we've succeeded
		for path in paths:
			if path[ -1 ] == goal:
				return path
