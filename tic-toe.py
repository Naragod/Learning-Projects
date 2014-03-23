'''Author Mateo Naranjo

'''

turn = 1
table = [["*" for x in range(3)] for y in range(3)]

def updateMove(content):
    global turn
    
    moves = content  
    sign = "X"
    
    if(table[moves[0]][moves[1]] == "*"):
        if turn == 2:
            sign = "0"
            turn = 1
        else:
            turn = 2      
            
        table[moves[0]][moves[1]] = sign
    else:
        print("You cannot change your opponent's move")
        
def read():
    global turn
    message = "Your move, Player 1: "
    if turn == 2:
        message = "Your move, Player 2 "
           
    pos = raw_input(message)
    res = pos.strip()
    moves = res.split(" ")
    
    x = moves[1]
    y = moves[0]      
 
    return([int(y), int(x)])
   
   
def main():
    count = 1
    while(True):
        print(table[0])
        print(table[1])
        print(table[2])
        updateMove(read())
     
main()