class Map:
    """Класс карты"""
    def __init__(self, locations):
        self.locations = locations  # Локации карты
        self.fear_track = 0  # Трек ужаса
        self.sky = []  # Небо
        self.suburb = []  # Окраины
