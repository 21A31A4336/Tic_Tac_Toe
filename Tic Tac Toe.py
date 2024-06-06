def printboard(board):
    print("-"*20)
    for row in board:
        print("   |    ".join(row))
        print("--"*10)
    print('*'*20)
def isfull(board):
    for row in board:
        for col in row:
            if col!="":
                return False
    else:
        return True
def check(board,pl):
    #HORIZONTAL
    for a in range(3):
        if a==0:
            if board[a][0]==pl and board[a][1]==pl and board[a][2]==pl:
                return True
        if a==1:
            if board[a][0]==pl and board[a][1]==pl and board[a][2]==pl:
                return True
        if a==2:
            if board[a][0]==pl and board[a][1]==pl and board[a][2]==pl:
                return True
    #DIAGONAL
    if board[0][0]==pl and board[1][1]==pl and board[2][2]:
        return True
    elif board[2][0]==pl and board[1][1]==pl and board[0][2]==pl:
        return True
    #VERTICAL
    for a in range(3):
        if a==0:
            if board[0][a]==pl and board[1][a]==pl and board[2][a]==pl:
                return True
        if a==1:
            if board[0][a]==pl and board[1][a]==pl and board[2][a]==pl:
                return True
        if a==2:
            if board[0][a]==pl and board[1][a]==pl and board[2][a]==pl:
                return True

board=[['']*3 for i in range(3)]
print("TIC TAC TOE")
printboard(board)
print("players are X and O")
print("first X turn")
current='x'
while True:
    print("current player is:",current)
    print("enter the dinmension")
    x,y=map(int,input().split())
    if -1<x<3 and -1<y<3:
        if board[x][y]=='':
            board[x][y]=current
            printboard(board)
            if check(board,current):
                print("congrats",current,"wins")
                break

            if isfull(board):
                print("GAME IS DRAW")
                break
            if current=='x':
                current='o'
            else:
                current='x'
    else:
        print("enter valid number")