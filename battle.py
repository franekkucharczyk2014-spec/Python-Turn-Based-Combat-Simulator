
import random

enemy_easy_hp = 100
enemy_medium_hp = 150
enemy_hard_hp = 200
enemy_impossible_hp = 250

player_max_hp = 100

enemy_easy_max_hp = 100
enemy_medium_max_hp = 150
enemy_hard_max_hp = 200
enemy_impossible_max_hp = 250

heal_chance = 50

p1_heal_chance = 50
p2_heal_chance = 50

run_chance_easy = 50
run_chance_medium_hard = 25
run_chance_impossible = 0

p1_stun_chance = 25
p2_stun_chance = 25

heals_left_easy = 0
heals_left_medium = 6
heals_left_hard = 8
heals_left_impossible = 10

while True:
    print('1) single player')
    print('2) two player')
    print('3) quit')

    choice = input('Choose an option: ')

    # SINGLE PLAYER
    if choice == '1':

        print('Choose difficulty:')
        print('1) Easy')
        print('2) Medium')
        print('3) Hard')
        print('4) Impossible')

        choice = input('Choose difficulty: ')

        if choice == '1':
            enemy_hp = enemy_easy_hp
            enemy_max_hp = enemy_easy_max_hp
            run_chance = run_chance_easy
            heals_left = heals_left_easy
            enemy_attack_min = 10
            enemy_attack_max = 20

        elif choice == '2':
            enemy_hp = enemy_medium_hp
            enemy_max_hp = enemy_medium_max_hp
            run_chance = run_chance_medium_hard
            heals_left = heals_left_medium
            enemy_attack_min = 12
            enemy_attack_max = 22

        elif choice == '3':
            enemy_hp = enemy_hard_hp
            enemy_max_hp = enemy_hard_max_hp
            run_chance = run_chance_medium_hard
            heals_left = heals_left_hard
            enemy_attack_min = 15
            enemy_attack_max = 25

        elif choice == '4':
            enemy_hp = enemy_impossible_hp
            enemy_max_hp = enemy_impossible_max_hp
            run_chance = run_chance_impossible
            heals_left = heals_left_impossible
            enemy_attack_min = 20
            enemy_attack_max = 30

        else:
            print('Invalid difficulty. Please try again.')
            continue

        player_hp = player_max_hp
        current_heal_chance = heal_chance

        while True:
            healed = False

            print(f"Player HP: {player_hp}/{player_max_hp}")
            print(f"Enemy HP: {enemy_hp}/{enemy_max_hp}")

            choice = input(
                'Choose action: (1) Attack, (2) Heal, (3) Run: '
            )

            # ATTACK
            if choice == '1':
                attack = random.randint(10, 20)
                enemy_hp -= attack

                print(f'You dealt {attack} damage to the enemy.')

            # HEAL
            elif choice == '2':
                if heals_left > 0:
                    heal = random.randint(1, 100)
                    heals_left -= 1

                    if heal <= current_heal_chance:
                        player_hp += 20

                        if player_hp > player_max_hp:
                            player_hp = player_max_hp

                        print(
                            f'You healed yourself for 20 HP. '
                            f'Remaining heals: {heals_left}'
                        )

                        healed = True

                    else:
                        print(
                            f'Healing failed! '
                            f'Remaining heals: {heals_left}'
                        )

                else:
                    print('You have no more heals.')

            # RUN
            elif choice == '3':
                run = random.randint(1, 100)

                if run <= run_chance:
                    print('You managed to escape!')
                    break

                else:
                    print('You failed to escape!')

                    enemy_hp = round(enemy_hp * 1.5)
                    enemy_max_hp = round(enemy_max_hp * 1.5)

                    run_chance /= 1.5
                    current_heal_chance *= 1.1

            else:
                print('Invalid choice. Please try again.')
                continue

            # ENEMY DEFEATED
            if enemy_hp <= 0:
                print('You won!')
                break

            # ENEMY ATTACK
            if not healed:
                enemy_attack = random.randint(
                    enemy_attack_min,
                    enemy_attack_max
                )

                player_hp -= enemy_attack

                print(f'Enemy dealt {enemy_attack} damage to you.')

                if player_hp <= 0:
                    print('You lost!')
                    break

    # TWO PLAYER
    elif choice == '2':

        p1_hp = 100
        p2_hp = 100

        p1_max_hp = 100
        p2_max_hp = 100

        p1_heals_left = 6
        p2_heals_left = 6

        p1_stun = False
        p2_stun = False

        while True:

            # PLAYER 1 STUN CHECK
            if p1_stun:
                print('Player 1 is stunned and cannot act this turn.')
                p1_stun = False
                continue

            print(f'Player 1 hp: {p1_hp}/{p1_max_hp}')
            print(f'Player 2 hp: {p2_hp}/{p2_max_hp}')

            choice = input(
                'Choose action: (1) Attack, (2) Heal, (3) Stun: '
            )

            # PLAYER 1 ATTACK
            if choice == '1':
                p1_attack = random.randint(10, 20)
                p2_hp -= p1_attack

                print(
                    f'Player 1 dealt {p1_attack} damage '
                    f'to Player 2.'
                )

            # PLAYER 1 HEAL
            elif choice == '2':
                if p1_heals_left > 0:
                    heal = random.randint(1, 100)
                    p1_heals_left -= 1

                    if heal <= p1_heal_chance:
                        p1_hp += 20

                        if p1_hp > p1_max_hp:
                            p1_hp = p1_max_hp

                        print(
                            f'Player 1 healed for 20 HP. '
                            f'Remaining heals: {p1_heals_left}'
                        )

                    else:
                        print(
                            f'Healing failed! '
                            f'Remaining heals: {p1_heals_left}'
                        )

                else:
                    print('Player 1 has no more heals.')

            # PLAYER 1 STUN
            elif choice == '3':
                stun = random.randint(1, 100)

                if stun <= p1_stun_chance:
                    print('Player 1 stunned Player 2!')
                    p2_stun = True

                else:
                    print('Player 1 failed to stun Player 2!')

                    p2_hp += 10

                    if p2_hp > p2_max_hp:
                        p2_hp = p2_max_hp

                    p2_heals_left += 1

            else:
                print('Invalid choice. Please try again.')
                continue

            # PLAYER 2 DEFEATED
            if p2_hp <= 0:
                print('Player 1 won!')
                break

            # PLAYER 2 STUN CHECK
            if p2_stun:
                print('Player 2 is stunned and cannot act this turn.')
                p2_stun = False
                continue

            print(f'Player 1 hp: {p1_hp}/{p1_max_hp}')
            print(f'Player 2 hp: {p2_hp}/{p2_max_hp}')

            choice = input(
                'Choose action: (1) Attack, (2) Heal, (3) Stun: '
            )

            # PLAYER 2 ATTACK
            if choice == '1':
                p2_attack = random.randint(10, 20)
                p1_hp -= p2_attack

                print(
                    f'Player 2 dealt {p2_attack} damage '
                    f'to Player 1.'
                )

            # PLAYER 2 HEAL
            elif choice == '2':
                if p2_heals_left > 0:
                    heal = random.randint(1, 100)
                    p2_heals_left -= 1

                    if heal <= p2_heal_chance:
                        p2_hp += 20

                        if p2_hp > p2_max_hp:
                            p2_hp = p2_max_hp

                        print(
                            f'Player 2 healed for 20 HP. '
                            f'Remaining heals: {p2_heals_left}'
                        )

                    else:
                        print(
                            f'Healing failed! '
                            f'Remaining heals: {p2_heals_left}'
                        )

                else:
                    print('Player 2 has no more heals.')

            # PLAYER 2 STUN
            elif choice == '3':
                stun = random.randint(1, 100)

                if stun <= p2_stun_chance:
                    print('Player 2 stunned Player 1!')
                    p1_stun = True

                else:
                    print('Player 2 failed to stun Player 1!')

                    p1_hp += 10

                    if p1_hp > p1_max_hp:
                        p1_hp = p1_max_hp

                    p1_heals_left += 1

            else:
                print('Invalid choice. Please try again.')
                continue

            # PLAYER 1 DEFEATED
            if p1_hp <= 0:
                print('Player 2 won!')
                break

    # QUIT
    elif choice == '3':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Please try again.')
