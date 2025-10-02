count = 0  
prev_num = int(input())  
current_num = int(input())  

while current_num != 0:
    next_num = int(input())  
    if next_num != 0 and current_num > prev_num and current_num > next_num:
        count += 1  

    prev_num = current_num
    current_num = next_num

print(count)