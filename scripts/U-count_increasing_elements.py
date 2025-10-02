def count_increasing_elements():
    count = 0
    previous_num = int(input()) 

    while True:
        current_num = int(input())
        if current_num == 0: 
            break
        if current_num > previous_num: 
            count += 1
        previous_num = current_num 
    print(count) 
    
count_increasing_elements() 