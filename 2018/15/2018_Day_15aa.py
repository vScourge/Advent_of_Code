r"""
--- Day 15: Beverage Bandits ---
Having perfected their hot chocolate, the Elves have a new problem: the Goblins that live in these caves will
do anything to steal it. Looks like they're here for a fight.

You scan the area, generating a map of the walls (#), open cavern (.), and starting position of every Goblin (G)
and Elf (E) (your puzzle input).

Combat proceeds in rounds; in each round, each unit that is still alive takes a turn, resolving all of its actions
before the next unit's turn begins. On each unit's turn, it tries to move into range of an enemy (if it isn't
already) and then attack (if it is in range).

All units are very disciplined and always follow very strict combat rules. Units never move or attack diagonally,
as doing so would be dishonorable. When multiple choices are equally valid, ties are broken in reading order:
top-to-bottom, then left-to-right. For instance, the order in which units take their turns within a round is the
reading order of their starting positions in that round, regardless of the type of unit or whether other units
have moved after the round started. For example:

                 would take their
These units:   turns in this order:
  #######           #######
  #.G.E.#           #.1.2.#
  #E.G.E#           #3.4.5#
  #.G.E.#           #.6.7.#
  #######           #######
Each unit begins its turn by identifying all possible targets (enemy units). If no targets remain, combat ends.

Then, the unit identifies all of the open squares (.) that are in range of each target; these are the squares
which are adjacent (immediately up, down, left, or right) to any target and which aren't already occupied by a
wall or another unit. Alternatively, the unit might already be in range of a target. If the unit is not already
in range of a target, and there are no open squares which are in range of a target, the unit ends its turn.

If the unit is already in range of a target, it does not move, but continues its turn with an attack.
Otherwise, since it is not in range of a target, it moves.

To move, the unit first considers the squares that are in range and determines which of those squares it could
reach in the fewest steps. A step is a single movement to any adjacent (immediately up, down, left, or right)
open (.) square. Units cannot move into walls or other units. The unit does this while considering the current
positions of units and does not do any prediction about where units will be later. If the unit cannot reach
(find an open path to) any of the squares that are in range, it ends its turn. If multiple squares are in range
and tied for being reachable in the fewest steps, the square which is first in reading order is chosen.
For example:

Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######
In the above scenario, the Elf has three targets (the three Goblins):

Each of the Goblins has open, adjacent squares which are in range (marked with a ? on the map).

Of those squares, four are reachable (marked @); the other two (on the right) would require moving through
a wall or unit to reach.

Three of these reachable squares are nearest, requiring the fewest steps (only 2) to reach (marked !).

Of those, the square which is first in reading order is chosen (+).

The unit then takes a single step toward the chosen square along the shortest path to that square. If
 multiple steps would put the unit equally closer to its destination, the unit chooses the step which is
 first in reading order. (This requires knowing when there is more than one shortest path so that you can
 consider the first step of each such path.) For example:

In range:     Nearest:      Chosen:       Distance:     Step:
#######       #######       #######       #######       #######
#.E...#       #.E...#       #.E...#       #4E212#       #..E..#
#...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
#..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
#######       #######       #######       #######       #######
The Elf sees three squares in range of a target (?), two of which are nearest (!), and so the first in
reading order is chosen (+). Under "Distance", each open square is marked with its distance from the
destination square; the two squares to which the Elf could move on this turn (down and to the right)
are both equally good moves and would leave the Elf 2 steps from being in range of the Goblin. Because
the step which is first in reading order is chosen, the Elf moves right one square.

Here's a larger example of movement:

Initially:
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########

After 1 round:
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########

After 2 rounds:
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########

After 3 rounds:
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########
Once the Goblins and Elf reach the positions above, they all are either in range of a target or cannot
find any square in range of a target, and so none of the units can move until a unit dies.

After moving (or if the unit began its turn in range of a target), the unit attacks.

To attack, the unit first determines all of the targets that are in range of it by being immediately
adjacent to it. If there are no such targets, the unit ends its turn. Otherwise, the adjacent target
with the fewest hit points is selected; in a tie, the adjacent target with the fewest hit points which
is first in reading order is selected.

The unit deals damage equal to its attack power to the selected target, reducing its hit points by that
amount. If this reduces its hit points to 0 or fewer, the selected target dies: its square becomes . and
it takes no further turns.

Each unit, either Goblin or Elf, has 3 attack power and starts with 200 hit points.

For example, suppose the only Elf is about to attack:

       HP:            HP:
G....  9       G....  9
..G..  4       ..G..  4
..EG.  2  -->  ..E..
..G..  2       ..G..  2
...G.  1       ...G.  1
The "HP" column shows the hit points of the Goblin to the left in the corresponding row. The Elf is in
range of three targets: the Goblin above it (with 4 hit points), the Goblin to its right (with 2 hit
points), and the Goblin below it (also with 2 hit points). Because three targets are in range, the ones
with the lowest hit points are selected: the two Goblins with 2 hit points each (one to the right of the
	Elf and one below the Elf). Of those, the Goblin first in reading order (the one to the right of the
	Elf) is selected. The selected Goblin's hit points (2) are reduced by the Elf's attack power (3),
	reducing its hit points to -1, killing it.

After attacking, the unit's turn ends. Regardless of how the unit's turn ends, the next unit in the round
takes its turn. If all units have taken turns in this round, the round ends, and a new round begins.

The Elves look quite outnumbered. You need to determine the outcome of the battle: the number of full
rounds that were completed (not counting the round in which combat ends) multiplied by the sum of the
hit points of all remaining units at the moment combat ends. (Combat only ends when a unit finds no
targets during its turn.)

Below is an entire sample combat. Next to each map, each row's units' hit points are listed from
left to right.

Initially:
#######
#.G...#   G(200)
#...EG#   E(200), G(200)
#.#.#G#   G(200)
#..G#E#   G(200), E(200)
#.....#
#######

After 1 round:
#######
#..G..#   G(200)
#...EG#   E(197), G(197)
#.#G#G#   G(200), G(197)
#...#E#   E(197)
#.....#
#######

After 2 rounds:
#######
#...G.#   G(200)
#..GEG#   G(200), E(188), G(194)
#.#.#G#   G(194)
#...#E#   E(194)
#.....#
#######

Combat ensues; eventually, the top Elf dies:

After 23 rounds:
#######
#...G.#   G(200)
#..G.G#   G(200), G(131)
#.#.#G#   G(131)
#...#E#   E(131)
#.....#
#######

After 24 rounds:
#######
#..G..#   G(200)
#...G.#   G(131)
#.#G#G#   G(200), G(128)
#...#E#   E(128)
#.....#
#######

After 25 rounds:
#######
#.G...#   G(200)
#..G..#   G(131)
#.#.#G#   G(125)
#..G#E#   G(200), E(125)
#.....#
#######

After 26 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(122)
#...#E#   E(122)
#..G..#   G(200)
#######

After 27 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(119)
#...#E#   E(119)
#...G.#   G(200)
#######

After 28 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(116)
#...#E#   E(113)
#....G#   G(200)
#######

More combat ensues; eventually, the bottom Elf dies:

After 47 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(59)
#...#.#
#....G#   G(200)
#######
Before the 48th round can finish, the top-left Goblin finds that there are no targets remaining, and so
combat ends. So, the number of full rounds that were completed is 47, and the sum of the hit points of
all remaining units is 200+131+59+200 = 590. From these, the outcome of the battle is 47 * 590 = 27730.

Here are a few example summarized combats:

#######       #######
#G..#E#       #...#E#   E(200)
#E#E.E#       #E#...#   E(197)
#G.##.#  -->  #.E##.#   E(185)
#...#E#       #E..#E#   E(200), E(200)
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 982 total hit points left
Outcome: 37 * 982 = 36334
#######       #######
#E..EG#       #.E.E.#   E(164), E(197)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##.#   E(98)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#
#######       #######

Combat ends after 46 full rounds
Elves win with 859 total hit points left
Outcome: 46 * 859 = 39514
#######       #######
#E.G#.#       #G.G#.#   G(200), G(98)
#.#G..#       #.#G..#   G(200)
#G.#.G#  -->  #..#..#
#G..#.#       #...#G#   G(95)
#...E.#       #...G.#   G(200)
#######       #######

Combat ends after 35 full rounds
Goblins win with 793 total hit points left
Outcome: 35 * 793 = 27755
#######       #######
#.E...#       #.....#
#.#..G#       #.#G..#   G(200)
#.###.#  -->  #.###.#
#E#G#G#       #.#.#.#
#...#G#       #G.G#G#   G(98), G(38), G(200)
#######       #######

Combat ends after 54 full rounds
Goblins win with 536 total hit points left
Outcome: 54 * 536 = 28944
#########       #########
#G......#       #.G.....#   G(137)
#.E.#...#       #G.G#...#   G(200), G(200)
#..##..G#       #.G##...#   G(200)
#...##..#  -->  #...##..#
#...#...#       #.G.#...#   G(200)
#.G...G.#       #.......#
#.....G.#       #.......#
#########       #########

Combat ends after 20 full rounds
Goblins win with 937 total hit points left
Outcome: 20 * 937 = 18740
What is the outcome of the combat described in your puzzle input?
"""

