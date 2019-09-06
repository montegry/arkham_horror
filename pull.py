from monster import Monster
MONSTERS = [{"Name": "Halo", "Description": "Scarry monster!!", "Health": 2, "Skill": None,
             "Resist": "Magic resistance", "Health_resist": -2, "Mind_resist": -1, "Mind_damage": 0,
             "Health_damage": -1, "Color": "Green", "Type": "Moon", "Vigilance": +2}]


class Pull:
    """Класс пулла для монстров"""
    def __init__(self):
        self.pull = []
        self.create()

    def create(self):
        for i in range(len[MONSTERS]):
            self.pull.append(Monster(definition=MONSTERS[i]["Description"], health_damage=MONSTERS[i]["Health_damage"],
                                     health=MONSTERS[i]["Health"], skill=MONSTERS[i]["Skill"],
                                     resist=MONSTERS[i]["Resist"], power_resist=MONSTERS[i]["Health_resist"],
                                     mind_resist=MONSTERS[i]["Mind_resist"], mind_damage=MONSTERS[i]["Mind_damage"],
                                     vigilance=MONSTERS[i]["Vigilance"], color=MONSTERS[i]["Color"],
                                     m_type=MONSTERS[i]["Type"]))

    def pull_out(self):
        if len(self.pull) >= 0:
            pass
        else:
            pass

    def pull_in(self, monster):
        self.pull.append(monster)
