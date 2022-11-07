# player class
class Player:
    def __init__(self, name, health, attack, defense, speed, level, exp):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.exp = exp

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_speed(self, speed):
        self.speed = speed

    def set_level(self, level):
        self.level = level

    def set_exp(self, exp):
        self.exp = exp

    def __str__(self):
        return "Name: " + self.name + "\nHealth: " + str(self.health) + "\nAttack: " + str(self.attack) + "\nDefense: " + str(self.defense) + "\nSpeed: " + str(self.speed) + "\nLevel: " + str(self.level) + "\nEXP: " + str(self.exp)
