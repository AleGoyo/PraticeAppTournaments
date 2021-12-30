import random
from project import Player


class Tournament(Player):

    def __init__(self):
        self._table = {}
        self.kind_results = {'WIN': [], 'LOSSES': [], 'DRAW': []}


    @property
    def table(self):
        return self._table

    @table.setter
    def table(self,names):
        self._table.update({i: self.kind_results.copy() for i in names})

    @staticmethod
    def getting_results (self,name, result_of_players):
        if name in self._table:
            self._table[name][result_of_players] +=1
        else:
            print(f'O Jogador {name} não foi registrado')


    @staticmethod
    def merge(dic_1, dic_2):
        merged = dic_1 | dic_2
        return merged


class Swiss(Tournament):
    def __init__(self, table_players):
        super().__init__()

    def __getitem__(self, item):
        return self._table[item]

    @staticmethod
    def first_bye(self, quantidade_jogadores, lst_players):
        if quantidade_jogadores % 2 != 0:
            z = random.sample(lst_players, 1)
            return z

        
        



