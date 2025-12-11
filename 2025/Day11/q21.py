from time import time


t0 = time()
dic = {}
ans = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        k, v = line.strip().split(":")
        dic[k] = [x.strip() for x in v.split()]


# for k in dic:
#     print(k,dic[k])

# Dfs from key=you to key=out
res = []


def dfs(key, path):
    if key == "out":
        res.append(path[:])
        return
    for k in dic[key]:
        dfs(k, path + [k])


path = dfs("you", [])
# print(path)
# print("dfs done")
# print(res)
print(len(res))

end_time = time()
print("Time taken:", end_time - t0)
print("Answer:", ans)
