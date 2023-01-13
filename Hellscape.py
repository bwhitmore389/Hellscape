import random
import time

class Hero:
    def __init__(self, name, race, xlass, xp = 0, level = 1, potions = 1):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.race = race
        self.xlass = xlass
        self.xp = xp
        self.potions = potions
        self.is_knocked_out = False

    def __repr__(self):
        # Printing a hero will tell you its name, its type, its level and how much health it has remaining
        return "{name}, Level {level} {race} {xlass} has {health} hit points remaining".format(level = self.level, name = self.name, health=self.health, race = self.race, xlass = self.xlass)

    def revive(self):
        # Reviving a hero will flip it's status to False
        self.is_knocked_out = False
        # A revived hero can't have 0 health. This is a safety precaution. revive() should only be called if the hero was given some health, but if it somehow has no health, its health gets set to 1.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def knock_out(self):
        # Knocking out a hero will flip its status to True.
        self.is_knocked_out = True
        # A knocked out hero can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the hero had health left, it gets set to 0.
        if self.health != 0:
            self.health = 0
        print("{name} was slaughtered!".format(name = self.name))

    def lose_health(self, amount):
        # Deducts heath from a hero and prints the current health reamining
        self.health -= amount
        if self.health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the hero.
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def use_potion(self):
        self.health += round(self.max_health * 0.5)
        self.potions -= 1
        # Makes sure the heath does not go over the max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} used a potion and now has {health} health.\n{potions} remaining in {name}'s inventory.".format(name = self.name, health = self.health, potions = self.potions))

    def melee_attack(self, enemy):
        # Checks to make sure the hero isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because they are knocked out!".format(name = self.name))
            return
        # If the hero attacking is proficient in the selected attack, then their attack will be fully effective. 
        if (self.xlass == "Warrior"):
            print("{name} attacked {other_name} for {damage} damage.".format(name = self.name, other_name = enemy.name, damage = round(self.level * 2)))
            print("It cuts deep!")
            enemy.lose_health(round(self.level * 2))
        # If the hero attacking doesn't have proficiency in the selected attack, then their attack will be less effective.
        if (self.xlass != "Warrior"):
            print("{name} attacked {other_name} for {damage} damage.".format(name = self.name, other_name = enemy.name, damage = round(self.level * .6)))
            print("'Tis but a flesh wound... Try using attacks that are more suitable!")
            enemy.lose_health(round(self.level * .6))
    
    def magic_attack(self, enemy):
        # Checks to make sure the hero isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because they are knocked out!".format(name = self.name))
            return
        # If the hero attacking is proficient in the selected attack, then their attack will be fully effective. 
        if (self.xlass == "Mage"):
            print("{name} casted a spell at {other_name} for {damage} damage.".format(name = self.name, other_name = enemy.name, damage = round(self.level * 2)))
            print("The spell is super effective!")
            enemy.lose_health(round(self.level * 2))
        # If the hero attacking doesn't have proficiency in the selected attack, then their attack will be less effective.
        if (self.xlass != "Mage"):
            print("{name} attacked {other_name} for {damage} damage.".format(name = self.name, other_name = enemy.name, damage = round(self.level * .6)))
            print("'Tis but a flesh wound... Try using attacks that are more suitable!")
            enemy.lose_health(round(self.level * .6))

    def ranged_attack(self, enemy):
        # Checks to make sure the hero isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because they are knocked out!".format(name = self.name))
            return
        # If the hero attacking is proficient in the selected attack, then their attack will be fully effective. 
        if (self.xlass == "Archer"):
            print("{name}'s arrow hits {other_name} for {damage} damage.".format(name = self.name, other_name = enemy.name, damage = round(self.level * 2)))
            print("Bullseye!")
            enemy.lose_health(round(self.level * 2))
        # If the hero attacking doesn't have proficiency in the selected attack, then their attack will be less effective.
        if (self.xlass != "Archer"):
            print("{name} attacked {other_name} for {damage} damage.".format(name = self.name, other_name = enemy.name, damage = round(self.level * .6)))
            print("'Tis but a flesh wound... Try using attacks that are more suitable!")
            enemy.lose_health(round(self.level * .6))

class Enemy(Hero):
    
    def __repr__(self):
        # Printing an enemy will tell you its name, its type, its level and how much health it has remaining
        return "{name}, Level {level} {race} {xlass} has {health} hit points remaining".format(level = self.level, name = self.name, health=self.health, race = self.race, xlass = self.xlass)

def first_turn():
    go = random.randint(1, 2)
    if go == 1:
        return "Enemy"
    else:
        return "Hero"

# Heros - AKA Objects of the Hero Class
a = Hero("Bug", "Orc", "Warrior")
b = Hero("Twig", "Undead", "Mage")
c = Hero("Cassie", "Human", "Archer")

#Enemies - AKA Objects of the Enemy Class
x = Enemy("The Hammer", "Human", "Warrior")
y = Enemy("Lord de Siete", "Skeleton", "Mage")
z = Enemy("Tailspin", "Orc", "Archer")

#####################################################################################
selected_hero = []
selected_enemy = []
turn = first_turn()

