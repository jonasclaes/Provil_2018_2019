#!/bin/python3
# TicTacToe - Jonas Claes
import os, random

class TicTacToe:
    board = []
    playerCharacter = ""
    computerCharacter = ""

    WIN_COMBINATIONS = [
        # Horizontal
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # Vertical
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # Diagonal
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board(self):
        # Print top line
        print(chr(9484) + chr(9472) + chr(9472) + chr(9472) + chr(9516) + chr(9472) + chr(9472) + chr(9472) + chr(9516) + chr(9472) + chr(9472) + chr(9472) + chr(9488))

        # Print first row
        print(chr(9474) + chr(8194) + self.board[6] + chr(8194) + chr(9474) + chr(8194) + self.board[7] + chr(8194) + chr(9474) + chr(8194) + self.board[8] + chr(8194) + chr(9474))

        # Print first line
        print(chr(9500) + chr(9472) + chr(9472) + chr(9472) + chr(9532) + chr(9472) + chr(9472) + chr(9472) + chr(9532) + chr(9472) + chr(9472) + chr(9472) + chr(9508))

        # Print second row
        print(chr(9474) + chr(8194) + self.board[3] + chr(8194) + chr(9474) + chr(8194) + self.board[4] + chr(8194) + chr(9474) + chr(8194) + self.board[5] + chr(8194) + chr(9474))

        # Print second line
        print(chr(9500) + chr(9472) + chr(9472) + chr(9472) + chr(9532) + chr(9472) + chr(9472) + chr(9472) + chr(9532) + chr(9472) + chr(9472) + chr(9472) + chr(9508))

        # Print third row
        print(chr(9474) + chr(8194) + self.board[0] + chr(8194) + chr(9474) + chr(8194) + self.board[1] + chr(8194) + chr(9474) + chr(8194) + self.board[2] + chr(8194) + chr(9474))

        # Print last line
        print(chr(9492) + chr(9472) + chr(9472) + chr(9472) + chr(9524) + chr(9472) + chr(9472) + chr(9472) + chr(9524) + chr(9472) + chr(9472) + chr(9472) + chr(9496))

    def choose_player_character(self):
        while not (self.playerCharacter == "X" or self.playerCharacter == "O"):
            self.playerCharacter = input("Do you want to be X or O? ").upper()
        if self.playerCharacter == "X":
            self.computerCharacter = "O"
            print("You are playing as X.")
        else:
            self.computerCharacter = "X"
            print("You are playing as O.")

    @staticmethod
    def choose_starting_player():
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    @staticmethod
    def check_free(board, pos):
        return board[pos] == " "

    @staticmethod
    def check_win(board, character):
        for combination in TicTacToe.WIN_COMBINATIONS:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] == character:
                return True
        return False

    def check_board_full(self):
        for i in range(9):
            if self.check_free(self.board, i):
                return False
        return True

    def copy_board(self):
        return self.board.copy()

    @staticmethod
    def choose_random_move_from_list(board, moves):
        possible_moves = []
        for move in moves:
            if TicTacToe.check_free(board, move):
                possible_moves.append(move)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None

    def get_computer_move(self):
        for i in range(9):
            copied_board = self.copy_board()
            if TicTacToe.check_free(copied_board, i):
                TicTacToe.move(copied_board, i, self.computerCharacter)
                if TicTacToe.check_win(copied_board, self.computerCharacter):
                    return i

        for i in range(9):
            copied_board = self.copy_board()
            if TicTacToe.check_free(copied_board, i):
                TicTacToe.move(copied_board, i, self.playerCharacter)
                if TicTacToe.check_win(copied_board, self.playerCharacter):
                    return i

        if TicTacToe.check_free(self.board, 4):
            return 4

        move = TicTacToe.choose_random_move_from_list(self.board, [0, 2, 6, 8])
        if move is not None:
            return move

        return TicTacToe.choose_random_move_from_list(self.board, [1, 3, 5, 7])

    @staticmethod
    def move(board, pos, character):
        board[pos] = character

    def get_player_move(self):
        move = ""
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            move = input("What is your next move? [1-9] ")
            if not TicTacToe.check_free(self.board, int(move) - 1):
                print("This space has already been taken.")
        return int(move)

    @staticmethod
    def play_again():
        return input("Do you want to play again? [Y/n] ").lower().startswith("y")

    @staticmethod
    def run():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Welcome to TicTacToe!")
            ttt = TicTacToe()
            ttt.choose_player_character()
            turn = ttt.choose_starting_player()
            print("%s will go first." % turn.title())
            game_over = False

            while not game_over:
                if turn == 'player':
                    ttt.print_board()
                    move = ttt.get_player_move() - 1
                    TicTacToe.move(ttt.board, move, ttt.playerCharacter)

                    if TicTacToe.check_win(ttt.board, ttt.playerCharacter):
                        ttt.print_board()
                        print("Good game! You won!")
                        game_over = True
                    else:
                        if ttt.check_board_full():
                            ttt.print_board()
                            print("It's a tie")
                            break
                        else:
                            turn = 'computer'

                else:
                    move = ttt.get_computer_move()
                    TicTacToe.move(ttt.board, move, ttt.computerCharacter)

                    if TicTacToe.check_win(ttt.board, ttt.computerCharacter):
                        ttt.print_board()
                        print("Yikes, the computer won!")
                        game_over = True
                    else:
                        if ttt.check_board_full():
                            ttt.print_board()
                            print("It's a tie")
                            break
                        else:
                            turn = 'player'

            if not TicTacToe.play_again():
                break


TicTacToe.run()
