curr_pos=50
ans=0
with open("input.txt",'r') as f:
    for line in f.readlines():
        dir, val = line.strip()[0], int(line.strip()[1:])
        if dir=='L':
            curr_pos = (curr_pos-val)%100
        else: 
            curr_pos = (curr_pos+val)%100
        if curr_pos==0:
            ans+=1
print('ANSWER:',ans)