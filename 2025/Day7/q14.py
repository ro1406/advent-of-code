from functools import lru_cache
from time import time
ans=0

t0=time()
grid=[]
with open("input.txt",'r') as f:
    for line in f.readlines():
        grid.append(line.strip())

S_col=grid[0].index('S')

@lru_cache(maxsize=None)
def recur(row,col):
    
    #DFS through the tree, everytime you reach a leaf, add 1 to ans
    #A leaf is a node with no children in any row below
    if all(grid[r][col-1]!='^' and grid[r][col+1]!='^' for r in range(row+2,len(grid))):
        #Is a leaf
        return 2
    
    total=0
    #Check for left child
    if grid[row+2][col-1]=='^':
        total+= recur(row+2,col-1)
    else:
        #No direct child, but need to check if any other splitter comes in this col
        found=False
        for r in range(row+2,len(grid)):
            if grid[r][col-1]=='^':
                found=True
                total+= recur(r,col-1)
                break
        if not found:
            #No splitter found, so just add 1 since that beam is the end
            #If splitter was found then its taken care of in the recur() call
            total+= 1

    #Check for right child
    if grid[row+2][col+1]=='^':
        total+= recur(row+2,col+1)
    else:
        #No direct child, but need to check if any other splitter comes in this col
        found=False
        for r in range(row+2,len(grid)):
            if grid[r][col+1]=='^':
                found=True
                total+= recur(r,col+1)
                break
                
        if not found:
            #No splitter found, so just add 1 since that beam is the end
            #If splitter was found then its taken care of in the recur() call
            total+= 1
    return total
    
before_recur=time()
ans=recur(2,S_col)
end=time()
print("ANSWER:",ans)
print("Time taken including loading data:",end-t0)
print("Time taken only for processing:",end-before_recur)