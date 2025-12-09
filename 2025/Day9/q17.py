from time import time

ans = 0
t0 = time()
arr=[]
with open("input.txt", "r") as f:
    for line in f.readlines():
        arr.append(list(map(int, line.strip().split(","))))

# Sort arr by lowest x coord, highest y coord
# arr.sort(key=lambda x: (x[0],-x[1]))

# for x in arr:
#     ans=max(ans,(abs(arr[0][0]- x[0])+1)*(abs(arr[0][1]- x[1])+1))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        ans=max(ans,(abs(arr[i][0]- arr[j][0])+1)*(abs(arr[i][1]- arr[j][1])+1))

end_time = time()
print("Answer:", ans)
print("Time taken:", end_time - t0)
