class Acient:
    """класс древнего"""
    def __init__(self, definition, track, resist, skill):
        self.definition = definition  # имя айди описание
        self.track = track  # трек древнего
        self.resist = resist  # сопротивление.
        self.skill = skill  # здесь надо писать как он будет биться в случае просыпания и как влияет на игру.

    def is_sleeping(self):
        """Проверка на сон"""
        if self.track[0] >= self.track[2]:
            return True
        else:
            return False

