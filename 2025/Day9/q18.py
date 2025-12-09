from time import time
from tqdm import tqdm
import matplotlib.pyplot as plt

ans = 0
arr = []
t0 = time()
with open("input.txt", "r") as f:
    for line in f.readlines():
        arr.append(list(map(int, line.strip().split(","))))
start_time = time()

border = set()
for i in tqdm(range(len(arr))):
    p1 = arr[i]
    p2 = arr[(i + 1) % len(arr)]
    for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            border.add((x, y))


for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        p1 = arr[i]
        p2 = arr[j]

        # Check if area is bigger than the current ans - no need to check if its smaller than the current ans
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        if area < ans:
            continue

        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        # Check if any point on the perimeter of the polygon is inside the rectangle
        valid = True
        for x, y in border:
            if x_min < x < x_max and y_min < y < y_max:
                valid = False
                break

        if valid:
            # Area is more than ans and the rect is valid
            ans = area

print("Answer:", ans)
print("Time taken:", time() - start_time)
