# TODO: FIX 1/4

def inputPair():
    inp = input()
    sp = inp.split(' ')
    return int(sp[0]), int(sp[1])


def solve(x, y):
    if x > 0 and x < M + 1 and y > 0 and y < N + 1:
        return True
    return False


def get_neighbors(M, N, x, y):
    def get_up_neighbor(x, y):
        return (x, y - 1)
    def get_down_neighbor(x, y):
        return (x, y + 1)
    def get_left_neighbor(x, y):
        return (x - 1, y)
    def get_right_neighbor(x, y):
        return (x + 1, y)

    def exclude(neighbors, M, N):
        def neighbor_exist(neighbor, M, N):
            def check_left_and_up_line(x):
                if x >= 0:
                    return True
                return False
            def check_right_and_down_line(x, m):
                if x <= m:
                    return True
                return False
            return check_right_and_down_line(x, M) and check_right_and_down_line(y, N) or check_left_and_up_line(
                x) and check_left_and_up_line(y)

        for neighbor in neighbors:
            if neighbor_exist(neighbor, M, N):
                yield neighbor

    neighbors = exclude(
        [get_up_neighbor(x, y),
         get_left_neighbor(x, y),
         get_down_neighbor(x, y),
         get_right_neighbor(x, y)]
         , M, N)
    return neighbors


def print_neighbors(neighbors):
    for neighbor in neighbors:
        print(f"{neighbor[0]} {neighbor[1]}")


M, N = inputPair()
x, y = inputPair()

print_neighbors(get_neighbors(M, N, x, y))
