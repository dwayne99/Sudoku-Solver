import sys

def canInsert(n,x,y):
    for i in range(9):
        if matrix[x][i] == n:
            return False
    for i in range(9):
        if matrix[i][y] == n:
            return False
    return True


def solve():
    global matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for k in range(1,10):
                    if canInsert(k,i,j):
                        matrix[i][j] = k
                        solve()
                        matrix[i][j] = 0
                return 

    print(f"{'*'*20}")
    for i in range(len(matrix)):
        print(matrix[i])
    input('Press any key to exit...')
    # sys.exit()



matrix = [
        [0,0,0,0,0,0,6,8,0],    
        [0,0,0,0,7,3,0,0,9],    
        [3,0,9,0,0,0,0,4,5],    
        [4,9,0,0,0,0,0,0,0],    
        [8,0,3,0,5,0,9,0,2],    
        [0,0,0,0,0,0,0,3,6],    
        [9,6,0,0,0,0,3,0,8],    
        [7,0,0,6,8,0,0,0,0],    
        [0,2,8,0,0,0,0,0,0],    
        ]



solve() 
