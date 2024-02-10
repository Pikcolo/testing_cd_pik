def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if ord(grid[i][j]) > ord(grid[i+1][j]):
                return "NO"
                
    return "YES"