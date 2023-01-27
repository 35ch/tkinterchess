import tkinter

# TODO: remove available squares outside the board in the find_available_squares method.
# Alternate the command of the buttons from click to play

#[[ '♖',  '♘',  '♗',  '♕',  '♔',  '♗',  '♘',  '♖'], 
# [ '♙',  '♙',  '♙',  '♙',  '♙',  '♙',  '♙',  '♙'], 
# [None, None, None, None, None, None, None, None], 
# [None, None, None, None, None, None, None, None], 
# [None, None, None, None, None, None, None, None], 
# [None, None, None, None, None, None, None, None], 
# [ '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎'], 
# [ '♜',  '♞',  '♝',  '♛',  '♚',  '♝',  '♞',  '♜']]

class Chess:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(0,0)

        self.current_piece = None
        self.white_pieces = ["♔", "♕", "♖", "♗", "♘", "♙"]
        self.black_pieces = ["♚", "♛", "♜", "♝", "♞", "♟︎"]
        self.available_squares = []        
        self.board = []
                
        for row in range(8):
            if row == 0:
                self.board.append(["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"])
            elif row == 1:
                self.board.append(["♙" for i in range(8)])
            elif row == 6:
                self.board.append(["♟︎" for i in range(8)])
            elif row == 7:
                self.board.append(["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"])
            else:
                self.board.append([None for i in range(8)])
        
        self.squares = [[tkinter.Button(self.window) for row in range(8)] for column in range(8)]
        
        for row in range(8):
            for column in range(8):
                if self.squares[row][column] is None:
                    self.squares[row][column].config(state="disabled")

                self.squares[row][column].config(height=1, width=2, text=self.board[row][column],
                                                 font=("Helvetica 20 bold"), command=lambda 
                                                 row=row, column=column: self.click(row, column))
                self.squares[row][column].grid(row=row, column=column)        
        
        
        
        self.rook_available = [
            [-2, -1], [-2, 1], [-1, -2], [-1, 2],
            [2, -1],  [2, 1],   [1, 2], [1, -2]
        ]
        
        self.window.mainloop()
    
    def find_available_squares(self, piece, row, column):
        if piece == "♔" or piece == "♚":
        
            for square in self.king_available:
                if square in self.white_pieces.extend(self.black_pieces):
                    available_squares.remove(square)                        

        elif piece == "♕" or piece == "♛":
            return      

        elif piece == "♖" or piece == "♜":
            return

        elif piece == "♗" or piece == "♝":
            return

        elif piece == "♘" or piece == "♞":
            for square in self.rook_available:
                if (0 <= row+square[0] <= 7 and 
                    0 <= column+square[1] <= 7 and
                    self.board[row+square[0]][column+square[1]] is None and
                    self.board[row+square[0]][column+square[1]] is None):
                    self.available_squares.append(self.squares[row+square[0]][column+square[1]])
                    self.squares[row+square[0]][column+square[1]].config(background="black")

            for r in self.available_squares:
                print(r)
 
        elif piece == "♙" or piece == "♟︎":
            return

    def click(self, row, column):
        square = self.board[row][column]
        
        if (square is not None and 
            self.current_piece is None):
            self.find_available_squares(square, row, column)
            self.current_piece = [row, column]
 
        elif self.current_piece is not None:
            self.play(self.current_piece[0], self.current_piece[1], row, column)
    
    def play(self, previous_row, previous_column, row, column):
        self.board[row][column] = self.board[previous_row][previous_column]
        self.board[previous_row][previous_column] = None

        for i in range(8):
            for r in range(8): 
                print(self.board[i][r], end=" ")
            print()      
            
        self.squares[previous_row][previous_column].config(text=None)
        self.squares[row][column].config(text=self.board[previous_row][previous_column])
        
        self.current_piece = None
    
    def check_checker(self):
        return

Chess()
