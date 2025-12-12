from collections import Counter
ans=0

def method1(arr):
    dic={}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]].append(i)
        else:
            dic[arr[i]]=[i]
    
    temp=[0 for _  in range(len(arr))]
    num_filled=0
    for k,v in sorted(dic.items(),key=lambda x:x[0], reverse=True):
        if num_filled==12:
            break
        for i in reversed(v):
            temp[i]=k
            num_filled+=1
            if num_filled==12:
                break
    
    return int(''.join(map(str,[x for x in temp if x!=0])))

def method2(arr):
    num_to_skip = len(arr)-12
    # print(num_to_skip)
    temp=''
    num_skipped=0
    for i in range(len(arr)):
        if num_skipped<num_to_skip:
            if i!=len(arr)-1 and arr[i]<arr[i+1]:
                num_skipped+=1
                continue
            else:
                temp+=str(arr[i])
                if len(temp)==12:
                    return int(temp)
        else:
            temp+=str(arr[i])
            if len(temp)==12:
                return int(temp)
    print("Didnt reach 12 anywhere")
    return int(temp)

def method3(arr):
    #If the number of digits on the right of this element >= it is >=12 then dont select this element
    num_elements_bigger_than_i = []
    for i in range(len(arr)):
        num_elements_bigger_than_i.append(len([x for x in arr[i+1:] if x>=arr[i]]))
    print(num_elements_bigger_than_i)
    temp=''
    for i in range(len(arr)):
        if num_elements_bigger_than_i[i]>=12-len(temp):
            continue
        else:
            temp+=str(arr[i])
            if len(temp)==12:
                return int(temp)
    print("Didnt reach 12 anywhere")
    return int(temp)

def method4(arr):
    #Pick the highest digit in arr[i+1 : len(arr)-1-digits_remaining_to_pick] and then set i to be the index of highest digit+1
    res=''
    def recur(a,num_to_pick):
        nonlocal res
        if num_to_pick==1:
            res+=str(max(a))
            return
        segment = a[:len(a)-num_to_pick+1]
        maxx=max(segment)
        maxx_index = segment.index(maxx)
        res+=str(maxx)
        recur(a[maxx_index+1:],num_to_pick-1)

    recur(arr,12)
    return int(res)



with open("input.txt",'r') as f:
    for line in f.readlines():
        if not line.strip(): break
        arr = list(map(int,line.strip()))
        
        # m1_ans = method1(arr)
        # m2_ans = method2(arr)
        # print(arr)
        m4_ans = method4(arr)
        print(m4_ans)
        ans+=m4_ans
        # print('-'*100)

        # ans+= max(m1_ans,m2_ans)
        

print("ANSWER:",ans)