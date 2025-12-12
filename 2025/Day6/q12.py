from time import time
ans=0

grid=[]
t0=time()
with open("input.txt",'r') as f:
    for line in f.readlines():
        grid.append(line.strip('\n')+' ')

# for x in grid:
#     print(x)
# print('-'*100)
after_loading= time()
res=-1
for col in range(len(grid[0])):

    #Find the op
    if grid[-1][col] in ['+','*']:
        op = grid[-1][col]
    
    #Reset res only if new op (res is empty)
    if op=='+' and res==-1:
        res=0
    elif op=='*' and res==-1:
        res=1
    
    num=''
    for row in range(len(grid)-1):
        if grid[row][col]==' ': continue
        num+= str(grid[row][col])
        
    #Now we have the number to add to res
    if num:
        if op=='+':
            res+=int(num)
        else:
            res*=int(num)
    

    #If this col is all spaces then num was empty, so the problem is over
    if not num:
        #This sum is over, add res to ans
        ans+=res
        res=-1
        
end_time = time()
print("ANSWER:",ans)
print("Time after loading:",end_time-after_loading)
print("Total time including loading:",end_time-t0)