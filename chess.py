import sys
f=open(sys.argv[1],"r")
commands=[line.split() for line in f.readlines()]
f.close()

#### CHESS BOARD ####
chess_board=[]
def board():
    global chess_board
    chess_board=['','','','','','','','','']
    chess_board[8]=['','R1','N1','B1','QU','KI','B2','N2','R2']
    chess_board[7]=['','P1','P2','P3','P4','P5','P6','P7','P8']
    chess_board[6]=['','  ','  ','  ','  ','  ','  ','  ','  ']
    chess_board[5]=['','  ','  ','  ','  ','  ','  ','  ','  ']
    chess_board[4]=['','  ','  ','  ','  ','  ','  ','  ','  ']
    chess_board[3]=['','  ','  ','  ','  ','  ','  ','  ','  ']
    chess_board[2]=['','p1','p2','p3','p4','p5','p6','p7','p8']
    chess_board[1]=['','r1','n1','b1','qu','ki','b2','n2','r2']
    chess_board[0]=['','  ','  ','  ','  ','  ','  ','  ','  ']
    return chess_board

board_copy= board().copy()

black={'pawn':['P1','P2','P3','P4','P5','P6','P7','P8'],\
       'rook':['R1','R2'],\
       'knight':['N1','N2'],\
       'bishop':['B1','B2'],\
       'queen':['QU'],\
       'king':['KI']}

white={'pawn':['p1','p2','p3','p4','p5','p6','p7','p8'],\
       'rook':['r1','r2'],\
       'knight':['n1','n2'],\
       'bishop':['b1','b2'],\
       'queen':['qu'],\
       'king':['ki']}

black_list=[piece for value in black.values() for piece in value]
white_list=[piece for value in white.values() for piece in value]

def is_white(piece):        
    if piece in white_list:
        return True
    elif piece in black_list:
        return False

def position(piece):       
    for i in board_copy:
        if piece in i:
            pos=[board_copy.index(i),i.index(piece)]
            return pos

def letter2numb(input):
    letter2pos= ["", "a", "b", "c", "d", "e", "f", "g", "h"]
    pos_x=  letter2pos.index(input[0])
    pos_y=  int(input[1])
    position=[pos_y,pos_x]
    return position

def numb2letter(x,y):
    pos2letter=["", "a", "b", "c", "d", "e", "f", "g", "h"]
    pos_y= pos2letter[y]
    pos_x= str(x)
    position= pos_y+pos_x
    return position

def initialize():
    global board_copy
    board_copy = board().copy()
    for i in range(8,0,-1):
        print(" ".join(board()[i]))


def is_occupied(object,position):
    x=letter2numb(position)[0]
    y=letter2numb(position)[1]
    if is_white(object):
        if board_copy[x][y]=="  ":
            return False
        elif is_white(board_copy[x][y]) or board_copy[x][y]=="KI":
            return True
        elif not is_white(board_copy[x][y]):
            return False

    elif not is_white(object):
        if board_copy[x][y]=="  ":
            return False
        elif not is_white(board_copy[x][y]) or board_copy[x][y]=="ki":
            return True
        elif is_white(board_copy[x][y]):
            return False

