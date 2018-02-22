from formattext import *				# Import some important functions for formatting text.


from player import Player
from world import World
import parse

debug_mode = True	# Use this to toggle verbose mode on the text parser.

game_name = "Escape from Cave Terror, v3"

help_text = "To interact with this game world, you will use a basic text-based interface. \
Try single-word commands like 'inventory' or 'west' (or their counterpart abbreviations, 'i' or 'w', respectively \
to get started. For more complex interactions, use commands of the format [VERB][NOUN] (e.g. 'open door', \
or in some cases, [VERB][NOUN][OBJECT] (e.g. 'attack thief with nasty knife').\
The game will ignore the articles 'a', 'an', and 'the' (e.g. 'open the door' is the same as 'open door.').\n\n\
To exit the game at any time, type 'exit' or 'quit'."

player = Player()
world = World()
	
def play():	
	clear_screen()
	print("--------------------------------------------------------")
	print_wrap("Welcome to %s!" % game_name)
	print("--------------------------------------------------------")
	print()
	
	turn_count = 0		# Tracking turn count may be used for some games.
	
	print_wrap(world.tile_at(player.x,player.y).intro_text())
	
	while True:
		print()							# Print a blank line for spacing purposes.
		[raw_input, parsed_input] = parse.get_command()
		print()							# Print a blank line for spacing purposes.
		
		
		if(debug_mode):	
			print("--------------------------------------------------------")
			print("RAW USER COMANDS: " + raw_input)
			print("PARSED USER COMMANDS: " + str(parsed_input))
			print("--------------------------------------------------------")
			print()
			

		if(len(parsed_input) == 3):
			[verb, noun1, noun2] = parsed_input
			[turn_taken, result_text] = handle_input(verb, noun1, noun2)
			if(turn_taken):
				turn_count += 1
			if(result_text):
				if(isinstance(result_text, list)):	# Find out if there is more than one sentence returned.
					for text in result_text:
						print_wrap(text)
				else:
					print_wrap(result_text)
		else:
			print("Something seems to have gone wrong. Please try again.")
			
		
def handle_input(verb, noun1, noun2):
	if(verb == 'help'):
		if(not noun1):
			return [False, help_text]
		else:
			return [False, "I'm not sure what you need help with. Try using 'help' on its own."]

			
	elif(verb == 'exit'):
		if(not noun1):
			exit()
		else:
			return[False, "Are you trying to quit the game? If so, just type 'exit' on its own."]
	
	
	elif(verb == 'go'):
		if(not noun2):
			if(noun1 == 'north'):
				[move_status, move_description] = world.check_north(player.x, player.y)
				if(move_status):
					player.move_north()
					return [True, [move_description, world.tile_at(player.x, player.y).intro_text()]]
				else:
					return [False, move_description]
					
			elif(noun1 == 'south'):
				[move_status, move_description] = world.check_south(player.x, player.y)
				if(move_status):
					player.move_south()
					return [True, [move_description, world.tile_at(player.x, player.y).intro_text()]]
				else:
					return [False, move_description]
					
			elif(noun1 == 'east'):
				[move_status, move_description] = world.check_east(player.x, player.y)
				if(move_status):
					player.move_east()
					return [True, [move_description, world.tile_at(player.x, player.y).intro_text()]]
				else:
					return [False, move_description]
					
			elif(noun1 == 'west'):
				[move_status, move_description] = world.check_west(player.x, player.y)
				if(move_status):
					player.move_west()
					return [True, [move_description, world.tile_at(player.x, player.y).intro_text()]]
				else:
					return [False, move_description]		
					
			else:
				return [False, "I'm not sure where you're trying to go."]
				
		else:
			return [False, "Whatever you are trying to do is too complicated for me to understand. Please try again."]
			
			
	elif(verb == 'check'):
		if(not noun2):
			if(noun1 == 'none' or noun1 == 'around' or noun1 == 'room' or noun1 == 'surroundings'):
				return [False, world.tile_at(player.x, player.y).intro_text()]
			elif(noun1 == 'inventory' or 'pockets'):
				player.print_inventory();
				return [False, '']	# No need to return any text because the player.print_inventory() function already did.
			else:
				return [False, "I'm not sure what you are trying to look at."]
		else:
			return [False, "I think you are trying to look at something, but your phrasing is too complicated. Please try again."]
			
	elif(verb):
		return [False, "I'm not sure how to %s that." % verb]
	else:
		return [False, "I have no idea what you are trying to do. Please try again."]
 

### Play the game.
play()