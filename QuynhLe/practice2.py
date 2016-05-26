#Class game_board
class game_board():
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
    
    def update_board(self,user, coordinate = []):
        x = coordinate[0]
        y = coordinate[1]
        if self.board[x][y] == 0:
            self.board[x][y] = user.symbol
            return True
        else:
            return False

    def set_position(self, user):
        position = user.set_move()
        while self.update_board(user, position) == False:
            print "This position is already taken!"
            position = user.set_move()
        self.print_board()

    ##How to optimize this part?
    def check_fullboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return False
        return True

    def print_board(self):
        for i in range(len(self.board)):
            print self.board[i]

class user():
    def __init__(self,symbol):
        self.symbol = symbol

    def set_move(self):
        coordinate_raw = list(raw_input(self.symbol + " --> Enter your move (x,y):"))
        coordinate = [int(coordinate_raw[0]) - 1, int(coordinate_raw[2]) - 1]
        return coordinate

if __name__ == "__main__":
    gb = game_board()
## Init 2 users:
    user1 = user(raw_input("User 1: Enter your symbol:"))
    user2 = user(raw_input("User 2: Enter your symbol:"))
    list_users = [user1, user2]

## Game starts
    while True:
        for user in list_users:
            gb.set_position(user)
            if gb.check_fullboard() == True:
                break
        if gb.check_fullboard() == True:
            break
#print fullboard

    print "Game Over!"


