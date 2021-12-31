import random
from project import Player


class Tournament(Player):

    def __init__(self):
        self._table = {}
        self.kind_results = {'WIN': [], 'LOSSES': [], 'DRAW': []}

    def __len__(self):
        return len(self._table)

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, names):
        self._table.update({i: self.kind_results.copy() for i in names})

    @staticmethod
    def setting_results(self, v_player, l_player, result_of_players):
        if v_player & l_player in self._table:
            self._table[v_player]['WIN'] += {l_player: result_of_players}
            self._table[l_player]['LOSSES'] += {v_player: result_of_players.reverse()}
        elif v_player not in self._table:
            print(f'O Jogador {v_player} não foi registrado!')
        elif l_player not in self._table:
            print(f'O Jogador {l_player} não foi registrado!')
        else:
            print(f'Nenhum Jogador encontrado!')

    def getting_victory(self, name):
        if name in self._table:
            return self._table[name]['WIN']

    @staticmethod
    def merge(dic_1, dic_2):
        merged = dic_1 | dic_2
        return merged


class Swiss(Tournament):
    def __init__(self):
        super().__init__()

    def __getitem__(self, item):
        return self._table[item]

    @staticmethod
    def first_bye(self):
        if len(self._table) % 2 != 0:
            z = random.sample(self._table.key, 1)
            return z
