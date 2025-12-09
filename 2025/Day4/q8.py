ans=0

def remove_rolls(grid):
    temp_ans=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "@":
                #Check the 8 adjacent positions and count number of @s
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if not(x==i and y==j) and 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == "@":
                            count += 1
                if count<4:
                    grid[i][j] = "."
                    temp_ans+=1
    return grid, temp_ans

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]

    num_removed = -1
    while num_removed != 0:
        grid, num_removed = remove_rolls(grid)
        ans += num_removed

print('ANSWER:',ans)