import collections
import sys
import time

import numpy

### CONSTANTS ###

NORTH	= 0
EAST	= 2
SOUTH	= 3
WEST	= 1

EMPTY		= 0
ELF		= 1
GOBLIN	= 2


### FUNCTIONS ###


### CLASSES ###

class Point( ):
	def __init__( self, x, y ):
		self.x = x
		self.y = y

	def get_tuple( self ):
		return ( self.x, self.y )

	def __eq__( self, other ):
		return self.x == other.x and self.y == other.y

	def __lt__( self, other ):
		return self.y < other.y or ( self.y == other.y and self.x < other.x )

	def __hash__( self ):
		return hash( ( self.x, self.y ) )

	def __repr__( self ):
		return '<Point ({0},{1})>'.format( self.x, self.y )


class Spot( Point ):
	def __init__( self, x, y ):
		Point.__init__( self, x, y )

		self.links = {
			NORTH:	None,
			EAST:		None,
			SOUTH:	None,
			WEST:		None,
		}

		self.contents = EMPTY

	def __repr__( self ):
		return '<Spot ({0},{1})>'.format( self.x, self.y )


class Unit( ):
	def __init__( self, type, spot ):
		self.type = type
		self.spot = spot
		self.hitpoints = 200
		self.attack_power = 3

	def is_alive( self ):
		return self.hitpoints > 0

	def __lt__( self, other ):
		if self.hitpoints < other.hitpoints:
			return True
		elif self.hitpoints > other.hitpoints:
			return False
		else:
			# Equal, so use position
			if self.spot < other.spot:
				return True

		return False

	def __repr__( self ):
		return '<Unit ({0})>'.format( 'Elf' if self.type == ELF else 'Goblin' )


