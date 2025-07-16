def clear():
    print("\n" * 100)  # убираем из видимости старое игровое поле


# отображаем игровое поле


def display_board(board):
    clear()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[1] + "|" + board[2] + "|" + board[3])


def player_input():

    marker = ""

    while marker != "X" and marker != "O":
        marker = input('Игрок 1, пожалуйста, выберите "X" или "O":').upper()

    # распределение Х и О
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


player1, player2 = player_input()

# размещение маркера


def place_marker(board, marker, position):
    board[position] = marker


# проверка на победу


def win_check(board, mark):

    return (
        (
            board[7] == mark and board[8] == mark and board[9] == mark
        )  # горизонталь сверху
        or (
            board[4] == mark and board[5] == mark and board[6] == mark
        )  # горизонталь в середине
        or (
            board[1] == mark and board[2] == mark and board[3] == mark
        )  # горизонталь снизу
        or (
            board[7] == mark and board[4] == mark and board[1] == mark
        )  # вертикаль слева
        or (
            board[8] == mark and board[5] == mark and board[2] == mark
        )  # вертикаль в середине
        or (
            board[9] == mark and board[6] == mark and board[3] == mark
        )  # вертикаль справа
        or (board[7] == mark and board[5] == mark and board[3] == mark)  # диагональ
        or (board[9] == mark and board[5] == mark and board[1] == mark)
    )  # диагональ


# кто ходит первым

import random


def choose_first():
    if random.randint(0, 1) == 0:
        return "Первым ходит Игрок 1"
    else:
        return "Первым ходит Игрок 2"


# проверяем пустое ли поле


def space_check(board, position):
    return board[position] == " "


# проверяем все ли поле занято


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# спрашиваем игрока о его ходе


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(
        board, position
    ):
        position = int(input("Выберите какое поле хотите отметить: (1-9)"))

    return position


# спрашиваем игрока о новой игре


def new_play():

    choice = input('Хотите сыграть снова? Введите "YES" или "NO":').upper()

    return choice == "YES"


# Приветствие игрока

print('Добро пожаловать в игру "Крестики-Нолики"!')
print()
print("Как выглядит поле. Цифры это номер поля для хода")
print()
print("7" + "|" + "8" + "|" + "9")
print("-----")
print("4" + "|" + "5" + "|" + "6")
print("-----")
print("1" + "|" + "2" + "|" + "3")
print()

# реализация всех функций для игры

import time

time.sleep(0.2)

while True:
    # Настройка игры
    theBoard = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print("Первым ходит " + turn + ".")

    play_game = input('Вы готовы играть? Введите "YES" или "NO".')

    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Игрок 1":
            # Ход Игрока 1

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Поздравляю! Вы выиграли!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Ничья!")
                    break
                else:
                    turn = "Игрок 2"

        else:
            # Ход Игрока 2

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Игрок 2 выиграл!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Ничья!")
                    break
                else:
                    turn = "Игрок 1"

    if not new_play():
        break
