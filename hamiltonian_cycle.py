def is_valid_move(grid, h, w, path, r, c):
    if (r, c) in path:
        return False

    if len(path) == w * h - 1:
        for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            if 0 <= r + dr < h and 0 <= c + dc < w and (r + dr, c + dc) == path[0]:
                return True
        return False

    return 0 <= r < h and 0 <= c < w

def hamiltonian_cycle(grid, w, h):
    # nested recurtion, don't juge the redability, it's more optimal this way
    def backtrack(path):
        if len(path) == w * h:
            return path

        r, c = path[-1]
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if is_valid_move(grid, w, h, path, new_r, new_c):
                ret = backtrack(path + [(new_r, new_c)])
                if ret:
                    return ret
        return None

    for i in range(h):
        for j in range(w):
            ret = backtrack([(i, j)])
            if ret:
                return ret

    return None

def generate_hamiltonian_cycle(width, height):   
    grid = [[0 for _ in range(width)] for _ in range(height)]
    cycle = hamiltonian_cycle(grid, height, width)
    if cycle:
        i = 0
        for point in cycle:
            grid[point[0]][point[1]] = i
            i += 1
    else:
        print("Couldn't find a path (try even grid area)")
    return grid