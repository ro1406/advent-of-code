from time import time
from collections import deque
from functools import lru_cache


t0 = time()
dic = {}
ans = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        k, v = line.strip().split(":")
        dic[k] = [x.strip() for x in v.split()]

if "out" not in dic:
    dic["out"] = []


def is_reachable(start, goal):
    """Check if goal is reachable from start using BFS"""
    if start == goal:
        return True
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        if node in dic:
            for neighbor in dic[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return False


# Use dynamic programming to find number of paths from start to goal
@lru_cache(maxsize=None)
def find_paths(curr_node, goal):
    if curr_node == goal:
        return 1
    if curr_node not in dic:
        return 0
    return sum(find_paths(neighbor, goal) for neighbor in dic[curr_node])


print('is_reachable("svr", "dac"):', is_reachable("svr", "dac"))
print('is_reachable("dac", "fft"):', is_reachable("dac", "fft"))
print('is_reachable("fft", "out"):', is_reachable("fft", "out"))

print('is_reachable("svr", "fft"):', is_reachable("svr", "fft"))
print('is_reachable("fft", "dac"):', is_reachable("fft", "dac"))
print('is_reachable("dac", "out"):', is_reachable("dac", "out"))
print("-" * 100)

# Idea: find paths from svr-dac then dac-fft then fft-out and multiply the number of paths
#      repeat for svr-fft-dac-out and add the number of paths found in each case

# Issue: dac-fft is not reachable - verified by BFS. So only need to consider svr-fft-dac-out

print("Finding paths from svr to fft:")
svr_fft_paths = find_paths("svr", "fft")
print("Number of paths from svr to fft:", svr_fft_paths)
print("Finding paths from fft to dac:")
fft_dac_paths = find_paths("fft", "dac")
print("Number of paths from fft to dac:", fft_dac_paths)
print("Finding paths from dac to out:")
dac_out_paths = find_paths("dac", "out")
print("Number of paths from dac to out:", dac_out_paths)

ans = svr_fft_paths * fft_dac_paths * dac_out_paths

end_time = time()
print("Time taken:", end_time - t0)
print("Answer:", ans)
