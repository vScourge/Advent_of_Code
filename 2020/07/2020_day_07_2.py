"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks 
like you'll even have time to grab some food: all flights are currently delayed 
due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being 
enforced about bags and their contents; bags must be color-coded and must contain 
specific quantities of other color-coded bags. Apparently, nobody responsible for 
these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every 
faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 
6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, 
how many different bag colors would be valid for the outermost bag? (In other 
words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least 
one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list 
of rules is quite long; make sure you get all of it.)

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because 
of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 
2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this 
example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

### IMPORTS ###


### CONSTANTS ###


### FUNCTIONS ###

def parse_rules( lines ):
	"""
	vibrant cyan bags contain 4 drab beige bags, 4 vibrant maroon bags, 2 dull coral bags.
	"""
	bags = { }
	
	for line in lines:
		end = line.find( ' bags' )
		key = line[ :end ]
		
		bag = Bag( key )
		bags[ key ] = bag
		
		if line.endswith( 'no other bags.' ):
			continue
		
		end = line.find( ' contain ' ) + 9
		temp = line[ end: ]
		
		for part in temp.split( ', ' ):
			words = part.split( ' ' )
			qty = int( words[ 0 ] )
			color = ' '.join( words[ 1:-1 ] )
			
			bag.contains[ color ] = qty
			
	return bags
		
	
def can_contain_recurse( bags, color_start, color_target ):
	bag = bags[ color_start ]
	
	for color_contained in bag.contains:
		if color_contained == color_target or can_contain_recurse( bags, color_contained, color_target ):
			return True

	return False


def count_contained_bags_recurse( bags, color_start ):
	"""
	shiny gold bags contain 1 clear coral bag, 1 muted green bag, 5 muted teal bags, 4 dull olive bags.
	
	1 shiny gold
		1 clear coral
			1 striped olive
				4 posh maroon
					5 striped beige
						2 bright lavender
							3 mirrored gold
								1 vibrant blue
		1 muted green
			
		5 muted teal
		4 dull olive
		
	"""
	bag = bags[ color_start ]
	
	print( '---')
	print( 'Bag: {0}'.format( color_start ) )

	total = 0
	
	for color_contained, count in bag.contains.items( ):
		print( '  {0} {1}'.format( count, color_contained ) )
		total += count
		count2 = count_contained_bags_recurse( bags, color_contained )
		total += count * count2
		
	print( '  total = {0}'.format( total ) )
		
	return total
	
	
	
### CLASSES ###

class Bag( ):
	def __init__( self, color ):
		self.color = color
		self.contains = { }		# key is bag color, value is # it can contain
		
		
	def __repr__( self ):
		return '<Bag "{0}">'.format( self.color )

### MAIN ###

if __name__ == "__main__":
	lines = open( 'input.txt', 'r' ).read( ).splitlines( )

	bags = parse_rules( lines )
	
	count = count_contained_bags_recurse( bags, 'shiny gold' )
	
	print( count )
		   
	# shiny gold bags contain 1 clear coral bag, 1 muted green bag, 5 muted teal bags, 4 dull olive bags.
	# 34375168109855377315644045 too high
	# 11 wrong
	# answer = 58175