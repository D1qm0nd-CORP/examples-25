def compress_list(nums):
    writer_index = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[writer_index] = nums[i]
            writer_index += 1

    for i in range(writer_index, len(nums)):
        nums[i] = 0

    return nums

input_line = input()
numbers_str = input_line.split()
numbers = [int(num) for num in numbers_str]

compressed_numbers = compress_list(numbers)

print(*compressed_numbers)
