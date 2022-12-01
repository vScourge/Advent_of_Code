"""
--- Day 21: Allergen Assessment ---
You reach the train's last stop and the closest you can get to your vacation island without getting wet. 
There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' 
worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens 
are listed in a language you do understand. You should be able to use this information to determine which 
ingredient contains which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that 
food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens 
aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the 
ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. 

However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: 
maybe they forgot to label it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)

The first food in the list has four ingredients (written in a language you don't understand): 
mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food 
definitely contains are listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in 
your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. 

Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all 
appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do 
any of those ingredients appear?
"""

### IMPORTS ###

import math
import numpy
import time


### CONSTANTS ###

INPUT_FILENAME = 'input.txt'

rules = { }


### FUNCTIONS ###

def parse_input( ):
	lines = open( INPUT_FILENAME, 'r' ).read( ).splitlines( )

	data_f = { }
	data_i = { }
	data_a = { }
	i = 0
	
	for line in lines:
		i += 1
		
		parts1 = line.split( '(' )
		ingredients = set( parts1[ 0 ].strip( ).split( ' ' ) )
		allergens = set( parts1[ 1 ][ 9: ].rstrip( ')' ).split( ', ' ) )

		food = Food( i, ingredients, allergens )
		
		data_f[ food.id ] = food
		    
		# Add these ingredients to dict of allergens
		for allergen in allergens:
			if allergen not in data_a:
				data_a[ allergen ] = Allergen( allergen )

			data_a[ allergen ].ingredients = data_a[ allergen ].ingredients.union( ingredients )
			
		# Add these allergens to dict of ingredients
		for ingredient in ingredients:
			if ingredient not in data_i:
				data_i[ ingredient ] = Ingredient( ingredient )
				
			data_i[ ingredient ].allergens = data_i[ ingredient ].allergens.union( allergens )
	
	return data_f, data_i, data_a


def update_lists( final_i, data_i, data_a ):
	# Go through allergens and remove ingredients that are no longer possible
	for a_name, allergen in data_a.items( ):
		if len( allergen.ingredients ) == 1:
			continue
		
		not_ingredients = [ i for i in final_i if final_i[ i ] != a_name ]
		allergen.ingredients = allergen.ingredients.difference( not_ingredients )
		
		if len( allergen.ingredients ) == 1 and list( allergen.ingredients )[ 0 ] not in final_i:
			final_i[ list( allergen.ingredients )[ 0 ] ] = a_name
			
		
	for i_name, ingredient in data_i.items( ):
		not_allergens = [ a for a in final_i.values( ) if a != a_name ]
		ingredient.allergens = allergen.ingredients.difference( not_allergens )
	
	return final_i, data_i, data_a



def main( data ):
	"""
	"""
		
	return answer
	

### CLASSES ###

class Food( ):
	def __init__( self, id, ingredients, allergens ):
		self.id = id
		self.ingredients = ingredients
		self.allergens = allergens
		
	def __repr__( self ):
		return '<Food {0}>'.format( self.id )
	

class Ingredient( ):
	def __init__( self, ingredient ):
		self.id = ingredient
		self.foods = set( )
		self.allergens = set( )
		
	def __repr__( self ):
		return '<Ingredient "{0}">'.format( self.id )
	

class Allergen( ):
	def __init__( self, allergen ):
		self.id = allergen
		self.foods = set( )
		self.ingredients = set( )
		
	def __repr__( self ):
		return '<Allergen "{0}">'.format( self.id )
	


### MAIN ###

if __name__ == "__main__":
	"""
	mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
	trh fvjkl sbzzf mxmxvkd (contains dairy)
	sqjhc fvjkl (contains soy)
	sqjhc mxmxvkd sbzzf (contains fish)
	
	The first step is to determine which ingredients can't possibly contain any of the allergens in any food in 
	your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. 
	Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all 
	appear once each except sbzzf, which appears twice.
	"""
	time_start = time.perf_counter( )

	data_f, data_i, data_a = parse_input( )
	
	# 1. Go through each allergen, looking for foods that list it, but do not
	# contain ingredients associated with that allergen. Remove those from 
	# the list of possibiliites.
	final_i = { }	# key is ingredient name, value is allergen name
	
	
	while len( final_i ) != len( data_a ):
		print( '{0} of {1}'.format( len( final_i ), len( data_a ) ) )
		                            
		foods = [ f for f in data_f.values( ) ]
		
		for food in foods:
			a_name = list( food.allergens )[ 0 ]
			ingredients = set( food.ingredients )
			
			for food2 in data_f.values( ):
				if food == food2:
					continue
				
				if a_name in food2.allergens:
					# Skip allergens we've already identified
					if a_name in final_i.values( ):
						continue
					
					# Same allergen is listed in these 2 foods.
					# See which ingredients are listed in both
					ingredients = ingredients.intersection( food2.ingredients )
					# Now remove any we've already connected to an allergen
					ingredients = ingredients.difference( set( [ i for i in final_i ] ) )
					
					if len( ingredients ) == 1 and list( ingredients )[ 0 ] not in final_i:
						# Found a final ingredient-allergen connection!
						i_name = list( ingredients )[ 0 ]
						final_i[ i_name ] = a_name
	
						# Update the allergen list in this ingredient object
						data_i[ i_name ].allergens = set( [ a_name ] )
					
						# Update the ingredients list in this allergen object
						data_a[ a_name ].ingredients = set( [ i_name ] )
						
						final_i, data_i, data_a = update_lists( final_i, data_i, data_a )
						#print( 'blah' )

				#final_i, data_i, data_a = update_lists( final_i, data_i, data_a )
				
					
	# Make list of ingredients that don't contain any allergens
	safe_ingredients = [ i for i in data_i if i not in final_i ]
	#print( safe_ingredients )
	
	# count how many times those ingredients appear
	total = 0
	
	for food_id, food in data_f.items( ):
		for ingredient in safe_ingredients:
			if ingredient in food.ingredients:
				total += 1
			
	answer = total
	
	print( 'answer =', answer )
	print( 'done in {0:.4f} secs'.format( time.perf_counter( ) - time_start ) )

# 2786
