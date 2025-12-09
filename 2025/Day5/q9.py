ans = 0
ranges=[]
with open("input.txt", "r") as f:
    reading_ranges = True
    for line in f.readlines():
        if line == "\n":
            reading_ranges = False
            continue
        if reading_ranges:
            s,e = map(int,line.strip().split('-'))
            ranges.append((s,e))
        else:
            num=int(line.strip())
            for s,e in ranges:
                if s<=num<=e:
                    ans+=1
                    break


print("ANSWER:", ans)
