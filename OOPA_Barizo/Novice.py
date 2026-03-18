#This is the Novice class

from Character import Character

class Novice():
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage}")
#Problem here was my own typos within the code
#Specifically with indentation and confusing a comma with a period    