#The game mechanics
from random import randint

class Weapon():
    Weapons = {
        "sword": 6,
        "scimitar": 7,
        "bow_and_arrow": 4,
        "spear": 7,
        "staff": 10
    }

class Player():
    def __init__(self):
        self.health = int(40 * ((randint(1,9) + 100) * .1))
        self.equipped_weapon = None

    def equip(self, weapon_name):
        if weapon_name in Weapon.Weapons:
            self.equipped_weapon = weapon_name
            print("You equipped the %s") % weapon_name
        else:
            print("Invalid weapon") 

    def attack(self, enemy):
        if self.equipped_weapon:
            damage = Weapon.Weapons[self.equipped_weapon]
            enemy.health -= damage
            print("You attack the enemy with %s for %d damage.") % (self.equipped_weapon, damage)
        else:
            print("You need to equip a weapon first!")

class Enemy():
    def __init__(self):
        self.health = int(15 * ((randint(1,5) + 100) * .1 ))

    def attack(self, player):
        damage = randint(1, 5)  # Example damage for the enemy
        player.health -= damage
        print("The enemy attacks you for %d damage.") % damage

class GameMap():
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        print("Here we are beach whataga")
        print("You see an enemy and some weapons")
        print("sword, scimitar, bow and arrow, spear and staff")
        self.game_loop()    
        
    def game_loop(self):
        while self.player.health > 0 and self.enemy.health > 0:
            weapon_choice = raw_input("Choose a weapon to equip (or type 'attack' to attack): ")
            if weapon_choice in Weapon.Weapons:
                self.player.equip(weapon_choice)
            elif weapon_choice.lower() == 'attack':
                self.player.attack(self.enemy)
                if self.enemy.health > 0:  # Enemy attacks only if it's still alive
                    self.enemy.attack(self.player)
            else:
                print("Invalid input. Please choose a weapon or type 'attack'.")

        if self.player.health <= 0:
            print("You have been defeated!")
        elif self.enemy.health <= 0:
            print("You defeated the enemy!")

# Start the game
game = GameMap()