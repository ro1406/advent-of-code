ans=0

grid=[]
with open("input.txt",'r') as f:
    for line in f.readlines():
        grid.append(line.strip())

S_col=grid[0].index('S')

cols_to_check= set([S_col])

for row in range(1,len(grid)):
    temp_cols_to_Check=set()
    for col in cols_to_check:
        if '^' == grid[row][col]:
            #Youve split a beam
            ans+=1
            temp_cols_to_Check.add(col-1)
            temp_cols_to_Check.add(col+1)
        else:
            temp_cols_to_Check.add(col)

    cols_to_check=temp_cols_to_Check


print("ANSWER:",ans)