import random
from project import Player
import copy  # importing to create a deepcopy of kind_results to be able to alter the mutable separately


class Tournament(Player):

    def __init__(self):
        super().__init__()
        self._table = {}
        self.kind_results = {'WIN': [], 'LOSSES': [], 'DRAW': [], 'POINTS': [], 'TIE BREAK': []}

    def __len__(self):
        return len(self._table)

    def __setitem__(self, name, opponent, result):
        self._table[name][result].append(opponent)

    def __getitem__(self, name, item):
        return self._table[name][item]

    @property
    def table(self):
        return self._table

    def create_table(self, names):  # function to create the table for the tournament
        # dict with a deepcopy
        self._table.update({i: copy.deepcopy(self.kind_results) for i in names})

    def checking_players(self, name1, name2):
        if name1 and name2 in self._table:
            return True
        elif name1 not in Tournament.table:
            return f'O Jogador {name1} não foi registrado'
        elif name2 not in Tournament.table:
            return f'O Jogador {name2} não foi registrado'
        else:
            return f'Nenhum Jogador foi encontrado'

    @staticmethod
    def setting_won_losses(self, v_player, l_player):
        if Tournament.checking_players(self, v_player, l_player) is True:
            Tournament.__setitem__(self, v_player, l_player, 'WIN')
            Tournament.__setitem__(self, l_player, v_player, 'LOSSES')

        else:
            print(Tournament.checking_players(self, v_player, l_player))

    def setting_draw(self, player1, player2):
        if Tournament.checking_players(self, player1, player2) is True:
            Tournament.__setitem__(self, player1, player2, 'DRAW')
            Tournament.__setitem__(self, player2, player1, 'DRAW')
        else:
            print(Tournament.check(self, player1, player2))

    def getting_points(self, name):
        if name in self.table:
            return int(len(self.table[name]['WIN']) * 3 + len(self.table[name]['DRAW']))

    @staticmethod
    def merge(dic_1, dic_2):
        merged = dic_1 | dic_2
        return merged


class Swiss(Tournament):
    def __init__(self, names):
        super().__init__()
        self.names = names

    def __getitem__(self, name, item):
        return self._table[name][item]

    def tie_breaking_sb(self, name):
        sv = []  # sum of the victory of the other players
        d = []  # sum of the draw of the other players
        for i in self.table:
            if i is not name and i in self.table[name]['WIN'] or i in self.table[name]['DRAW']:
                sv.append(len(self.table[i]['WIN']))
                d.append(len(self.table[i]['DRAW']))
        sb = ((sum(sv) * 3) + (sum(d) * 1))  # calculating the tie break of Sonnenborn-Berger
        self.table[name]['TIE BREAK'].append(sb)

    def starting(self):
        return Tournament.create_table(self, self.names)

    def first_pairing(self):
        pass

    def pairing(self):
        pass

    def first_bye(self):
        if len(self.table) % 2 != 0:
            z = random.sample(list(self.table), 1)
            print(f'O Jogador{z[0]} esta de BYE')
            Tournament.__setitem__(self, z[0], 'BYE', 'WIN')
            return z[0]
        else:
            return False

    def byes(self, names):
        bye_1 = {names: Tournament.getting_points(self, names) for names in names}
        bye_return = min(bye_1, key=bye_1.get)
        Tournament.__setitem__(self, bye_return, 'BYE', 'WIN')
        return bye_return

    @staticmethod  # function to get the number of rounds
    def number_of_rounds_swiss(self):
        for x in range(Tournament.__len__(self._table)):
            if pow(2, x) >= Tournament.__len__(self._table):
                return int(x)