hero_selection = input("Welcome to Hellscape, O\'Fallon. Select your hero: \n [1] Bug, The Orc Warrior\n [2] Twig, The Undead Mage \n [3] Cassie the Human Archer")

print(hero_selection)

while hero_selection != "1" and hero_selection != "2" and hero_selection != "3": 
  hero_selection = input("A hero must be selected from the list, you pathetic worm! \n Select your hero: \n [1] Bug, The Orc Warrior\n [2] Twig, The Undead Mage \n [3] Cassie the Human Archer")

if hero_selection == "1":
    selected_hero.append(a)
    print("You have selected {name}, a level {level} {race} {xlass}. His axe is at your command!".format(name = a.name, level = a.level, race = a.race, xlass = a.xlass))
elif hero_selection == "2":
    selected_hero.append(b)
    print("You have selected {name}, a level {level} {race} {xlass}. His staff is set to kill!".format(name = b.name, level = b.level, race = b.race, xlass = b.xlass))
elif hero_selection == "3":
    selected_hero.append(c)
    print("You have selected {name}, a level {level} {race} {xlass}. She's nocked and loaded!".format(name = c.name, level = c.level, race = c.race, xlass = c.xlass))


print("On a scouting expedition one midsummer's afternoon, your hero makes a grisly discovery. You find the body of Joy, the local nurse, laying in the field just outside of town. Her entrails are now extrails. Your hero is keen enough to suspect foul play...")

initial_investigation = input("Does your hero decide to investigate? \n [Y/N]")

if initial_investigation == "Y":
  print("As you investicate the crime scene, you discover an alarmingly high concentration of Mythical Bone Powder in the area. This leads you to three possible conclusion...")

else:
  print("Better luck next time, adventurer! Clearly, you are yet a match for Hellscape, O'Fallon.")

enemy_selection = input("Your hero must now decide where to search for Nurse Joy's killer. \n Select your destination... \n [1] The Cemetary Gates \n [2] The Prison Chateau D'if \n [3] The Putrid Swamp")

while enemy_selection != "1" and enemy_selection != "2" and enemy_selection != "3": 
  enemy_selection = input("A location must be selected for investigation, you pathetic worm! \n Select your destination: \n [1] The Cemetary Gates \n [2] The Prison Chateau D'if \n [3] The Putrid Swamp")

if enemy_selection == "1":
    selected_enemy.append(x)
    print("{name} approaches The Cemetary Gates, and is ambushed by {other_name}, a level {level} {race} {xlass}. He's ready for a fight!".format(name = selected_hero[0].name, other_name = x.name, level = x.level, race = x.race, xlass = x.xlass))
elif enemy_selection == "2":
    selected_enemy.append(y)
    print("{name} approaches The Prison Chateau D'if, and is ambushed by {other_name}, a level {level} {race} {xlass}. The end of his staff glows with blue flame!".format(name = selected_hero[0].name, other_name = y.name, level = y.level, race = y.race, xlass = y.xlass))
elif enemy_selection == "3":
    selected_enemy.append(z)
    print("{name} approaches The Cemetary Gates, and is ambushed from above by {other_name}, a level {level} {race} {xlass}. He's ready for a fight!".format(name = selected_hero[0].name, other_name = z.name, level = z.level, race = z.race, xlass = z.xlass))

# Main Game Loop
while selected_hero[0].is_knocked_out == False and selected_enemy[0].is_knocked_out == False:
    if turn != "Enemy":
        action = int(input("{name}, please choose an action: \n1) Melee Attack\n2) Magic Attack \n3) Ranged Attack \n4) Use Potion\n".format(name = selected_hero[0].name)))
        while action != 1 and action != 2 and action != 3 and action !=4:
            action = int(input("Stop being such a wimp and attack the enemy! {name}, please choose an action: \n1) Melee Attack\n".format(name = selected_hero[0].name)))
        if action == 1:
            melee_attack = selected_hero[0].melee_attack(selected_enemy[0])
            turn = "Enemy"
        elif action == 2:
            magic_attack = selected_hero[0].magic_attack(selected_enemy[0])
            turn = "Enemy"
        elif action == 3:
            ranged_attack = selected_hero[0].ranged_attack(selected_enemy[0])
            turn = "Enemy"
        elif action == 4 and selected_hero[0].potions == 0:
            print("{name} is out of potions. Please select another option...".format(name = selected_hero[0].name))
            turn = "Hero"
        elif action == 4:
            use_potion = selected_hero[0].use_potion()
            turn = "Enemy"
    else:
        if selected_enemy[0].health <= 2 and selected_enemy[0].potions >= 1:
            selected_enemy[0].use_potion()
            turn = "Hero"
        elif selected_enemy[0].xlass == "Warrior":
            selected_enemy[0].melee_attack(selected_hero[0])
            turn = "Hero"
        elif selected_enemy[0].xlass == "Mage":
            selected_enemy[0].magic_attack(selected_hero[0])
            turn = "Hero"
        elif selected_enemy[0].xlass == "Archer":
            selected_enemy[0].ranged_attack(selected_hero[0])
            turn = "Hero"


            
            


