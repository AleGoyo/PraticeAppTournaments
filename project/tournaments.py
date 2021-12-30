import random
# from project import Player


class Tournament:

    def __init__(self):
        self._table = {}

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, name):
        self._table = {name: [{'Victory': [], 'Losses':[], 'Draws': []}]}

    @staticmethod
    def merge(dic_1, dic_2):
        merged = dic_1 | dic_2
        return merged


class Swiss(Tournament):
    def __init__(self, table_players):
        super().__init__()
        self.table_players = table_players

    def __getitem__(self, item):
        return self.table_players[item]

    @staticmethod
    def bye(self, quantidade_jogadores, lst_players):
        if quantidade_jogadores % 2 != 0:
            z = random.sample(lst_players, 1)
            return z

        
        
        


