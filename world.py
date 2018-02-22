import items
import barriers

class MapTile:
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = []):
		self.x = x
		self.y = y
		self.contents = {'barriers': barriers, 'items': items, 'enemies': enemies}	# A dict containing all the contents of the room.
	
	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
	def intro_text(self):
		return """You find yourself in a cave with a flickering torch on the wall.
		You can make out a path to the east and to the west, each equally as dark and foreboding.
		"""

class Corridor(MapTile):
	def intro_text(self):
		return """You find yourself in a poorly lit corridor."""
		
class StoreRoom(MapTile):
	def intro_text(self):
		return """You seem to have entered an underground storeroom!"""
		
class Expanse(MapTile):
	def intro_text(self):
		return """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see."""

class Nook(MapTile):
	def intro_text(self):
		return """A dank nook of the cave lies before you. The only way out is back the way you came."""
		
		
class NearVictory(MapTile):
	def intro_text(self):
		return """You can see a light to the east at the end of this corridor. Could that be your way out?"""


class VictoryTile(MapTile):
	def intro_text(self):
		return """You see a bright light in the distance...
		It grows as you get closer! It's sunlight!	
		Victory is yours!
		"""
		
class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[Corridor(),												NearVictory(),												VictoryTile(),															Corridor(), 																		Corridor()],
		[Expanse(),													Expanse(),		 											Nook(), 																Corridor(barriers = [barriers.Wall('e')]),		 									Corridor(barriers = [barriers.Wall('w')])],
		[Expanse(),													Expanse(),	 												Corridor(barriers = [barriers.Wall('n'), barriers.Wall('s')]), 															Corridor(barriers = [barriers.Wall('e'), barriers.Wall('s')]),		 				Corridor(barriers = [barriers.Wall('w')])],
		[None,														Corridor(barriers = [barriers.Wall('n')]),					StartTile(barriers = [barriers.Wall('s'), barriers.Wall('n')]), 		Corridor(barriers = [barriers.Wall('n')]), 											Corridor()],
		[None,														Corridor(barriers = [barriers.WoodenDoor('e')]),			StoreRoom(barriers = [barriers.Wall('n')]),								None,																				None]
	]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		for barrier in self.map[y][x].contents['barriers']:
			if(barrier.direction == 'north' and not barrier.passable):
				return [False, barrier.description()]				
				
		if y-1 < 0:
			room = None
		try:
			room = self.map[y-1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]
			
	def check_south(self, x, y):
		for barrier in self.map[y][x].contents['barriers']:
			if(barrier.direction == 'south' and not barrier.passable):
				return [False, barrier.description()]	
				
		if y+1 < 0:
			room = None
		try:
			room = self.map[y+1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for barrier in self.map[y][x].contents['barriers']:
			if(barrier.direction == 'west' and not barrier.passable):
				return [False, barrier.description()]	
	
		if x-1 < 0:
			room = None
		try:
			room = self.map[y][x-1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]
			
	def check_east(self, x, y):
		for barrier in self.map[y][x].contents['barriers']:
			if(barrier.direction == 'east' and not barrier.passable):
				return [False, barrier.description()]	
				
		if x+1 < 0:
			room = None
		try:
			room = self.map[y][x+1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]