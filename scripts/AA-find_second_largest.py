def find_second_largest():
    max1 = -1
    max2 = -1

    while True:
        num = int(input())
        if num == 0:
            break

        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    if max2 != -1:
        print(max2)
    else:
        print("В последовательности не хватает двух элементов для определения второго по величине.")


find_second_largest()
