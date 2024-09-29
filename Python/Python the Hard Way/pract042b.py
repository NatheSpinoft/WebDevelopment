# Class wARFARE!!

class Spells():
    Spell_list = {
        "Fireball": 10,
        "Iceball": 7,
        "Lightning": 11,
        "Earthbend": 6
    }
class Player():
    def __init__(self):
        self.health = 40 + (((randint(3,9) * 10) + 100) * .1)
        self.equipped_spell = None
    
    def equip(self, equipped_spell):
        if equipped_spell in Spells.Spell_list:
            self.equipped_spell = equipped_spell
            print("You equipped the %s spell") % equipped_spell
        else:
            print("Invalid Choice")
        