# libs:

from project import Player
from project import tournaments





# function the check the first bye


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    registered_players = []
    table_champ = []
    menu = 1
    while menu != 0:
        print('Menu')
        print('0:Fechar Aplicação')
        print('1: Registar/Alterar/Deletar Jogador')
        print('2: Começar campeonato')
        print('3:Exportar Campeonato')
        menu = int(input('Escolha uma das opções:'))
        if menu == 0:
            menu = 0

        # registering/altering/deleting players
        elif menu == 1:
            checking = 1
            while checking != 0:
                print('0:Fechar a Registro de Jogadores')
                print('1:Registrar Jogadores:')
                print('2:Alterar Jogadores:')
                print('3:Deletar Jogadores')
                print('4:Visualizar Jogadores')
                menu_choice = int(input('Faça Sua escolha:'))
                # closing the loop/done
                if menu_choice == 0:
                    checking = int(input('Deseja terminar o registro de jogadores?\n 0:sim \n 1:Não'))

                # registering the players/done
                elif menu_choice == 1:
                    name = str(input('Nome do Jogador:'))
                    last_name = str(input('Sobrenome do Jogador:'))
                    registered_players.append(Player.Player(name, last_name))

                # altering players/done
                elif menu_choice == 2:
                    name_altered = str(input('Digite o Nome do usuario a ser alterado:')).upper()
                    last_name_altered = str(input('Digite o Sobrenome do usuario a ser alterado')).upper()
                    to_be_altered = name_altered + last_name_altered
                    for loop in registered_players:
                        if to_be_altered == str(loop.name + loop.last_name).upper():
                            new_name = str(input("Digite o Nome:"))
                            new_last_name = str(input("Digite o Sobrenome:"))
                            loop.name(new_name)
                            loop.last_name(new_last_name)

                # deleting player
                elif menu_choice == 3:
                    name_remove = str(input('Digite o Nome do Jogador a Ser removido:')).upper()
                    last_name_remove = str(input('Digite o Sobrenome do Jogador a Ser removido:')).upper()
                    to_be_removed = name_remove + last_name_remove
                    i = 0
                    for loop in registered_players:
                        if to_be_removed == str(loop.name + loop.last_name).upper():
                            print(f'Você tem certeza que deseja deletar {loop.name} {loop.last_name}? ')
                            sure = int(input('1: Sim\n2: Não'))
                            if sure == 1:
                                registered_players.pop(i)
                            else:
                                i += 1
                        print('Não Há jogadores com esse nome registrado')
                # printing the players/done
                elif menu_choice == 4:
                    for obj in registered_players:
                        print(obj)

        # starting championship
        elif menu == 2:
            if len(registered_players) == 0:  # checking if there is no players registered
                print('Não há Jogadores registrados!')
                continue
            else:
                number_rounds = number_of_rounds_swiss(len(registered_players))
                print(f'Serão {number_rounds} rodadas')
                sheet_game = {}
                if len(registered_players) % 2 != 0:
                    tournaments.Swiss.first_bye(len(registered_players), registered_players)

                else:
                    pass

        # exporting the championship sheet
        elif menu == 3:
            pass
            print('In developpment')