class Manager( ):
	def __init__( self, filename ):
		self.map			= { }
		self.map_filename = filename

		self.elves		= [ ]
		self.goblins	= [ ]
		self.units		= [ ]

		self._parse_map( filename )


	def _parse_map( self, filename ):
		map = { }	# key is Point coords, value is Spot
		elves = [ ]
		goblins = [ ]
		units = [ ]

		y = 0

		for line in open( filename, 'r' ):
			x = 0

			for c in line.strip( ):
				if c == '#':
					x += 1
					continue
				elif c == '.':
					spot = Spot( x, y )
				elif c == 'E':
					spot = Spot( x, y )
					unit = Unit( ELF, spot )
					spot.contents = unit
					elves.append( unit )
					units.append( unit )
				elif c == 'G':
					spot = Spot( x, y )
					unit = Unit( GOBLIN, spot )
					spot.contents = unit
					goblins.append( unit )
					units.append( unit )

				map[ spot.get_tuple( ) ] = spot
				x += 1

			y += 1

		# populate links
		for pos, spot in map.items( ):
			x, y = pos

			if ( x, y-1 ) in map:
				spot.links[ NORTH ] = map[ ( x, y-1 ) ]
			if ( x+1, y ) in map:
				spot.links[ EAST ] = map[ ( x+1, y ) ]
			if ( x, y+1 ) in map:
				spot.links[ SOUTH ] = map[ ( x, y+1 ) ]
			if ( x-1, y ) in map:
				spot.links[ WEST ] = map[ ( x-1, y ) ]

		self.map = map
		self.elves = elves
		self.goblins = goblins
		self.units = units

		return


	def pathfind( self, start, goal ):
		"""
		http://ai-depot.com/Tutorial/PathFinding.html
		"""
		paths = [ ( start, ) ]

		while True:
			cur_path  = paths.pop( 0 )
			new_paths = [ ]

			# Get links for spot on end of list, but get them in
			# "reading order".
			links = [ ]
			for i in range( 4 ):
				#link = list( cur_path[ -1 ].links.values( ) )[ i ]
				link = cur_path[ -1 ].links[ i ]
				if link and ( link.contents == EMPTY or not link.contents.is_alive( ) ):
					links.append( link )

			#links = [ l for l in cur_path[ -1 ].links.values( ) if l and l.contents == EMPTY ]

			for link in links:
				new_paths.append( tuple( list( cur_path ) + [ link ] ) )

			# Remove any with loops
			new_paths = [ p for p in new_paths if len( set( p ) ) == len( p ) ]

			paths += new_paths

			# If we run out of paths, we've failed
			if not paths:
				return [ ]

			# Sort paths by distance from last node to goal node
			paths = sorted( paths, key = lambda p: self.get_distance( p[ -1 ], goal ) )

			# If a path has the goal at end, we've succeeded
			for path in paths:
				if path[ -1 ] == goal:
					return path


	def _get_links_recurse( self, spot, cluster ):
		new_links = [ s for s in spot.links if s not in cluster and s.contents == EMPTY ]
		cluster += new_links
		
		for link in new_links:
			cluster += self._get_links_recurse( link, cluster )
		
		return cluster
	

	def get_distance( self, point1, point2 ):
		return abs( point1.x - point2.x ) + abs( point1.y - point2.y )


	def move_unit( self, unit, spot ):
		old_spot = unit.spot
		unit.spot = spot
		old_spot.contents = EMPTY
		unit.spot.contents = unit
		#print( 'moving {0} -> {1}'.format( old_spot.get_tuple( ), spot.get_tuple( ) ) )


	def get_enemies( self, unit ):
		enemies = [ u for u in self.units if u != unit and u.type != unit.type and u.is_alive( ) ]
		enemies = sorted( enemies, key = lambda u: self.get_distance( unit.spot, u.spot ) )
		return enemies


	def get_goal_path( self, unit ):
		"""
		Given a unit, return nearest spot adjacent to enemies that is not occupied.
		"""
		spots = [ ]
		enemies = self.get_enemies( unit )

		valid_path = None

		e = 0
		paths = { }

		while e < len( enemies ):
			# Check spots around enemies, closest enemies first
			enemy = enemies[ e ]
			spots = [ s for s in enemy.spot.links.values( ) if s and s.contents == EMPTY ]

			for spot in spots:
				print( 'pathfinding {0} -> {1}'.format( unit.spot, spot ) )
				path = self.pathfind( unit.spot, spot )

				if path:
					if len( path ) not in paths:
						paths[ len( path ) ] = [ ]

					paths[ len( path ) ].append( path )

			# No valid path to this enemy, so move to next
			e += 1

			# Found at least one path to this enemy, so let's try
			# stopping here.
			if paths:
				break

		if paths:
			valid_path = sorted( paths[ sorted( paths.keys( ) )[ 0 ] ] )[ 0 ]

		return valid_path


	def get_units( self ):
		self.units = sorted( self.units, key = lambda u: u.spot )

		return self.units


	def match_over( self ):
		types = set( [ u.type for u in self.units if u.is_alive( ) ] )
		return len( types ) == 1


	def get_adjacent_enemies( self, unit ):
		enemies = [ s.contents for s in unit.spot.links.values( ) if s and s.contents and s.contents.is_alive( ) and s.contents.type != unit.type ]

		return enemies


	def get_unit_at_pos( self, pos ):
		for unit in self.units:
			if not unit.is_alive( ):
				continue

			if unit.spot.x == pos[ 0 ] and unit.spot.y == pos[ 1 ]:
				return unit

		return None


	def print_map( self ):
		y = 0
		print( '             1111111111222222222233' )
		print( '   01234567890123456789012345678901' )
		
		for line in open( self.map_filename, 'r' ):
			line = line.strip( ).replace( 'E', '.' ).replace( 'G', '.' )

			row = ''
			x = 0

			for x in range( len( line ) ):
				pos = ( x,y )
				unit = self.get_unit_at_pos( pos )

				if unit:
					if unit.type == ELF:
						row += 'E'
					else:
						row += 'G'
				else:
					row += line[ x ]

				x += 1

			num_str = '  ' + str( y )
			print( num_str[ -2: ] + ' ' +  row )
			#print( row )
			y += 1



