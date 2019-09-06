class Monster:
    """Клас Монстра."""
    def __init__(self, definition, health, skill, resist, power_resist, mind_resist, health_damage, mind_damage,
                 vigilance, color, m_type):
        self.health = health  # количество удач для победы + цена трофея
        self.skill = skill  # Особое умение типа "Нежить" "Неисчислимость" и т.д.
        self.resist = resist  # Сопротивление урону: Магическое , Физическое
        self.power_resist = power_resist  # Минус по силе удара
        self.mind_resist = mind_resist  # Минус по силе воли
        self.health_damage = health_damage  # Урон по здоровью
        self.mind_damage = mind_damage  # Урон по воле
        self.vigilance = vigilance  # бдительность, для проверок по уходу от монстра
        self.color = color  # Передвижения зависят отцвета
        self.type = m_type  # Тип мира откуда прибыл Тругольник Месяц и т.д.
        self.position = None  # Локация где расположен
        self.definition = definition  # Описание здесь нужен список с именем, id, и описанием
