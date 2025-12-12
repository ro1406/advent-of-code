from time import time
import numpy as np

# Actual fast solution thats accepted:
# - Check if the total number of # in all the presents is greater than the grid space then it is impossible to fit
# - If its less than or equal to grid space then its possible.

# Thats it!!


# I still implemented the full backtracking solution for fun
# (and because the above doesnt work for all cases and it doesnt work in the examples either)

RUN_BACKTRACKING = False
VERBOSE = False


t0 = time()

ans = 0
presents = {}
queries = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 5):
        # Reading presents
        no = int(lines[i].split(":")[0])
        present = []
        for j in range(1, 4):
            present.append(list(lines[i + j].strip()))
        presents[no] = present
        if len(presents) >= 6:
            break

    # Now lets read the grids
    for i in range(30, len(lines)):
        # Reading grids
        if not lines[i].strip():
            break
        size, indices = lines[i].strip().split(":")
        r, c = map(int, size.split("x"))
        indices = list(map(int, indices.split()))
        queries.append((r, c, indices))

if VERBOSE:
    for x in presents:
        print(x)
        for y in presents[x]:
            print(y)
        print("-" * 100)

for idx, (r, c, indices) in enumerate(queries):
    if VERBOSE:
        print(f"Query {idx+1}: {r}x{c} with indices {indices}")
    # Quick check, if there are more total number of # in present than grid space then it is impossible to fit
    total_hashes = 0
    for i in range(len(indices)):
        if indices[i] > 0:
            present = presents[i]
            total_hashes += sum([x.count("#") for x in present]) * indices[i]
    if VERBOSE:
        print(f"Total hashes: {total_hashes}")
    if total_hashes > r * c:
        if VERBOSE:
            print(f"Query {idx+1} is impossible to fit")
    else:
        if VERBOSE:
            print(f"Query {idx+1} is possible to fit. hashes: {total_hashes}, space: {r*c}")
        ans += 1

end_time = time()
print(f"Answer: {ans}")
print(f"Time taken: {end_time-t0} seconds")


# BACKTRACKING SOLUTION:
if RUN_BACKTRACKING:
    t0 = time()
    import numpy as np

    def rot90(matrix):
        # Anti clockwise rotation
        return np.rot90(matrix)

    def rot180(matrix):
        return np.rot90(matrix, 2)

    def rot270(matrix):
        return np.rot90(matrix, 3)

    def flip_horizontal(matrix):
        return np.flipud(matrix)

    def flip_vertical(matrix):
        return np.fliplr(matrix)

    combos = {}
    for k, v in presents.items():
        coms = []
        coms.append(v)
        coms.append(rot90(v))
        coms.append(rot180(v))
        coms.append(rot270(v))
        coms.append(flip_horizontal(v))
        coms.append(flip_vertical(v))
        # Remove duplicates
        # Stack into a single 2D array
        stacked_array = np.stack(coms)
        # Use np.unique along axis 0 to find unique rows (arrays)
        unique_arrays_sorted = np.unique(stacked_array, axis=0)
        combos[k] = unique_arrays_sorted.tolist()

    # print("COMBOS:")
    # for k in combos:
    #     print(k)
    #     for y in combos[k]:
    #         for x in y:
    #             print(x)
    #         print('-'*100)
    #     print('='*100)

    # Try all rotations and flips of the present and see if it fits in the grid

    def can_fit(mask, grid, i, j):
        if i + len(mask) > len(grid) or j + len(mask[0]) > len(grid[0]):
            return False
        for x in range(len(mask)):
            for y in range(len(mask[0])):
                if mask[x][y] == "#" and grid[i + x][j + y] == "#":
                    # Collision detected
                    return False
        return True

    def place_piece(mask, grid, i, j):
        for x in range(len(mask)):
            for y in range(len(mask[0])):
                if mask[x][y] == "#":
                    grid[i + x][j + y] = "#"
        return grid

    def remove_piece(mask, grid, i, j):
        for x in range(len(mask)):
            for y in range(len(mask[0])):
                if mask[x][y] == "#":
                    grid[i + x][j + y] = "."
        return grid

    def print_grid(grid):
        for x in grid:
            print("".join(x))
        print("-" * 100)

    for idx, (r, c, indices) in enumerate(queries):
        # Pieces is a list of all the pieces that need to be placed in the grid
        pieces = []
        for i in range(len(indices)):
            if indices[i] > 0:
                pieces += [i] * indices[i]

        grid = [["." for _ in range(c)] for _ in range(r)]

        def backtrack(piece_idx, grid):
            if piece_idx == len(pieces):
                return True

            # If there are fewer . in grid than there are # in all the remaining pieces then it is impossible to fit
            remaining_hashes = 0
            for i in range(piece_idx, len(pieces)):
                present = presents[pieces[i]]
                remaining_hashes += sum([x.count("#") for x in present])

            if remaining_hashes > sum([x.count(".") for x in grid]):
                # print(f"Remaining hashes: {remaining_hashes} is greater than . in grid: {sum([x.count('.') for x in grid])}")
                # print(f"Query {idx+1} is impossible to fit")
                return False

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    for combo in combos[pieces[piece_idx]]:
                        if can_fit(combo, grid, i, j):
                            grid = place_piece(combo, grid, i, j)
                            if backtrack(piece_idx + 1, grid):
                                return True
                            grid = remove_piece(combo, grid, i, j)
            return False

        result = backtrack(0, grid)
        if result:
            print(f"Query {idx+1} is possible to fit")
            ans += 1
        else:
            print(f"Query {idx+1} is impossible to fit")

    end_time = time()
    print(f"Answer [Backtracking]: {ans}")
    print(f"Time taken for backtracking: {end_time-t0} seconds")
