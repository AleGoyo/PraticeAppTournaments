# libs:
from project.tournaments import Swiss
from project import Player


def apply_results_players_swiss(players):
    cp_players = []
    while players:
        if len(cp_players) == len(players) and len(cp_players) != 0:
            print('Não há mais jogadores para receberem os resultados!')
            break
        else:
            print('Os jogadores que ainda não receberam os resultados:')
            for a in range(len(players)):
                if players[a] not in cp_players:
                    print(f'{players[a][0]}\t e \t{players[a][1]}')
            try:
                mesa = int(input('Escolha qual mesa será passado o resultado!'))
            except ValueError:
                print("Mesa só pode ser números inteiros!Utilize caracteres numéricos!")
            else:
                if players[mesa-1] in cp_players:
                    print(f'Os jogadores {players[mesa-1][0]} e {players[mesa-1][1]} ja receberam o resultado')
                    ch = True
                    while ch:
                        try:
                            mesa = int(input('Escolha outra mesa para receber o resultado o resultado!'))
                            if players[mesa - 1] in cp_players:
                                ch = True
                            else:
                                ch = False
                        except ValueError:
                            print("Mesa só pode ser números inteiros!Utilize caracteres numéricos!")

                try:
                    print(f'Mesa{mesa}:\t Jogador 1:{players[mesa - 1][0]} \t '
                          f'Jogador 2:{players[mesa - 1][1]}')
                    jogador = int(input('Qual Jogador foi o vencedor? Ou houve Empate?\n'
                                        '1: Jogador 1 Venceu\n'
                                        '2: Jogador 2 Venceu\n'
                                        '3: Empate'))
                except ValueError:
                    print("Escolha as opções 1,2 ou 3!\n"
                          "Utilize caracteres numéricos!")
                else:
                    if jogador == 3:
                        cp_players.append(players[mesa - 1])
                        swiss.setting_draw(players[mesa-1][0], players[mesa-1][1])
                        swiss.tie_breaking_sb(players[mesa-1][0])
                        swiss.tie_breaking_sb(players[mesa - 1][1])
                        print('Resultado recebido')
                    elif jogador == 1:
                        cp_players.append(players[mesa - 1])
                        swiss.setting_won_losses(players[mesa-1][0], players[mesa-1][1])
                        swiss.tie_breaking_sb(players[mesa-1][0])
                        swiss.tie_breaking_sb(players[mesa - 1][1])
                        print('Resultado recebido')
                    elif jogador == 2:
                        cp_players.append(players[mesa - 1])
                        swiss.setting_won_losses(players[mesa-1][1], players[mesa-1][0])
                        swiss.tie_breaking_sb(players[mesa-1][0])
                        swiss.tie_breaking_sb(players[mesa - 1][1])
                        print('Resultado recebido')
                    else:
                        print(f'O Valor {jogador} não foi encontrado')


if __name__ == '__main__':
    menu = 1
    registered_players = []
    while menu != 0:

        print('Menu')
        print('0:Fechar Aplicação')
        print('1: Registar/Alterar/Deletar Jogador')
        print('2: Começar campeonato')
        print('3:Exportar campeonato')
        
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

                # registering the players
                elif menu_choice == 1:
                    name = str(input('Nome do Jogador:'))
                    last_name = str(input('Sobrenome do Jogador:'))
                    registered_players.append(Player.Player(name, last_name))

                # altering players
                elif menu_choice == 2:
                    name_altered = str(input('Digite o Nome do usuário a ser alterado:')).upper()
                    last_name_altered = str(input('Digite o Sobrenome do usuário a ser alterado')).upper()
                    to_be_altered = name_altered + last_name_altered
                    for loop in registered_players:
                        if to_be_altered == str(loop.name + loop.last_name).upper():
                            new_name = str(input("Digite o Nome a ser alterado:"))
                            new_last_name = str(input("Digite o Sobrenome a ser alterado:"))
                            loop.name_setter(new_name)
                            loop.last_name_setter(new_last_name)

                # deleting player
                elif menu_choice == 3:
                    name_remove = str(input('Digite o Nome do Jogador a Ser removido:')).upper()
                    last_name_remove = str(input('Digite o Sobrenome do Jogador a Ser removido:')).upper()
                    to_be_removed = name_remove + last_name_remove
                    if to_be_removed not in registered_players:
                        print('Não Há jogadores com esse nome registrado')
                    for loop in registered_players:
                        if to_be_removed == str(loop.name + loop.last_name).upper():
                            print(f'Você tem certeza que deseja deletar {loop.name} {loop.last_name}? ')
                            sure = int(input('1: Sim\n2: Não'))
                            if sure == 1:
                                registered_players.remove(loop)
                            else:
                                break

                # printing the players/done
                elif menu_choice == 4:
                    for obj in registered_players:
                        print(obj)

        # starting championship
        elif menu == 2:
            if len(registered_players) == 0:  # checking if there is no players registered
                print('Não há Jogadores registrados!')
                break
            else:
                swiss = Swiss(registered_players)
                swiss.starting()
                rounds = swiss.number_of_rounds_swiss()
                print(f'Serão {rounds} rodadas')
                for i in range(rounds):
                    if i == 0:
                        first_round = swiss.first_pairing()
                        for j in range(len(first_round)):
                            print(f'Mesa{j+1}:\t{first_round[j][0]}\t vs \t{first_round[j][1]}')
                        apply_results_players_swiss(first_round)
                        swiss.setting_points(registered_players)
                        for player in registered_players:
                            print(f'Resultados da rodada{i+1}:\t'
                                  f'{player}:Vitorias:{len(swiss.__getitem__(player,"WIN"))}\t'
                                  f'Derrotas:{len(swiss.__getitem__(player,"LOSSES"))}\t'
                                  f'Empates:{len(swiss.__getitem__(player,"DRAW"))}\t'
                                  f'Pontos:{swiss.__getitem__(player,"POINTS")}\n')
                    else:
                        print(f'Round{i+1}')
                        n_round = swiss.pairing()
                        for j in range(len(n_round)):
                            print(f'Mesa{j + 1}:\t{n_round[j][0]}\t vs \t{n_round[j][1]}')
                        apply_results_players_swiss(n_round)
                        swiss.setting_points(registered_players)
                        for player in registered_players:
                            print(f'Resultados da rodada{i+1}:\t'
                                  f'{player}:Vitorias:{len(swiss.__getitem__(player,"WIN"))}\t'
                                  f'Derrotas:{len(swiss.__getitem__(player,"LOSSES"))}\t'
                                  f'Empates:{len(swiss.__getitem__(player,"DRAW"))}\t'
                                  f'Pontos:{swiss.__getitem__(player,"POINTS")}\n')

        # exporting the championship sheet
        elif menu == 3:
            pass
