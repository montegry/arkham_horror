class Gamer:
    """Класс Игрок."""
    def __init__(self, id0, start_health, start_mind, start_inventory, concentration, skill, speed, secrecy, power,
                 volition, knowledge, luck, definition, position):
        self.health = start_health  # Здоровье
        self.mind = start_mind  # Разум
        self.inventory = start_inventory  # Инвентарь
        self.concentration = concentration  # Собранность (перемешение ползунков)
        self.unique_skill = skill  # Особое умение пока не знаю как применять
        self.speed = speed  # Скорость
        self.secrecy = secrecy  # Скрытность
        self.power = power  # Сила
        self.volition = volition  # Воля
        self.knowledge = knowledge  # Знания
        self.luck = luck  # Удача
        self.definition = definition  # Описание героя
        self.position = position  # Местоположение
        self.haul = []  # трофеи, можно включить в инвентарь
        self.id = id0  # возможно порядок хода