def showmoves(piece):
    pos_numb=position(piece)
    y=int(pos_numb[0])
    x=int(pos_numb[1])
    current_pos=numb2letter(y,x)
    showmoves=[]

    def bishop1(opposite):
        nonlocal x
        nonlocal y
        a = [x, y]
        b = [x, y]
        while True:
            y = y - 1
            x = x + 1
            if y == 0 or x == 9:
                break

            if not is_occupied(piece, numb2letter(y, x)):
                showmoves.append(numb2letter(y, x))
                if board_copy[y][x] in opposite:
                    break

            if is_occupied(piece, numb2letter(y, x)):
                break
        x = a[0]
        y = a[1]
        while True:
            y = y - 1
            x = x - 1
            if y == 0 or x == 0:
                break

            if not is_occupied(piece, numb2letter(y, x)):
                showmoves.append(numb2letter(y, x))
                if board_copy[y][x] in opposite:
                    break
            if is_occupied(piece, numb2letter(y, x)):
                break
        x=b[0]
        y=b[1]

    def bishop2(opposite):
        nonlocal x
        nonlocal y
        a = [x, y]
        b = [x, y]
        while True:
            y = y + 1
            x = x + 1
            if y == 9 or x == 9:
                break

            if not is_occupied(piece, numb2letter(y, x)):
                showmoves.append(numb2letter(y, x))
                if board_copy[y][x] in opposite:
                    break
            if is_occupied(piece, numb2letter(y, x)):
                break
        x = a[0]
        y = a[1]
        while True:
            y = y + 1
            x = x - 1
            if y == 9 or x == 0:
                break

            if not is_occupied(piece, numb2letter(y, x)):
                showmoves.append(numb2letter(y, x))
                if board_copy[y][x] in opposite:
                    break
            if is_occupied(piece, numb2letter(y, x)):
                break
        x = b[0]
        y = b[1]

    def rook(opposite):
        while True:
            for i in range(x-1,0,-1):
                if not is_occupied(piece,numb2letter(y,i)):
                    showmoves.append(numb2letter(y, i))
                    if board_copy[y][i] in opposite:
                        break

                if is_occupied(piece,numb2letter(y,i)):
                    break

            for i in range(x+1,9):
                if not is_occupied(piece,numb2letter(y,i)):
                    showmoves.append(numb2letter(y, i))
                    if board_copy[y][i] in opposite:
                        break

                if is_occupied(piece,numb2letter(y,i)):
                    break

            for i in range(y+1,9):
                if not is_occupied(piece,numb2letter(i,x)):
                    showmoves.append(numb2letter(i, x))
                    if board_copy[i][x] in opposite:
                        break

                if is_occupied(piece,numb2letter(i,x)):
                    break

            for i in range(y-1,0,-1):
                if not is_occupied(piece,numb2letter(i,x)):
                    showmoves.append(numb2letter(i, x))
                    if board_copy[i][x] in opposite:
                        break

                if is_occupied(piece,numb2letter(i,x)):
                    break
            break

    def knight():
        diagonal_list = []
        diagonal_list2 = []
        l_list = []
        l_list2 = []
        while True:
            if (y + 2 < 9 or y - 2 > 0) and (x + 2 < 9 or x - 2 > 0):
                for row in range(y + 2, y - 3, -1):
                    for column in range(x - 2, x + 3):
                        if row == y or column == x:
                            continue
                        if row == y + 2:
                            if column == x - 2 or column == x + 2:
                                continue
                            else:
                                l_list.append([row, column])

                        if row == y - 2:
                            if column == x - 2 or column == x + 2:
                                continue
                            else:
                                l_list.append([row, column])

                        if row == y + 1:
                            if column == x - 2 or column == x + 2:
                                l_list.append([row, column])
                            else:
                                diagonal_list.append([row, column])

                        if row == y - 1:
                            if column == x - 2 or column == x + 2:
                                l_list.append([row, column])
                            else:
                                diagonal_list.append([row, column])
            for i in l_list:
                if i[0] < 9 and i[1] > 0:
                    if i[1] < 9 and i[0] > 0:
                        if is_occupied(piece, numb2letter(*i)):
                            continue
                        else:
                            l_list2.append(i)
                    else:
                        continue

            for i in diagonal_list:
                if i[0] < 9 and i[1] > 0:
                    if i[1] < 9 and i[0] > 0:
                        if is_occupied(piece, numb2letter(*i)):
                            continue
                        else:
                            if board_copy[i[0]][i[1]] == "  ":
                                diagonal_list2.append(i)
                            else:
                                continue
                    else:
                        continue
            for location in l_list2:
                if numb2letter(*location)[1] == "0":
                    break
                showmoves.append(numb2letter(*location))
            for location in diagonal_list2:
                if numb2letter(*location)[1] == "0":
                    break
                showmoves.append(numb2letter(*location))
            break

    def king(opposite):
        while True:
            for i in range(x - 1, x-2, -1):
                if x-1==0:
                    break
                if not is_occupied(piece, numb2letter(y, i)):
                    showmoves.append(numb2letter(y, i))

                if is_occupied(piece, numb2letter(y, i)):
                    break

            for i in range(x + 1, x+2):
                if x+1==9:
                    break
                if not is_occupied(piece, numb2letter(y, i)):
                    showmoves.append(numb2letter(y, i))

                if is_occupied(piece, numb2letter(y, i)):
                    break

            for i in range(y + 1, y+2):
                if y+1==9:
                    break
                if x-1!=0:
                    if not is_occupied(piece,numb2letter(i,x-1)):
                        showmoves.append(numb2letter(i,x-1))
                if x+1!=9:
                    if not is_occupied(piece,numb2letter(i,x+1)):
                        showmoves.append(numb2letter(i,x+1))

                if not is_occupied(piece, numb2letter(i, x)):
                    showmoves.append(numb2letter(i, x))

                if is_occupied(piece, numb2letter(i, x)):
                    break

            for i in range(y - 1, y-2, -1):
                if y-1==0:
                    break
                if x-1!=0:
                    if not is_occupied(piece,numb2letter(i,x-1)):
                        showmoves.append(numb2letter(i,x-1))
                if x+1!=9:
                    if not is_occupied(piece,numb2letter(i,x+1)):
                        showmoves.append(numb2letter(i,x+1))

                if not is_occupied(piece, numb2letter(i, x)):
                    showmoves.append(numb2letter(i, x))

                if is_occupied(piece, numb2letter(i, x)):
                    break
            break

    if piece in black['pawn']:     # BLACK PAWN MOVES
        next_pos = numb2letter(y - 1, x)
        if not is_occupied(piece,next_pos):
            showmoves.append(next_pos)
            return showmoves
        elif is_occupied(piece,next_pos):
            return showmoves

    if piece in black['rook']:
        rook(white_list)

    if piece in black['knight']:
        knight()

    if piece in black['bishop']:
        bishop1(white_list)

    if piece in black['queen']:
        rook(white_list)
        bishop1(white_list)
        bishop2(white_list)

    if piece in black['king']:
        king(white_list)

    if piece in white['pawn']:
        if not is_occupied(piece, numb2letter(y +1, x)):
            showmoves.append(numb2letter(y+1, x))
            return showmoves
        elif is_occupied(piece, numb2letter(y +1, x)):
            return showmoves

    if piece in white['rook']:
        rook(black_list)

    if piece in white['knight']:
        knight()

    if piece in white['bishop']:
        bishop2(black_list)

    if piece in white['queen']:
        rook(black_list)
        bishop1(black_list)
        bishop2(black_list)

    if piece in white['king']:
        king(black_list)

    return(sorted(showmoves))

def move(piece,to_go):
    point=letter2numb(to_go)
    row=position(piece)[0]
    column=position(piece)[1]
    if to_go in showmoves(piece):
        board_copy[row][column]="  "
        board_copy[point[0]][point[1]]=piece
        return True
    else:
        return False

def print_2():
    print(" -----------------------")
    for i in range(8, 0, -1):
        print(" ".join(board_copy[i]))
    print(" -----------------------")

def command_line(commands):

    for cmd in commands:
        if "move" in cmd:
            piece=cmd[1]
            to_go=cmd[2]
            print(">",*cmd)
            pos=letter2numb(cmd[2])
            if move(piece,to_go):
                print("OK")
            else:
                print("FAILED")

        elif "showmoves" in cmd:
            piece=cmd[1]
            print(">",*cmd)
            if showmoves(piece)==[]:
                print("FAILED")
            else:
                print(" ".join(showmoves(piece)))


        elif "print" in cmd:
            print(">",*cmd)
            print_2()

        elif "initialize" in cmd:
            print(">",*cmd)
            print("OK")
            print(" -----------------------")
            initialize()
            print(" -----------------------")
            board_copy=chess_board

        elif "exit" in cmd:
            print(">",*cmd)
            exit()


command_line(commands)










