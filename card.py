class Card:
    """Класс карт родительский для всех карт."""
    def __init__(self, description):
        self.description = description


class MythCard(Card):
    pass


class ArkhamWorldCard(Card):
    def __init__(self, color, c_type):
        self.color = color
        self.c_type = c_type


class OutWorldCard(Card):
    pass


class CommonThing(Card):
    def __init__(self, magic_physical, damage):
        pass


class UniqueThing(Card):
    pass


class Spell(Card):
    pass


class Ally(Card):
    pass


class Skill(Card):
    pass


class Bless(Card):
    pass


class Fee(Card):
    pass


class Bank(Card):
    pass


