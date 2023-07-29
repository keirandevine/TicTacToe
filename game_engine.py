import tkinter
import pandas

data = {
    "squares": ['', '', '', '', '', '', '', '', '']
}


class GameEngine:
    def __init__(self):
        self.counter = 1
        self.playerx_turn = True
        self.squares_df = pandas.DataFrame(data)
        self.mark_img = tkinter.PhotoImage('X.png')
        self.mark_str = 'X'
        self.game_over = False
        self.draw = False


    def validate_move(self, player_input):
        """Checks if chosen square is free. If not, produces an error message and prompts player to choose again"""
        value_at_square = self.squares_df.loc['squares', (player_input - 1)]
        if value_at_square == '':
            return self.mark_square
        else:
            prompt = tkinter.Label(text=f"Player {self.mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)


    def mark_square(self, player_input):
        """Marks players chosen square in both the game dataframe"""
        self.squares_df.loc[0, player_input - 1] = self.mark_str


    def check_result(self):
        """Checks for a draw or win result to the game. Sets game over to True when draw or win detected and sets
        self.draw to True when draw detected"""
        if self.squares_df.loc[0, 0] != '' and self.squares_df.loc[0, 1] != '' and self.squares_df.loc[0, 2] != '' and self.squares_df.loc[0, 3] != '' and self.squares_df.loc[0, 4] != '' and self.squares_df.loc[0, 5] != '' and self.squares_df.loc[0, 6] != '' and self.squares_df.loc[0, 7] != '' and self.squares_df.loc[0, 8] != '':
            self.game_over = True
            self.draw = True

        if self.squares_df[0, 0] == self.mark_str and self.squares_df[0, 1] == self.mark_str and self.squares_df[0, 2] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 3] == self.mark_str and self.squares_df[0, 4] == self.mark_str and self.squares_df[0, 5] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 6] == self.mark_str and self.squares_df[0, 7] == self.mark_str and self.squares_df[0, 8] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 0] == self.mark_str and self.squares_df[0, 3] == self.mark_str and self.squares_df[0, 6] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 1] == self.mark_str and self.squares_df[0, 4] == self.mark_str and self.squares_df[0, 7] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 2] == self.mark_str and self.squares_df[0, 5] == self.mark_str and self.squares_df[0, 8] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 0] == self.mark_str and self.squares_df[0, 4] == self.mark_str and self.squares_df[0, 8] == self.mark_str:
            self.game_over = True
        elif self.squares_df[0, 2] == self.mark_str and self.squares_df[0, 4] == self.mark_str and self.squares_df[0, 6] == self.mark_str:
            self.game_over = True


    def set_turns(self):
        """Checks which player's turn it is. Sets players icon as mark_str and mark_img. Sets player prompt.
        Increases move counter"""
        if self.counter % 2 != 0:
            self.playerx_turn = False
            self.mark_img = tkinter.PhotoImage('O.png')
            self.mark_str = 'O'
            prompt = tkinter.Label(text="Player O - It's Your Turn")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)


        elif self.counter % 2 == 0:
            self.playerx_turn = True
            self.mark_img = tkinter.PhotoImage('X.png')
            self.mark_str = 'X'
            prompt = tkinter.Label(text="Player X - It's Your Turn")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
        self.counter += 1









