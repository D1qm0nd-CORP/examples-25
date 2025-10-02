def count_punctuation(text):
    punctuation_marks = ".,;:!?"  
    count = 0
    for char in text:  
        if char in punctuation_marks:  
            count += 1  
    return count

input_string = input()

punctuation_count = count_punctuation(input_string)

print(punctuation_count)
