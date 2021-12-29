class Player:

    def __init__(self, name, last_name):
        self._name = name.upper()
        self._last_name = last_name.upper()
        self.results = {'Win': [], 'Losses': [], 'Draw': []}

    def __str__(self):
        return f'{self._name} {self._last_name}'.upper()

    @staticmethod
    def set_altering_names(self, name, last_name):
        self._name = name
        self._last_name = last_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.upper()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name.upper()

    @property
    def results(self):
        return self._results

    def set_victory(self):
        self.results['Win'].append(True)

    def set_defeat(self):
        self.results['Losses'].append(True)

    def set_draw(self):
        self.results['Draw'].append(True)

    def get_results(self):
        return self.results
