"""
[1518-07-23 23:59] Guard #2179 begins shift
[1518-10-03 00:42] falls asleep
[1518-11-17 00:32] wakes up
"""

import datetime
import pickle
import time

ARRIVE = 'Arrive'
ASLEEP = 'Asleep'
AWAKE = 'Awake'


class Day( ):
	def __init__( self, dtime ):
		self.datetime = dtime
		self.day = dtime.day
		
		self.events = [ ]
		
	def is_guard_asleep( id, minute ):
		pass
	

class Guard( ):
	def __init__( self, id ):
		self.id = id
		
		self.mins_asleep = { }		# key is day, data is list of hours asleep
		self.total_mins_asleep = 0	# total across all days
		self.events = [ ]

	def __repr__( self ):
		return '<Guard id:{0}>'.format( self.id )
		

class Event( ):
	"""
	[1518-07-23 23:59] Guard #2179 begins shift
	"""
	def __init__( self, line ):
		line = line.strip( ).replace( '1518', '2018' )
		
		self.line = line
		self.datetime = datetime.datetime.strptime( line[ 1:17 ], '%Y-%m-%d %H:%M' )
		self.timestamp = time.mktime( self.datetime.timetuple( ) )
		self.guard_id = None
		
		if 'begins' in line:
			self.action = ARRIVE
			self.guard_id = line.split( '#' )[ 1 ].split( ' ' )[ 0 ]
		elif 'asleep' in line:
			self.action = ASLEEP
		else:
			self.action = AWAKE
			
	def __repr__( self ):
		"""
		[1518-07-23 23:59] Guard #2179 begins shift
		"""
		return '<Event #{0} {1} {2}>'.format( self.guard_id, self.line[ 6:17 ], self.action )


data = { }	# key = timestamp
count = 0

events = [ ]

for line in open( 'input.txt', 'r' ):
	event = Event( line )
	events.append( event )
	
events.sort( key = lambda r: r.timestamp ) 

# Update IDs on records that are after arrive for each guard
for event in events:
	if event.action == ARRIVE:
		temp_id = event.guard_id
	else:
		event.guard_id = temp_id

pickle.dump( events, open( 'events.pickle', 'wb' ) )

guards = { }

for event in events:
	if event.guard_id in guards:
		continue
	
	else:
		new_guard = Guard( event.guard_id )
		state = AWAKE
		
		guard_events = [ e for e in events if e.guard_id == new_guard.id ]
		new_guard.events = events
		
		mins_asleep = { }
		
		start_minute = None
		
		for g_event in guard_events:
			print( g_event )
			day = g_event.datetime.day
			
			if g_event.datetime.day not in mins_asleep:
				mins_asleep[ day ] = [ ]
			
			if g_event.action == ARRIVE:
				start_minute = None
	
			elif g_event.action == ASLEEP:
				start_minute = g_event.datetime.minute
				
			elif g_event.action == AWAKE:
				for m in range( start_minute, g_event.datetime.minute ):
					mins_asleep[ day ].append( m )
	
				start_minute = None
				
		# Out of events, so next guard has arrived
		new_guard.mins_asleep = mins_asleep
		start_minute = None
		
		# Figure total mins asleep across all days
		total = 0
		for mins in new_guard.mins_asleep.values( ):
			total += len( mins )
		new_guard.total_mins_asleep = total
	
		print( 'done' )
	
		guards[ new_guard.id ] = new_guard


# Find guard with most mins asleep
mins = 0
s_guard = None

for guard in guards.values( ):
	if guard.total_mins_asleep > mins:
		mins = guard.total_mins_asleep
		s_guard = guard
		
# Now figure which minute guard was asleep most often
guard = s_guard
print( 'Guard {0} most mins asleep {1}'.format( guard.id, guard.total_mins_asleep ) )

mins_total = { }

max_min = None
max_amt = 0

for day, mins in guard.mins_asleep.items( ):
	for minute in mins:
		if minute not in mins_total:
			mins_total[ minute ] = 0
			
		mins_total[ minute ] += 1
		
		if mins_total[ minute ] > max_amt:
			max_min = minute
			max_amt = mins_total[ minute ]

print( 'minute = {0} ({1} times)'.format( minute, max_amt ) )
print( 'answer = {0}'.format( int( guard.id ) * max_min ) )
print( 'done' )