list1_str = input().split()
list1 = list(map(int, list1_str))

list2_str = input().split()
list2 = list(map(int, list2_str))

common_count = len(set(list1) & set(list2))

print(common_count)
