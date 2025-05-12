import os
from player import Player
from board import Board
from menus import Menu

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
class Game:
    def __init__(self):
     self.players = [Player() , Player()]
     self.board = Board()
     self.menu = Menu()
     self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number , player in enumerate(self.players , start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.reset_game()
                    break

    def quit_game(self):
        print("Thanks for playing!")

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn({player.symbol}):")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1<= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number 1 and 9.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def reset_game(self):
        self.board.reset_board()
        self.current_player_index = 0
    def check_win(self):
        return False

    def check_draw(self):
        return False

game = Game()
game.start_game()
