from time import time

t0 = time()
arr = []
total = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        arr=line.strip().split()
        lights, *switches, joltages = arr
        switches = list(map(eval, switches))
        lights = lights.strip('[]')
        joltages = eval(joltages)
        print("Lights:", lights)
        print("Switches:", switches)
        print("Joltages:", joltages)

        
        ans=float('inf')
        def recur(idx, steps=0, curr_res=[]):
            #curr_res = [....]
            global ans
            if idx == len(switches):
                if ''.join(curr_res)==lights:
                    ans=min(ans, steps)
                return
            #Flip switch
            s = switches[idx]
            if isinstance(s, int):
                s = tuple([s])
            for i in s:
                curr_res[i] = '#' if curr_res[i]=='.' else '.'
            
            recur(idx+1, steps+1, curr_res)

            #Flip them back
            for i in s:
                curr_res[i] = '#' if curr_res[i]=='.' else '.'
            #Don't flip switch
            recur(idx+1, steps, curr_res)

        recur(0, 0, curr_res=['.' for _ in range(len(lights))])
        total+=ans
        print(ans)

        print('-'*100)

end_time = time()
print("Answer:", total)
print("Time taken including file reading:", end_time - t0)
