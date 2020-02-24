
#!/usr/bin/env python3
#!/usr/local/bin/python3
# solve_luddy.py : Sliding tile puzzle solver


# Code by: [vansh(vanshah) prashant(psateesh) kartik(admall)]
#
# Based on skeleton code by D. Crandall, September 2019
#
import queue as Q
import sys

# moves for luddy
MOVES_l = { "A": (-2, -1), "B": (-2, 1), "C": (2, -1), "D": (2,1), "E": (-1, -2), "F": (-1, 2), "G": (1, -2), "H": (1,2) }

# moves for circular and original
MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }

def rowcol2ind(row, col):
    return row*4 + col

def ind2rowcol(ind):
    return (int(ind/4), ind % 4)

def valid_index(row, col):
    return 0 <= row <= 3 and 0 <= col <= 3

def swap_ind(list, ind1, ind2):
    return list[0:ind1] + (list[ind2],) + list[ind1+1:ind2] + (list[ind1],) + list[ind2+1:]

def swap_tiles(state, row1, col1, row2, col2):
    return swap_ind(state, *(sorted((rowcol2ind(row1,col1), rowcol2ind(row2,col2)))))

def printable_board(row):
    return [ '%3d %3d %3d %3d'  % (row[j:(j+4)]) for j in range(0, 16, 4) ]

def is_goal(state):
    return sorted(state[:-1]) == list(state[:-1]) and state[-1]==0


# permutation inversion used for luddy , original and circular
    
def permutation_inversion(matrix):
    state_now = matrix[0]
    count = 0 
    #summation = 0
    #print(state_now)
    for i in range(len(state_now)):
        if(state_now[i] != 0):
            for j in range(i,len(state_now)):
                if(state_now[i] > state_now[j] and state_now[j] != 0):
                    count = count + 1
    
    #print(count) 
    #print(state_now)               
    (empty_row, empty_col) = ind2rowcol(state_now.index(0))
    #print(empty_row)
    if(empty_row%2 == 0) :
    #summation = empty_row + count
        if(count%2 == 0):
            return False
        else:
            return True
    elif(empty_row%2 != 0) :
    #summation = empty_row + count
        if(count%2 == 0):
            return True
        else:
            return False

# successor function for original
            
def successors(state):
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    successor = []
    
    for (c, (i, j)) in MOVES.items():
        matrix = []
        if (valid_index(empty_row+i, empty_col+j)):
            matrix = [swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c]
            if(permutation_inversion(matrix)):
                successor.append(matrix)
            
    return successor
# successor function for circular

def successors_c(state):
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    matrix = []
    successor = [] 
    for (c, (i, j)) in MOVES.items():
        if (empty_row + i > 3 ):
            matrix = ((swap_tiles(state, empty_row, empty_col, 0, empty_col + j), c))
            if(permutation_inversion(matrix)):
                successor.append(matrix)
         #   swap with row = 0  and col = empty_column 
        elif(empty_row + i < 0):
            matrix = ((swap_tiles(state, empty_row, empty_col, 3, empty_col + j), c))
            if(permutation_inversion(matrix)):
                successor.append(matrix)
        #    swap with row = 3 and col = empty_column
        elif(empty_col + j > 3 ):
            matrix = ((swap_tiles(state, empty_row, empty_col, empty_row + i, 0), c))
            if(permutation_inversion(matrix)):
                successor.append(matrix)
        #  swap with row = empty_row and col = 0
        elif(empty_col + j < 0):
            matrix = ((swap_tiles(state, empty_row, empty_col, empty_row + i, 3), c))
            if(permutation_inversion(matrix)):
                successor.append(matrix)
        # swap with row = empty_row and col = 3
        elif(valid_index):
            matrix = ((swap_tiles(state, empty_row, empty_col, empty_row + i, empty_col + j ), c))
            if(permutation_inversion(matrix)):
                successor.append(matrix)
            
        #print(matrix)
    return successor
           
# successor function for luddy
    
def successors_l(state):
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    successor = []
    
    for (c, (i, j)) in MOVES_l.items():
        matrix = []
        if (valid_index(empty_row+i, empty_col+j)):
            matrix = [swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c]
            if(permutation_inversion(matrix)):
                successor.append(matrix)
            
    return successor

# heuristic is manhattan distance for original         

def calculate_manhattan_distance(current_board, goal_board):
    summ = 0 
    
    for i in range(16):
        if(goal_board[i] != current_board[i] and current_board[i] != 0):
            
            index = get_index(goal_board,current_board,i)
            (row_c,column_c) = ind2rowcol(i)
            (row_g,column_g) = ind2rowcol(index)
            summ1 = (row_c - row_g)
            summ2 = (column_c - column_g)
            if summ1 < 0 :
                summ1 = -summ1
            if summ2 < 0 :
                summ2 = -summ2
               
            summ = summ1 + summ2 + summ
        else :
            summ = summ + 0
    #print(summ)
    return summ   
               ## find the index 
                
        
## to find indexes of all the elements in the array
def get_index(goal_board,current_board,i):
    index = goal_board.index(current_board[i])
    #print(index)
    return index


