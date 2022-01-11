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
        if name1 and name2 in self.table:
            return True
        elif name1 not in self.table:
            return f'O Jogador {name1} não foi registrado'
        elif name2 not in self.table:
            return f'O Jogador {name2} não foi registrado'
        else:
            return f'Nenhum Jogador foi encontrado'

    # @staticmethod
    def setting_won_losses(self, v_player, l_player):
        if self.checking_players(v_player, l_player) is True:
            self.__setitem__(v_player, l_player, 'WIN')
            self.__setitem__(l_player, v_player, 'LOSSES')

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
            return int(len(self.__getitem__(name, 'win')) * 3 + len(self.__getitem__(name, 'DRAW')))

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
        return self.create_table(self.names)

    def first_pairing(self):
        pair = []
        name_list = [i for i in self.table]
        while name_list:
            pairing = random.sample(name_list, 2)
            pair.append(pairing)
            name_list.remove(pairing[0])
            name_list.remove(pairing[1])
        return pair

    def pairing(self):
        pairing = {}
        r_list = []
        pairing.update({i: [self.table[i]['POINTS'].copy(), self.table[i]['TIE BREAK'].copy()] for i in self.table})
        s_list = sorted(pairing, key=pairing.get, reverse=True)
        while s_list:  # while to create a list of the pairings
            a = s_list.pop(0)
            b = s_list.pop(0)
            c = (a, b)
            r_list.append(c)
        return r_list

    def first_bye(self):
        if len(self.table) % 2 != 0:
            z = random.sample(list(self.table), 1)
            print(f'O Jogador{z[0]} esta de BYE')
            Tournament.__setitem__(self, z[0], 'BYE', 'WIN')
            return z[0]
        else:
            return False

    def byes(self, names):
        # added the tiebreak
        bye_1 = {names: [self.table[names]['TIE BREAK'].copy(), self.table[names]['TIE BREAK'].copy()] for names in
                 names}
        # may use a sort still thinking about it
        bye_return = min(bye_1, key=bye_1.get)
        self.__setitem__(bye_return, 'BYE', 'WIN')
        return bye_return

    @staticmethod
    def number_of_rounds_swiss(self):
        for x in range(Tournament.__len__(self._table)):
            if pow(2, x) >= Tournament.__len__(self._table):
                return int(x)
