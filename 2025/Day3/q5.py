ans=0

with open("input.txt",'r') as f:
    for line in f.readlines():
        line = line.strip()
        maxx=-1
        for i in range(len(line)):
            for j in range(i+1,len(line)):
                maxx=max(maxx,int(line[i]+line[j]))
        ans+=maxx

print("ANSWER:",ans)