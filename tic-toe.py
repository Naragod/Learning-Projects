'''Author Naragod
   Simple plain text based tic tac toe game.
   To play, enter two intergers separated by a space,
   where the first integer denominates the row and the
   second the column. Whoever stars is player one.
   
   The game will end when the either player fills in a row,
   column, or diagonal with either all X or all 0.
   
   There is no error checking code except for when trying
   to change another player's move. example:
   player 1:0 0
   player 2:0 0
   will produce an appropriate message.
'''

turn = 1
table = [["*" for x in range(3)] for y in range(3)]
numPlays = 0

def updateMove(moves):
    global turn, numPlays
    sign = "X"
   
    if(checkFull() == True):
        print("Game ends in a tie")
        return(True)
        
    if(table[moves[0]][moves[1]] == "*"):       #Can this be improved?
        if turn == 2:
            player = 2
            sign = "0"
            turn = 1
        else:
            turn = 2  
            player = 1
           
        numPlays += 1
        table[moves[0]][moves[1]] = sign
    else:
        print("That space has already been played")
        
    if(checkVictory() == True):
        print("Congratulations Player " + str(player) + " on your victory")
        return(True)
    
def read():
    global turn
    message = "Your move, Player 1: "
    if turn == 2:
        message = "Your move, Player 2: "
           
    pos = raw_input(message)
    res = pos.strip()
    moves = res.split(" ")
   
    x = moves[1]
    y = moves[0]      
 
    return([int(y), int(x)])

def checkVictory():
    for y in range(len(table)):
        for x in range(len(table)):
            if table[y][x] == table[y][0] and table[y][x] == table[y][1] and table[y][x] == table[y][2] and table[y][x] != "*":    #check horizontally for victory
                return(True)
            elif table[y][x] == table[0][0] and table[y][x] == table[1][1] and table[y][x] == table[2][2] and table[y][x] != "*":  #check left-right diagonaly for victory
                return(True)
            elif table[y][x] == table[0][2] and table[y][x] == table[1][1] and table[y][x] == table[2][0] and table[y][x] != "*":  #check right-left diagonally for victory
                return(True)
            elif table[y][x] == table[0][x] and table[y][x] == table[1][x] and table[y][x] == table[2][x] and table[y][x] != "*":  #check vertically for victory
                return(True)
            else:
                return(False)         

def printBoard():
    global table
    
    result = "   "
    print("")
    for y in range(len(table)):
        count = 1
        
        for x in range(len(table)):
            result += table[y][x] + "  "
            if ((count % 3) == 0):
                count = 1
                result += "\n   "            
            count += 1
            
    print(result)

def checkFull():
    global numPlays
    
    if numPlays == 9:
        return(True)
    else:
        return(False)

def main():
    while(True):
        printBoard()
        if updateMove(read()) == True:
            break
        
main()
