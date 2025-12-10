from time import time

t0 = time()
arr = []
total = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        arr = line.strip().split()
        lights, *switches, joltages = arr
        switches = list(map(eval, switches))
        for i in range(len(switches)):
            if isinstance(switches[i], int):
                switches[i] = tuple([switches[i]])

        # switches.sort(key=lambda x: len(x), reverse=True)
        switches.sort(key=lambda x: min(joltages[i] for i in x), reverse=False)

        lights = lights.strip("[]")
        joltages = list(map(int, joltages.strip("{}").split(",")))
        print("Lights:", lights)
        print("Switches:", switches)
        print("Joltages:", joltages)

        # Precompute the max number of times you can use a switch
        max_times_used = [0] * len(switches)
        for idx, s in enumerate(switches):
            minn = float("inf")
            for i in s:
                minn = min(minn, joltages[i])
            max_times_used[idx] = minn

        for s, m in zip(switches, max_times_used):
            print(s, m)

        num_times_left_to_use = max_times_used.copy()

        ans = float("inf")

        def recur(idx, steps=0, curr_res=[]):
            # print('\t'*idx,f'idx: {idx}, steps: {steps}, curr_res: {curr_res}')
            # curr_res = [0,0,0,0,0,0]
            global ans
            # Check if curr_res is equal to joltages
            if curr_res == joltages:
                ans = min(ans, steps)
                return

            # Too far, just return
            if idx >= len(switches):
                return

            if num_times_left_to_use[idx] <= 0:
                return

            # If youve taken more steps than the current answer, just return
            if steps > ans:
                return

            # Check if any of the curr_res has overshot joltages
            if any(curr_res[i] > joltages[i] for i in range(len(curr_res))):
                # Too high, just return
                return

            # Case 1: Flip switch, move
            s = switches[idx]

            for i in s:
                curr_res[i] += 1
            num_times_left_to_use[idx] -= 1
            recur(idx + 1, steps + 1, curr_res)
            for i in s:
                curr_res[i] -= 1
            num_times_left_to_use[idx] += 1

            # Case 2: Flip switch, but dont move
            for i in s:
                curr_res[i] += 1
            num_times_left_to_use[idx] -= 1
            recur(idx, steps + 1, curr_res)
            for i in s:
                curr_res[i] -= 1
            num_times_left_to_use[idx] += 1

            # Case 3: Dont flip switch, just move
            recur(idx + 1, steps, curr_res)

        recur(0, 0, curr_res=[0 for _ in range(len(joltages))])
        total += ans
        print(ans)

        print("-" * 100)

end_time = time()
print("Answer:", total)
print("Time taken including file reading:", end_time - t0)
