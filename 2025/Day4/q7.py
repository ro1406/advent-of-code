ans=0

with open("input.txt", "r") as f:
    grid = [x.strip() for x in f.readlines()]

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "@":
                #Check the 8 adjacent positions and count number of @s
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == "@" and not(x==i and y==j):
                            count += 1
                if count<4:
                    ans += 1

print('ANSWER:',ans)