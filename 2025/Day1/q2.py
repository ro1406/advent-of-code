import math
curr_pos=50
ans=0

with open("input.txt",'r') as f:
    for line in f.readlines():
        dir, val = line.strip()[0], int(line.strip()[1:])
        if dir=='L':
            #If curr_pos-val crosses 0 then count how many times it crossed 0
            ans+= (curr_pos-1)//100 - (curr_pos-1-val)//100
            curr_pos = (curr_pos-val)%100
        else: 
            #If curr_pos+val crosses 100, then count how many times it crossed 100
            ans+= (curr_pos+val)//100
            curr_pos = (curr_pos+val)%100

print('ANSWER:',ans)



# import math
# curr_pos=50
# ans=0
# with open("input2.txt",'r') as f:
#     for line in f.readlines():
#         if not line: break
#         dir, val = line.strip()[0], int(line.strip()[1:])
#         if dir=='L':
#             if curr_pos - val <=0:
#                 print(curr_pos,f'L{val}', curr_pos-val)
#                 ans+=max(math.ceil(abs(curr_pos-val)/100.),1)
#             curr_pos = (curr_pos-val)%100
#         else: 
#             if curr_pos + val >=100:
#                 print(curr_pos,f'R{val}', curr_pos+val)
#                 ans+=(curr_pos+val)//100 - (curr_pos%100==0)
#             curr_pos = (curr_pos+val)%100


# print('ANSWER:',ans)