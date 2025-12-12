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



#Adding list_of_components and visited lists as params, returning list of components
#since we need to return the list of components
#and these values need to be reset every invocation so global vars dont work
def dfs(node, list_of_components,visited):
    if node in visited:
        return list_of_components
    visited.add(node)
    list_of_components[-1].add(node)
    for neighbor in dic[node]:
        dfs(neighbor, list_of_components,visited)
    return list_of_components


dic={} #node:[neighbors]

while True:
    dist,p1,p2=heappop(h)
    # print(dist,p1,p2)
    if p2 in dic.get(p1,[]):
        #Already connected so nothing happens
        continue

    if p1 not in dic:
        dic[p1]=[]
    if p2 not in dic:
        dic[p2]=[]
    dic[p1].append(p2)
    dic[p2].append(p1)

    list_of_components = dfs(p1,[set()],set())
    if len(list_of_components[0])==len(points):
        #One big component found
        #Take the latest p1 and p2 and multiply
        print(p1,p2)
        ans=p1[0]*p2[0]
        break
    

print("ANSWER:",ans)

print("Time taken:",time()-t0)
