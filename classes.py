import random

#--------------------------------------------------------------------------------------Item Classes
class ItemSuper:
    def effect(self):
        return {
        'attribute': self.effect_what,
        'value': self.effect_value,
        }
class Items:
    """
    Items class allows the ItemGetter to work properly
    Each item gets a rarity which defines the drop chances
    The randint function selects from 0 to drop chances
    So the range should be between 1 - 1000
    """
    class Potion(ItemSuper):
        """
        Potions, yo
        """
        def __init__(self):
            self.value = 50
            self.description = """
            Potions are used when you find yourself in dire straits.\n
            They return your vitality, and heal wounds that are superficial.\n
            Heals 5 health.
            """
            #change rarity after test
            self.rarity = 1
            self.effect_what = "health"
            self.effect_value = 5
            self.item_string = "Potion"
            self.success = """
            The potion resotres 5 health to the target!
            """
    class PhilterOfStrength(ItemSuper):
        """
        test class
        """
        def __init__(self):
            #change rarity after test
            self.rarity = 15
            self.effect_what = "strength"
            self.effect_value = 5
            self.item_string = "PhilterOfStrength"
            self.success = """
            The Philter gives the target 5 extra strength points!
            """
            #change rarity after test
    class Hi_Potion(ItemSuper):
        def __init__(self):
            self.rarity = 5
            self.effect_what = "health"
            self.effect_value = 15
            self.item_string = "Hi_Potion"
            self.success = """
            Hi Potion restores 15 health points to the target!
            """

class ItemGetter:
    def __init__(self):
        pass
    def make_item(self, item_name):
        target_class = getattr(Items, item_name)
        instance = target_class()
        return instance