# heuristic for misplaced tiles
def calculate_manhattan_distance_c(current_board, goal_board):
    summ = 0 
    for i in range(16):
        if(goal_board[i] != current_board[i] and current_board[i] != 0):
            
            summ = summ + 1
    return summ  


# successors used for calculating heuristic for luddy
def successors_distance1(state , position):
    matrix = []
    successor = []
    (empty_row, empty_col) = ind2rowcol(state.index(position))
    for(c, (i, j)) in MOVES_l.items():
        if valid_index(empty_row+i, empty_col+j):
            
            matrix = [swap_tiles(state , empty_row , empty_col ,empty_row+i, empty_col+j) , c]
            successor.append(matrix)
    return successor


# bfs required  for solving  luddy
def calculating_moves1(current_board6 , goal6 , position):
    fringe = [ (current_board6, "") ]
    
    
    visited = []
    
    while len(fringe) > 0:
        (state, route_so_far) = fringe.pop()
        visited.append(state)
        #print(state)
        if goal6 == state:
            return( route_so_far )
        
        for(succ, move) in successors_distance1( state , position):
            
            if succ not in visited:
                
                fringe.insert(0, (succ, route_so_far + move ) )
                
        
    return False

# heuristic function for calculating luddy

def calculate_manhattan_distance_l(current_board, goal_board):
    summ = 0
    for i in range(1,16):
        current_board1  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        goal1  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        position = current_board.index(i)
        current_board1[position] = i 
        goal1[i - 1] = i
        
        route1 = calculating_moves1(tuple(current_board1) , tuple(goal1), i )
        summ = len(route1) + summ
        
    
    return summ


# solve/search function for cicular    

def solve_c(initial_board):
    current_dist = 0
    goal_board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    fringe = Q.PriorityQueue()

    cost_i = calculate_manhattan_distance_c(initial_board , goal_board)
    #print(cost_i)
    fringe.put((cost_i + current_dist, current_dist, initial_board, "" ))
    
    visited=[]
    
    
    while not fringe.empty():
        
        (cost ,current_dist,state, route_so_far) = fringe.get()
        visited.append(state)
        #print(cost ,current_dist,state, route_so_far)
        if is_goal(state):
            return( route_so_far  )
        for (succ, move) in successors_c( state ):
          
            # if succ is there in the node than compare cost ... if cost is less only than we will take 
            
            if succ not in visited:
                
            
                
                #visited.append(succ)
                fringe.put((calculate_manhattan_distance_c(succ ,goal_board) + current_dist + 1 ,current_dist + 1, succ, route_so_far + move   ))
                
        #print(fringe.queue)
    return False


### search for original 

def solve(initial_board):
    current_dist = 0
    goal_board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    fringe = Q.PriorityQueue()

    cost_i = calculate_manhattan_distance(initial_board , goal_board)
    #print(cost_i)
    fringe.put((cost_i + current_dist, current_dist, initial_board, "" ))
    
    visited=[]
    
    
    while not fringe.empty():
        
        (cost ,current_dist,state, route_so_far) = fringe.get()
        visited.append(state)
        #print(cost ,current_dist,state, route_so_far)
        if is_goal(state):
            return( route_so_far  )
        for (succ, move) in successors( state ):
          
            # if succ is there in the node than compare cost ... if cost is less only than we will take 
            
            if succ not in visited:
                
            
                
                #visited.append(succ)
                fringe.put((calculate_manhattan_distance(succ ,goal_board) + current_dist + 1 ,current_dist + 1, succ, route_so_far + move   ))
                
        #print(fringe.queue)
    return False

  # search for luddy  

def solve_l(initial_board):
    current_dist = 0
    goal_board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    fringe = Q.PriorityQueue()

    cost_i = calculate_manhattan_distance_l(initial_board , goal_board)
    #print(cost_i)
    fringe.put((cost_i + current_dist, current_dist, initial_board, "" ))
    
    visited=[]
    
    
    while not fringe.empty():
        
        (cost ,current_dist,state, route_so_far) = fringe.get()
        visited.append(state)
        #print(cost ,current_dist,state, route_so_far)
        if is_goal(state):
            return( route_so_far  )
        for (succ, move) in successors_l( state ):
          
            # if succ is there in the node than compare cost ... if cost is less only than we will take 
            
            if succ not in visited:
                
            
                
                #visited.append(succ)
                fringe.put((calculate_manhattan_distance_l(succ ,goal_board) + current_dist + 1 ,current_dist + 1, succ, route_so_far + move   ))
                
        #print(fringe.queue)
    return False


    
# test cases
if __name__ == "__main__":
    
    start_state = []
    k = (sys.argv[1])
    #k = ("/Users/vanshsmacpro/Desktop/admall-psateesh-vanshah-a1/part1/board4")
    with open(k, 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

           
    if len(start_state) != 16:
        raise(Exception("Error: couldn't parse start state file"))
    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))
    print("Solving...")
    if(sys.argv[2] == "original"):
        route = solve(tuple(start_state)) 
    if(sys.argv[2] == "circular"):
    
        route = solve_c(tuple(start_state))
    elif(sys.argv[2] == "luddy"):
        route = solve_l(tuple(start_state))

    
    
    
    if route: 
        print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)
    else : 
        print("Inf")
