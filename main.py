import random
import time

class state:
    def __init__(self,width,height,board = None):
        self.width = width
        self.height = height
        self.board = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)] if not board else board
    def update(self,r,c,val):
        self.board[r][c] = val
    def clear(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
    def __eq__(self,other):
        return self.board == other.board

def render_board(board):
    for row in board.board:
        print(' '.join(str(x) for x in row))

def check_neighbors(r,c,board):
    tot = 0
    for i in range (r-1,r+2):
        for j in range(c-1,c+2):
            if i == r and j == c:
                continue
            if i < 0 or j < 0 or i >= board.height or j >= board.width:
                continue
            tot += board.board[i][j]
    return tot

def next_board_state(old_state):
    res = state(old_state.width,old_state.height)
    for r in range(old_state.height):
        for c in range(old_state.width):
            res.update(r,c,old_state.board[r][c])
            n_neighbors = check_neighbors(r,c,old_state)
            if n_neighbors <= 1:
                res.update(r,c,0)
            if n_neighbors > 3:
                res.update(r,c,0)
            if old_state.board[r][c] == 0 and n_neighbors == 3:
                res.update(r,c,1)
    return res

if __name__ == "__main__":
    board = state(5,5)
    while 1:
        time.sleep(0.5)
        render_board(board)
        print('~~~~')
        board = next_board_state(board)