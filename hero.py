import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:

    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        """Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

        # counter to track deaths and kills respectively
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""

        if (not self.abilities) and (not opponent.abilities):
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                heroAttack = self.attack()
                opponentAttack = opponent.attack()

                self.take_damage(opponentAttack)
                opponent.take_damage(heroAttack)

                if self.is_alive():
                    self.add_kill(1)
                    opponent.add_death(1)
                    print(f"{self.name} won!")
                else:
                    opponent.add_kill(1)
                    self.add_death(1)
                    print(f"{opponent.name} won!")

        random_winner = random.choice([self, opponent])
        print(f"{random_winner.name} won!")

    def add_ability(self, ability):
        """ Add ability to abilities list """
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """ Add weapon to self.abilities"""
        self.abilities.append(weapon)

    def attack(self):
        """Calculate the total damage from all ability ability attacks.
        return: total_damage : Integer
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += str(ability.attack())

        return total_damage

    def add_armor(self, armor):
        """Add armor to self.armors
        Armor: Armor Object
        """
        self.armors.append(armor)

    def defend(self):
        """Calculate the total block amount from all armor blocks.
        return: total_block : Integer
        """
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense."""
        damageTaken = self.defend()
        damage -= damageTaken
        self.current_health -= damage

    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not"""
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        """ Update self.kills counter by num_kills amount"""
        self.kills += num_kills

    def add_death(self, num_deaths):
        """ Update self.kills counter by num_deaths amount"""
        self.deaths += num_deaths


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
