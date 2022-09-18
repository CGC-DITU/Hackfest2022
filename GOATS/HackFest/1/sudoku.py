import random
level = 30 
def sudoku(diff=level):

    numbers = [i for i in range(1,10)]
    
    grid = [[0 for x in range(9)] for y in range(9)]
    
    for i in range(81-diff):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.choice(numbers)
        while not scan(grid, row, col, num) or grid[row][col] != 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.choice(numbers)
        grid[row][col] = num
            


    return grid

def printGrid(grid):
    print("+-------+-------+-------+")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            print(grid[i][j], end=" ")
            if j % 3 == 2:
                print("|", end=" ")
        print()
        if i % 3 == 2:
            print("+-------+-------+-------+")

def scan(grid,row,col,num):
    for i in range(9):
        valid = True
        for i in range(9):
            if grid[row][i] == num:
                valid = False
                break
            if grid[i][col] == num:
                valid = False
                break
        x ,y= row // 3, col // 3
        
        for i in range(3):
            for j in range(3):
                if grid[x * 3 + i][y * 3 + j] == num:
                    valid = False
                    break
    return valid
    

def play():
    Game = True
    grid = sudoku()
    printGrid(grid)
    while Game:
        x=int(input("Enter the row: "))
        y=int(input("Enter the column:"))
        num=int(input("Enter the number: "))
        if scan(grid , x, y, num) and grid[x][y] == 0:
            grid[x][y] = num
        else:
            print("Invalid move")
        if num==0:
            print("Game Over")
            break
        printGrid(grid)
        
play()
        
        