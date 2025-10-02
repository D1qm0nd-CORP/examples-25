# TODO: FIX 4 / 10
def max_monotonic_length():
    max_len = 0
    current_len = 0
    prev_num = None
    is_increasing = None

    while True:
        num = int(input())
        if num == 0:
            break

        if prev_num is None:
            current_len = 1
        else:
            if num > prev_num:
                if is_increasing is None or is_increasing:
                    current_len += 1
                    is_increasing = True
                else:
                    current_len = 2
                    is_increasing = True
            elif num < prev_num:
                if is_increasing is None or not is_increasing:
                    current_len += 1
                    is_increasing = False
                else:
                    current_len = 2
                    is_increasing = False
            else:
                current_len = 2
                is_increasing = None
                if prev_num is not None:
                    pass

        max_len = max(max_len, current_len)
        prev_num = num

    return max_len - 1

print(max_monotonic_length())