#------------------------------------------------------------------------------------Character Classes
class Character:
    def __init__(self, level, health, health_max, strength, dexterity, stamina):
        self.name = ""
        self.level = level
        self.health = health
        self.health_max = health_max
        self.strength = strength
        self.dexterity = dexterity
        self.stamina  = stamina
        self.item_drop_classes = []
        self.items_dropped = []
        self.can_flee = True
    def do_damage(self, enemy):
        first = round((random.gauss(self.level, 0.75) - random.gauss(enemy.level, 0.75) + (self.strength/3))-((enemy.dexterity/2)-(self.dexterity/2)))
        second = max(first, 0)
        damage = min(second, enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print "%s evades %s's attack." % (enemy.name, self.name)
        else:
            print "%s causes %d damage to %s!" % (self.name, damage, enemy.name)
        return enemy.health <= 0

    def use_item(self, item):
        """
        item arg is a class instance of the item
        """
        try:
            effects_dict = item.effect()
            attr_val = getattr(self, effects_dict['attribute'])
            val = effects_dict['value']
            if self.bag_of_holding.contents[item.item_string].quantity > 0:
                self.bag_of_holding.contents[item.item_string].quantity -= 1
            else:
                print "You have no more %s!" % item.item_string
            if effects_dict['attribute'] == "health":
                if (self.health_max - self.health) < item.effect_value:
                    val = self.health_max - self.health
            setattr(self, effects_dict['attribute'], (getattr(self, effects_dict['attribute']) + val))
            print item.success

        except AttributeError:
            print "Be sure to specify the correct item!"

    def item_drop(self):
        getter = ItemGetter()
        for drop in self.drops:
            self.item_drop_classes.append(getter.make_item(drop))
        for items in self.item_drop_classes:
            if random.randint(0, items.rarity) == 1:
                self.items_dropped.append(items.item_string)
        return self.items_dropped

    def encounter(self):
        pass

class Goblin(Character):
    def __init__(self, player, name):
        Character.__init__(self, 1, 10, 10, 6, 5, 1)
        self.name = name
        self.gives_exp = 150
        self.gives_skill_points = 1
        self.can_probe = True
        self.drops = ["Potion"]

class Bear(Character):
    def __init__(self, player, name):
        Character.__init__(self, 3, 15, 15, 12, 2, 1)
        self.name = "Bear"
        self.gives_exp = 170
        self.gives_skill_points = 2
        self.can_probe = True
        self.drops = ["Potion", "Hi_Potion"]

class Demon(Character):
    def __init__(self, player, name):
        Character.__init__(self, 10, 30, 30, 20, 15, 1)
        self.name = name
        self.gives_exp = 1500
        self.gives_skill_points = 3
        self.can_probe = False
        self.drops = ["PhilterOfStrength", "Hi_Potion"]

class Dragon(Character):
    def __init__(self, player, name):
        Character.__init__(self, 30, 55, 55, 40, 30, 1)
        self.name = name
        self.gives_exp = 30000
        self.gives_skill_points = 40
        self.can_probe = False
        self.can_flee = False

class Player(Character):
    def __init__(self):
        Character.__init__(self, 1, 10, 10, 10, 7, 10)
        self.state = 'normal'
        self.has_levelled = False
        self.position = [0,1]
        self.skill_points = 0
        self.exp = 0
        self.exp_to_next = 50
        self.bag_of_holding = Container()
        self.bestiary = {}
        self.bag_of_holding.add_item("Potion")
        self.bag_of_holding.add_item("PhilterOfStrength")

    def quit(self):
        print "%s can't find the way back home, and dies of starvation.\nR.I.P." % self.name
        self.health = 0

    def help(self):
        import commands_dicts
        if self.state == 'normal':
            for c in commands_dicts.Commands:
                print c
        elif self.state == 'fight':
            for c in commands_dicts.Battle_Commands:
                print c

    def status(self):
        print "%s's level: %d" % (self.name, self.level)
        print "%s's exp is %d and %d is needed to level up"%(self.name, self.exp, self.exp_to_next)
        print "%s's has %d skill points remaining"%(self.name, self.skill_points)
        print "%s's health: %d/%d" % (self.name, self.health, self.health_max)
        print "%s's strength: %d" % (self.name, self.strength)
        print "%s's dexterity: %d" % (self.name, self.dexterity)

    def tired(self):
        print "%s feels tired." % self.name
        self.health = max(1, self.health - 1)

    def rest(self):
        if self.state != 'normal':
            print "%s can't rest now!" % self.name; self.enemy_attacks()
        else:
            print "%s rests." % self.name
            #deprecated
            #if random.randint(0, 1) > 4:
                #self.enemy = Enemy(self)
                #print "%s is rudely awakened by %s!" % (self.name, self.enemy.name)
                #self.state = 'fight'
                #self.enemy_attacks()

            if self.health < self.health_max:
                self.health = self.health + 1
            else: print "%s slept too much." % self.name; self.health = self.health - 1

    def explore(self):
        import bestiary_dicts
        direction = raw_input("Forward (f)/Backward(b)\n>")
        direction.lower()
        if self.state != 'normal':
            print "%s is too busy right now!" % self.name
            self.enemy_attacks()
        else:
            if direction == "f" and self.position[1] >= 0:
                print "%s explores deeper into the passage." % self.name
                self.position = [0, self.position[1]+1]
            elif direction == "b":
                if self.position[1] <= 0:
                    print "%s, you are about to leave the cave.\n Are you certain of your decision?\n" % self.name
                    choice = raw_input("Yes(Y)/No(N)\n>")
                    if choice.lower() == "y":
                        self.quit()
                    else:
                        print "You return to the darkness that promises glory."
                        self.position = [0, self.position[1] + 1]
                else:
                    print "%s returns in the direction of obscurity and the mundane." % self.name
                    self.position = [0, self.position[1] - 1]
            else:
                print "That was not an accepted direction, please try again."
                self.explore()
        if random.randint(0, 1):
            #I think that I'm going to kill the enemy -> character inheritance and use an enemy superclass
            #this whole "switch" could be a dictionary of methods within the superclass
            if self.position[1] <=10 :
                self.enemy = Goblin(self, "Goblin")
            elif self.position[1] > 10 and self.position[1] <=20:
                if random.randint(1, 2) == 1:
                    self.enemy = Bear(self, "Bear")
                else:
                    self.enemy = Goblin(self, "Goblin")
            elif self.position[1] == 20:
                print """Your senses tingle, the way has become more dangerous.\n
                Be wary of the way ahead, for it may be more than you're ready to handle.
                """
            elif self.position[1] > 20:
                if random.randint(1, 3) == 1:
                    self.enemy = Demon(self, "Demon")
                elif random.randint(1, 3) == 2:
                    self.enemy = Bear(self, "Bear")
                else:
                    self.enemy = Goblin(self, "Goblin")
            elif self.position[1] == 40:
                print """You can sense a strong being.\n
                To continue further would surely mean that you must meet it in battle.
                Tread lightly, %s, for the danger ahead is not one that you are liable to survive...
                """%self.name
            elif self.position[1] > 40:
                self.enemy = Dragon(self, "Dragon of Ages")
            print "%s encounters a %s!" % (self.name, self.enemy.name)
            if self.enemy.name not in self.bestiary:
                print bestiary_dicts.Bestiary_Desc[self.enemy.name]
                self.bestiary[self.enemy.name] = bestiary_dicts.Bestiary_Desc[self.enemy.name]
            else:
                print "View your bestiary for a description of this foe."
            self.state = 'fight'
        else:
            if random.randint(0, self.stamina): self.tired()

    def flee(self):
        if self.state != 'fight': print "%s runs in circles for a while." % self.name; self.tired()
        elif self.enemy.can_flee:
            if random.randint(1, self.health + 5) > random.randint(1, self.enemy.health):
                print "%s flees from %s." % (self.name, self.enemy.name)
                self.enemy = None
                self.state = 'normal'
            else: print "%s couldn't escape from %s!" % (self.name, self.enemy.name); self.enemy_attacks()
        else:
            print """Attempting to escape this enemy would surely lead to your demise!\n
            You stay and fight for your life.
            """

    def attack(self):
        if self.state != 'fight':
            print "%s swats the air, without notable results." % self.name; self.tired()
        else:
            if self.do_damage(self.enemy):
                print "-----------%s executes %s!----------------" % (self.name, self.enemy.name)
                item_array = self.enemy.item_drop()
                self.exp += self.enemy.gives_exp
                if (self.exp_to_next - self.exp) < self.enemy.gives_exp:
                    self.skill_points += self.enemy.gives_skill_points
                for items in item_array:
                    print "%s receives %s" % (self.name, items)
                    self.bag_of_holding.add_item(items)
                self.enemy = None
                self.state = 'normal'
            else: self.enemy_attacks()
            if self.exp >= self.exp_to_next:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.level += 1
                self.exp_to_next += self.level**2*100
                print "%s feels stronger!" % self.name
                if not self.has_levelled:
                    print "Be sure to check your status!"
                    self.has_levelled = True

    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print "%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name)
    def locate(self):
        print "%s has travelled %d meters into the cave..." % (self.name, self.position[1])

    def probe(self):
        if self.state == 'normal':
            print "There doesn't seem to be anything to probe..."
        elif self.enemy.can_probe:
            print "%s has:\nHealth: %d out of %d\nStrength: %d\nDexterity: %d"%(self.enemy.name,self.enemy.health, self.enemy.health_max,self.enemy.strength, self.enemy.dexterity)
        else:
            print "It seems this enemy can resist your perception!"

#need to look at all methods involving the inventory
    def view_items(self):
        if self.bag_of_holding.contents == {}:
            print "You have no items in your inventory!"
        else:
            for key in self.bag_of_holding.contents:
                print key, self.bag_of_holding.contents[key].quantity

    def use(self, item):
        self.use_item(item)

    def specify(self):
        item_to_use = raw_input("Which item?\n>")
        self.use(self.bag_of_holding.contents.get(item_to_use))

    def view_bestiary(self):
        for key in self.bestiary.keys():
            print key
        choice = raw_input("Which entry would you like to read?\n> ")
        try:
            print self.bestiary[choice]
        except KeyError:
            print "That doesn't seem to be a valid entry in your bestiary..."

    def assign_skill_points(self):
        if self.skill_points == 0:
            print "You have no remaining skill points!"
        else:
            choice = raw_input("Would you like to improve your strength (s), or dexterity(d)?\n> ")
            if choice == "s":
                self.strength += 1
                self.skill_points -= 1
            elif choice == "d":
                self.dexterity += 1
                self.skill_points -= 1
            else:
                print "You have not assigned your skill points."
                return

#---------------------------------------------------------------------------------extra classes

class Container:
    """
    This is a holder class for various types of containers, such as the player's bag of holding.
    It can also be used for chests and the like.
    """
    def __init__(self):
        self.contents = {}
        self.getter = ItemGetter()

    def init_item(self, item):
        self.contents[item] = self.getter.make_item(item)
        self.contents[item].quantity = 1

    def add_item(self, item):
        if item in self.contents:
            self.contents[item].quantity += 1
        else:
            self.init_item(item)

class Map:
    def __init__(self, player, width, height, type_of):
        self.width_height = [width, height]
        self.type = type_of
        #maybe I don't need a full map, but a description
        #consider easier options for this.

class Magic:
    def fire(self):
        pass
    def ice():
        pass
    def water():
        pass
    def thunder():
        pass
