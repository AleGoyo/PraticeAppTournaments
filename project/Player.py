class Player:

    def __init__(self, name, last_name):
        self._name = name.upper()
        self._last_name = last_name.upper()

    def __str__(self):
        return f'{self._name} {self._last_name}'.upper()

    @staticmethod
    def set_altering_names(self, name, last_name):
        self._name = name
        self._last_name = last_name

    @property
    def name(self):
        return self._name

    def name_setter(self, new_name):
        self._name = new_name.upper()

    @property
    def last_name(self):
        return self._last_name

    def last_name_setter(self, new_last_name):
        self._last_name = new_last_name.upper()
