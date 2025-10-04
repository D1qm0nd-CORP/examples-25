def find_closest_element(arr, x):
    if not arr:
        return None  
    
    closest_element = arr[0]
    min_diff = abs(arr[0] - x)

    for element in arr:
        diff = abs(element - x)
        if diff < min_diff:
            min_diff = diff
            closest_element = element
    return closest_element

N = int(input())
array = list(map(int, input().split()))
x = int(input())

result = find_closest_element(array, x)
print(result)