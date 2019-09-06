class Inventory:
    """Класс инвентарь игрока."""
    def __init__(self, common, unique, spell, ally, money, fee, bless, skill, evidence, bank):
        self.common = common
        self.unique = unique
        self.spell = spell
        self.ally = ally  # союзник
        self.money = money  # деньги
        self.fee = fee  # гонорар
        self.bless = bless  # благословение/проклятье
        self.skill = skill  # навык
        self.evidence = evidence
        self.bank = bank  # ссуда
