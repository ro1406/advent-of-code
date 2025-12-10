from time import time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def solve_min_sum_integer(A, b):
    """
    Solves Ax = b for integers x >= 0 such that sum(x) is minimized.
    """
    m, n = A.shape

    # Minimize sum(x) -> c = [1, 1, ..., 1]
    c = np.ones(n)

    # Define Constraints: Ax = b
    # We use LinearConstraint with lower_bound = upper_bound = b
    constraints = LinearConstraint(A, b, b)

    # Define Integrality: 1 indicates the variable must be an integer
    integrality = np.ones(n)

    # Define Bounds: x >= 0 (0 to infinity)
    bounds = Bounds(lb=0, ub=np.inf)

    # Solve using Mixed Integer Linear Programming
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    if res.success:
        # Round to nearest integer to avoid floating point artifacts (e.g. 3.00000001)
        return np.round(res.x).astype(int)
    else:
        return None


t0 = time()
arr = []
total = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        arr = line.strip().split()
        lights, *switches, joltages = arr
        switches = list(map(eval, switches))
        # Some switches got eval to int, just make them tuples
        for i in range(len(switches)):
            if isinstance(switches[i], int):
                switches[i] = tuple([switches[i]])

        lights = lights.strip("[]")
        joltages = list(map(int, joltages.strip("{}").split(",")))

        print("Lights:", lights)
        print("Switches:", switches)
        print("Joltages:", joltages)

        # Create A & b s.t Ax=b can be solved. x will be the number of times each switch is pressed
        # Ans will be sum(x)
        # A is the coef matrix based on the switches
        # b is the joltages vector
        # Use integer linear programming to solve for the minimum sum of x
        # min sum(x) s.t Ax=b and x>=0 and x is an integer
        A = []
        b = joltages.copy()
        for i in range(len(joltages)):
            A.append([1 if i in switches[j] else 0 for j in range(len(switches))])

        A = np.array(A)
        b = np.array(b)

        x_particular = solve_min_sum_integer(A, b)

        ans = sum(x_particular)
        total += ans
        print("ans:", ans)
        print("-" * 100)


end_time = time()
print("Answer:", total)
print("Time taken including file reading:", end_time - t0)
