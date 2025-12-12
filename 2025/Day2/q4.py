from time import time

def get_divisors(n):
    ans=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            ans.append(i)
            if i!=1:
                ans.append(n//i)
    return list(set(ans))

divisors_by_len = {n:get_divisors(n) for n in range(1,11)}
#One has no divisors that arent 1
divisors_by_len[1]=[]

ans=[]
start_time = time()
with open("input.txt",'r') as f:
    ranges = [r.split('-') for r in f.readlines()[0].strip().split(',')]

    for s,e in ranges:
        t0=time()
        for n in range(int(s),int(e)+1):
            num=str(n)
            divisors = divisors_by_len[len(num)]
            for i in divisors:
                #It can be i things repeated len(num)//i times
                if num == num[:i]*(len(num)//i):
                    ans.append(n)
                    break
print('ANSWER:',sum(set(ans)))
print("Time taken:",time()-start_time)
