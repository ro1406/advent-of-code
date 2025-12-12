from time import time
from heapq import heapify, heappop, heappush
ans=0

t0=time()
points=[]
with open("input.txt",'r') as f:
    for line in f.readlines():
        points.append(tuple(map(int,line.strip().split(','))))

h=[]
heapify(h)

for i in range(len(points)):
    for j in range(i+1,len(points)):
        #Find the dist and add to heap
        dist=((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2+(points[i][2]-points[j][2])**2)**0.5
        heappush(h,(dist,points[i],points[j]))


dic={} #node:[neighbors]

num_connections=0
while h and num_connections<1000:
    dist,p1,p2=heappop(h)
    # print(dist,p1,p2)
    if p2 in dic.get(p1,[]):
        #Already connected so nothing happens
        continue
    else:
        if p1 not in dic:
            dic[p1]=[]
        if p2 not in dic:
            dic[p2]=[]
        dic[p1].append(p2)
        dic[p2].append(p1)
        num_connections+=1
    

#dic is adjacency list
#Now DFS through this with visited set and find the connected components

visited=set()
list_of_components=[]

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    list_of_components[-1].add(node)
    for neighbor in dic[node]:
        dfs(neighbor)

for node in dic:
    if node not in visited:
        list_of_components.append(set())
        dfs(node)



#Pick the 3 longest sets in list_of_components
list_of_components.sort(key=lambda x:len(x),reverse=True)

print(len(list_of_components))
for x in list_of_components:
    print(x)
    print(len(x))
    print('-'*100)

ans=1
for i in range(3):
    ans*=len(list_of_components[i])

print("ANSWER:",ans)

print("Time taken:",time()-t0)
