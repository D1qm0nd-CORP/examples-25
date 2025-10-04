#TODO: FIX 3/4

import sys
def print_reverse_sequence():
    try:
        N_str = sys.stdin.readline().strip()
        
        if not N_str: 
            return

        N = int(N_str) 
        numbers_str = sys.stdin.readline().split()

        if len(numbers_str) != N:
            pass 

        def process_recursive(current_index):
            if current_index == N - 1:
                print(numbers_str[current_index], end=" ")
                return

            process_recursive(current_index + 1)
            print(numbers_str[current_index], end=" ")

        if N > 0:
            process_recursive(0)

    except EOFError:
        pass
    except ValueError:
        pass

print_reverse_sequence()