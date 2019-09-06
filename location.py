class Location:
    """Класс локации"""
    def __init__(self, color, street, move_color, name, cards):
        self.color = color  # Цвет локации
        self.street = street  # Обозначение Улица или нет (можно сделать подклассом)
        self.move_color = move_color  # Цвет для перемещения монстров Белый черный (можно сделать тру фолс)
        self.name = name  # Название
        self.opened = True  # Открыта ли локация или нет
        self.evidence = 0  # Количество улик на локации
        self.portal = False  # Есть ли открытые врата
        self.cards = cards  # Пул карт для локации (пока не понятно есть ли смысл создавать его здесь или сделать колоду)
