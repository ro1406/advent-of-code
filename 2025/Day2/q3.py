ans=0
with open("input.txt",'r') as f:
    ranges = f.readlines()[0].strip().split(',')
    ranges = [r.split('-') for r in ranges]

    for s,e in ranges:
        for i in range(int(s),int(e)+1):
            num=str(i)
            if num[:len(num)//2]==num[len(num)//2:]:
                ans+=i
print('ANSWER:',ans)