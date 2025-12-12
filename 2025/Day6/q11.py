from time import time
ans=0

grid=[]
t0=time()
with open("input.txt",'r') as f:
    for line in f.readlines():
        t=line.strip().split()
        grid.append([int(x) if x and '+' not in x and '*' not in x else x.strip() for x in t ])

after_loading= time()
for col in range(len(grid[0])):
    op=grid[-1][col]
    if op=='+':
        res=0
    else:
        res=1
    
    for row in range(len(grid)-1):
        if op=='+':
            res+=grid[row][col]
        else:
            res*=grid[row][col]
    ans+=res

end_time = time()
print("ANSWER:",ans)
print("Time taken after loading:",end_time-after_loading)
print("Total time including loading:",end_time-t0)