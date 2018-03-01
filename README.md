Week 8 Changes:

Added consume_description to Crusty_Bread and Red_Potion classes.
Added is_equipped variable to Weapon class.

Added max_hp variable to Player class.
Added weapon variable to Player class (to store currently equipped weapon).
Added methods heal(), take_damage(), and is_alive() to Player class.
Added options for 'self', 'health', or 'hp' to verb 'check' in Player handle_input() method.
Added options for consuming consumable items to Player handle_input() method.
Fixed print_inventory() method in Player class so that it does not fail when there is nothing in the inventory.
Added 'equip' option to Player handle_input() method.
Added 'unequip' option to Player handle_input() method.
Updated Player.print_inventory() method to include equipped weapon.
Added loop to update_inventory() method to allow player to drop an equippped weapon.

Added options for 'health', or 'hp' with implied verb 'check' in parse.py.

Added print_loss_text() function to game.py. Added check of player.is_alive() in main game loop.


Added enemy descriptions to MapTile.intro_text().
Added description, attack_description, and loot to Enemy class.
Added agro variable to Enemy class. This will be used to cause certain enemies to attack spontaneously.
Added direction and loot to Enemy __init__() method.
Added description() method to class Enemy.
Added take_damage() method to class Enemy.

Fixed a problem in Weapon.attack() that caused attack description index to go out of bounds.

Added some logic to MapTile.intro_text() to allow enemies to block paths as well as barriers. If an enemy is blocking a direction, it supercedes a barrier description.
Added check for enemies to World.check_north() and other directions.

Added update_rooms() method to World class to allow enemies to be removed after they are defeated and to allow enemies with agro = True to attack.

Added update() method to MapTile class. This is called by World.update_rooms().
Added random_spawn() method to MapTile class. This can be updated for rooms in which you want random encounters with enemies. An example of this using a colony of bats is used in the demo.

Added npcs.py.
Added NPC-related verbs to parse.py.
Added value to item objects so that they can be sold by NPCs.
Updated game.py to include 'buy' verb actions.

Fixed a bug in World.add_implied_barriers that caused walls to be erected if an enemy was blocking a path.