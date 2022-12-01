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
"""

### IMPORTS ###


### CONSTANTS ###


### FUNCTIONS ###

def find_base(bag):
	#print(bag)
	#print(rules[bag])
	if (rules[bag] == [['base']]):
		return False
	if ['shiny gold'] in rules[bag]:
		return True
	else:
		for key in rules[bag]:
			if find_base(key[0]) == True:
				return True



def print_rule_tree( bags, color, indent_level = 0 ):
	print( '{0}{1}'.format( ' ' * 2 * indent_level, color ) )

	for in_color in bags[ color ]:
		if in_color[ 0 ] == 'base':
			continue
		print_rule_tree( bags, in_color[ 0 ], indent_level + 1 )


### MAIN ###

if __name__ == "__main__":
	#7-1.py
	with open("input.txt","r") as file:
		data = file.readlines()
		rules = {}
		for line in data:
			line = line.split(' ')
			print(line)
			if line[-3] == "no":
				rules[line[0] + " " + line[1]] = [["base"]]
			elif len(line)>8:
				rules[line[0] + " " + line[1]] = [[line[5]+" " + line[6]], [line[9]+" " + line[10]]]
			else:
				rules[line[0] + " " + line[1]] = [[line[5]+" " + line[6]]]
		#print(rules)
		
	print_rule_tree( rules, 'bright black' )

	total = 0
	bags_with_gold = [ ]
	for line in rules:
		if find_base(line):
			#print("Exited function")
			total+=1
			bags_with_gold.append( line )
	print(total)
	bags_with_gold = list( set( bags_with_gold ) )
	bags_with_gold.sort( )
	for b in bags_with_gold:
		print( b )