### MAIN ###

if __name__ == "__main__":
	manager = Manager( 'input.txt' )
	rounds = 0

	while not manager.match_over( ):
		print( '\nAfter {0} rounds --------'.format( rounds ) )

		manager.print_map( )
		pending_moves = [ ]		# keys are units, values are spots to move to

		unit_count = 1

		for unit in manager.get_units( ):
			print( 'unit {0}/{1} - {2:.2f}%'.format( unit_count, len( manager.units ), unit_count / len( manager.units ) * 100 ) )

			if not unit.is_alive( ):
				continue

			adj_enemies = manager.get_adjacent_enemies( unit )

			if not adj_enemies:
				# Try to move
				# Get sorted list of goal spots, that are adjacent to enemies and unoccupied
				goal_path = manager.get_goal_path( unit )

				if goal_path:
					manager.move_unit( unit, goal_path[ 1 ] )
					# Move to first spot in path
					#pending_moves.append( ( unit, goal_path[ 1 ] ) )
					adj_enemies = manager.get_adjacent_enemies( unit )
				else:
					# Unit has no valid paths, so do nothing this turn
					unit_count += 1
					continue

			# Actually make moves
			#for move_unit, move_spot in pending_moves:
				#manager.move_unit( move_unit, move_spot )

			# If enemies are in range, attack one
			adj_enemies = manager.get_adjacent_enemies( unit )

			if adj_enemies:
				enemy = adj_enemies[ 0 ]
				enemy.hitpoints -= unit.attack_power

				if manager.match_over( ):
					break

			unit_count += 1
		# End unit loop

		if manager.match_over( ):
			break

		#print( 'elf = {0}'.format( manager.map[ (4,2) ].hitpoints ) )
		rounds += 1

	print( '\nAfter {0} rounds --------'.format( rounds + 1 ) )
	manager.print_map( )

	total_hps = sum( [ u.hitpoints for u in manager.get_units( ) if u.is_alive( ) ] )
	print( '\ntotal hitpoints = {0}'.format( total_hps ) )

	answer = total_hps * ( rounds + 1 )

	print( 'rounds = {0}'.format( rounds + 1 ) )

	print( 'answer = {0}'.format( answer ) )
	print( 'done' )