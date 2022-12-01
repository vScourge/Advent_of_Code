"""
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your 
re-routed trip coming up is on a high-speed train. However, the train ticket you were given is 
in a language you don't understand. You should probably figure out what it says before you get 
to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, 
and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other 
nearby tickets for the same train service (via the airport security cameras) together into a 
single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and 
the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means 
that one of the fields in every ticket is named class and can be any value in the ranges 1-3 
or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the 
numbers on the ticket in the order they appear; every ticket has the same format. For example, 
consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 
101,102,103,104,301,302,303,401,402,403; 
of course, the actual train tickets you're looking at are much more complicated. In any case, 
you've extracted just the numbers in such a way that the first number is always the same specific 
field, the second number is always a different specific field, and so on - you just don't know 
what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values 
which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12

It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets 
by considering only whether tickets contain values that are not valid for any field. In this example, 
the values on the first nearby ticket are all valid for at least one field. This is not true of the 
other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together 
all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?


--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the 
remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order 
is consistent between all tickets: if seat is the third field, it is the third field on every ticket, 
including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9

Based on the nearby tickets in the above example, the first position must be row, the second position 
must be class, and the third position must be seat; you can conclude that in your ticket, 
class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the 
word departure. What do you get if you multiply those six values together?
"""

### IMPORTS ###

import collections
import cProfile
import itertools
import numpy
import pstats
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'


### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )
	
	fields = [ ]
	my_ticket = [ ]
	tickets = [ ]
	i = 0
	
	while lines[ i ] != '':
		line = lines[ i ]
		parts1 = line.split( ':' )
		
		field = Field( parts1[ 0 ] )
		
		parts2 = parts1[ 1 ].strip( ).split( ' ' )
		
		min_max = [ int( x ) for x in parts2[ -3 ].split( '-' ) ]
		range1 = list( range( min_max[ 0 ], min_max[ 1 ] + 1 ) )

		min_max = [ int( x ) for x in parts2[ -1 ].split( '-' ) ]
		range2 = list( range( min_max[ 0 ], min_max[ 1 ] + 1 ) )
		
		field.ranges = [ range1, range2 ]
		field.valid = field.valid.union( set( range1 + range2 ) )
		fields.append( field )
		
		i += 1
		
	i += 2
	
	my_ticket = [ int( x ) for x in lines[ i ].split( ',' ) ]
	ticket = Ticket( my_ticket )
	tickets.append( ticket )	
	i += 3
	
	while i < len( lines ):
		values = [ int( x ) for x in lines[ i ].split( ',' ) ]
		ticket = Ticket( values )
		tickets.append( ticket )
		i += 1
			
	return( fields, my_ticket, tickets )
			
	

def main( fields, my_ticket, tickets ):
	
	# Make a set including all valid field values
	valid_values = set( )
	
	for field in fields:
		for range1 in field.ranges:
			valid_values = valid_values.union( set( range1 ) )
		
	# Discard tickets with any invalid values
	valid_tickets = [ ]
	
	for ticket in tickets:
		if not set( ticket.values ).difference( valid_values ):
			valid_tickets.append( ticket )
		
	# Make dict of all fields listed on all tickets.
	# Key is position, value is a set of all values listed at that pos
	f_data = { }
	
	for ticket in valid_tickets:
		for pos in range( len( ticket.values ) ):
			if pos not in f_data:
				f_data[ pos ] = set( )
				
			f_data[ pos ].add( list( ticket.values )[ pos ] )
			
	# Now iterate over field positions, and find which fields
	# have all-valid values across all tickets for that position.
	# End result is a dict where key is position, value is a list of
	# /possible/ field objects.
	valid_fields_by_pos = { }
	
	for field in fields:
		for pos in range( len( ticket.values ) ):
			pos_vals = f_data[ pos ]
			
			if not pos_vals.difference( field.valid ):
				# For this field position, all values on the tickets are within
				# the valid range for this field, so it must be the one.
				if pos not in valid_fields_by_pos:
					valid_fields_by_pos[ pos ] = [ ]

				valid_fields_by_pos[ pos ].append( field )
		
	# Now narrow down each position to the one possible field it must be. To do that...
	# Iterate over our valid_fields_by_pos dict, looking for positions that only have 1 possible field.
	# When found, remove that field from every other position's list.
	# Repeat until every pos has only one field left.

	# Keep going if any pos has > 1 field left
	while any( [ len( p ) > 1 for p in valid_fields_by_pos.values( ) ] ):
		# Iterate over all positions
		for pos in range( len( valid_fields_by_pos ) ):
			if len( valid_fields_by_pos[ pos ] ) == 1:
				this_field = valid_fields_by_pos[ pos ][ 0 ]
				
				# Remove this field from other position's lists
				for pos2 in range( len( valid_fields_by_pos ) ):
					if pos2 == pos:
						# Ignore the one pos we're currently looking at
						continue
					
					# If this pos contains our target field, remove it
					if this_field in valid_fields_by_pos[ pos2 ]:
						valid_fields_by_pos[ pos2 ].remove( this_field )
	
	# Now find each field starting with "departure" and add those values off my
	# ticket together.
	total = 1
	
	for pos, fields in valid_fields_by_pos.items( ):
		field = fields[ 0 ]		# only 1 in each list now
		
		if field.name.startswith( 'departure' ):
			total *= my_ticket[ pos ]
			
	print( 'answer =', total )
	

### CLASSES ###

class Field( ):
	def __init__( self, name ):
		self.name = name
		self.ranges = [ ]
		self.valid = set( )
		
	def __repr__( self ):
		return '<Field "{0}">'.format( self.name )
	

class Ticket( ):
	def __init__( self, values ):
		self.values = values
		
	def __repr__( self ):
		return '<Ticket "{0}">'.format( ','.join( [ str( x ) for x in self.values ] ) )
		

### MAIN ###

if __name__ == "__main__":
	time_start = time.perf_counter( )

	fields, my_ticket, tickets = parse_input( )

	#profiler = cProfile.Profile( )
	#profiler.enable( )

	main( fields, my_ticket, tickets )

	#profiler.disable( )
	#stats = pstats.Stats( profiler )
	#stats.dump_stats( r'C:\Users\Home\Dropbox (Personal)\misc\profile.pstats' )
	
	#print( 'answer =',  )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 756 too low
