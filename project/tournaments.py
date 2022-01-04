import random
from project import Player

import copy  # importing to create a deepcopy of kind_results to be able to alter the mutable separately


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
        # dict with a deepcopy
        self._table.update({i: copy.deepcopy(self.kind_results) for i in names})

    def checking_players(self, name1, name2):
        if name1 in self._table:
            if name2 in self._table:
                return True
        elif name1 not in self._table:
            return f'O Jogador {name1} não foi registrado'
        elif name2 not in self._table:
            return f'O Jogador {name2} não foi registrado'
        else:
            return f'Nenhum Jogador foi encontrado'

    @staticmethod
    def setting_won_losses(self, v_player, l_player):
        if Tournament.checking_players(self, v_player, l_player) is True:
            self._table[v_player]['WIN'].append(l_player)
            self._table[l_player]['LOSSES'].append(v_player)
        else:
            print(Tournament.checking_players(self, v_player, l_player))

    def setting_draw(self, player1, player2):
        if Tournament.checking_players(self, player1, player2) is True:
            self._table[player1]['Draw'].append(player2)
            self._table[player2]['Draw'].append(player1)
        else:
            print(Tournament.check(self, player1, player2))

    def getting_points(self, name):
        if name in self._table:
            return int(len(self._table[name]['WIN'])*3 + len(self._table[name]['DRAW']))

    @staticmethod
    def merge(dic_1, dic_2):
        merged = dic_1 | dic_2
        return merged


class Swiss(Tournament):
    def __init__(self):
        super().__init__()

    def __getitem__(self, item):
        return self._table[item]

    def byes(self, names):
        bye_1 = {names: Tournament.getting_points(self, names) for names in names}
        bye_return = min(bye_1, key=bye_1.get)
        self._table[bye_return]['WING'].append('BYE')
        return bye_return

    @staticmethod
    def first_bye(self):
        if len(self._table) % 2 != 0:
            z = random.sample(list(self._table), 1)
            print(f'O Jogador{z[0]} está de BYE')
            self._table[z[0]]['WIN'].append('BYE')
            return z[0]
