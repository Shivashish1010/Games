import random

class Game:
    
    def __init__(self, n, winning_number=2048):
        self.max_rows = n
        self.max_cols = n
        self.board = [[0]*n for _ in range(n)]
        self.fill_board(2)
        self.winning_number = winning_number
    
    def fill_board(self, total_fill):
        fill = 0
        while fill<total_fill:
            row = random.randint(0,self.max_rows-1)
            col = random.randint(0,self.max_cols-1)
            if not self.board[row][col]:
                self.board[row][col] = 2
                fill += 1
    
    def reverse_board(self):
        for i in range(self.max_rows):
            self.board[i] = self.board[i][::-1]

    def transpose(self):
        new_mat = [[0]*self.max_cols for _ in range(self.max_rows)]
        for r in range(self.max_rows):
            for c in range(self.max_cols):
                new_mat[c][r] = self.board[r][c]
        
        self.board = new_mat[:]

    def move_left(self):
        moved = False
        for r in range(len(self.board)):
            start_col = 1
            while start_col < self.max_cols and not self.board[r][start_col]:
                start_col += 1

            merged = False

            while start_col<self.max_cols:
                j = start_col
                while j and self.board[r][j-1] == 0:
                    if self.board[r][j]:
                        moved = True
                    self.board[r][j], self.board[r][j-1] = self.board[r][j-1], self.board[r][j]
                    j-=1

                if not merged and j and self.board[r][j-1] == self.board[r][j]:
                    self.board[r][j-1] *= 2
                    self.board[r][j] = 0
                    merged = True
                    moved = True

                start_col += 1
            
        if moved:
            self.fill_board(1)

    def move_right(self):
        self.reverse_board()
        self.move_left()
        self.reverse_board()
    
    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()
    
    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def display_board(self):
        for r in self.board:
            print(*r)
        
        print()

    def is_lost(self):
        for r in range(self.max_rows):
            for c in range(self.max_cols):
                if not self.board[r][c]:
                    return False
                if r+1 < self.max_rows and self.board[r][c] == self.board[r+1][c]:
                    return False
                if c+1 < self.max_cols and self.board[r][c] == self.board[r][c+1]:
                    return False
        
        return True
    
    def is_won(self):
        for r in range(self.max_rows):
            for c in range(self.max_cols):
                if self.board[r][c] == self.winning_number:
                    return True
        
        return False
        
grid = int(input("Enter what NxN grid you want "))
winning_number = int(input("Enter the winning number "))
game1 = Game(grid, winning_number)
print("Game starts!", end='\n\n')
game1.display_board()

while True:
    user_input = input("Give direction ").upper()
    if user_input == 'X':
        break

    elif user_input == 'A':
        game1.move_left()
    
    elif user_input == 'D':
        game1.move_right()
    
    elif user_input == 'W':
        game1.move_up()
    
    elif user_input == 'S':
        game1.move_down()
    
    game1.display_board()

    if game1.is_won():
        print("You Won")
        break

    if game1.is_lost():
        print("You Lost")
        break
