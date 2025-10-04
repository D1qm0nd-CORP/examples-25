def find_longest_word_length(text):
    words = text.split()  
    max_length = 0
    for word in words:
        word_length = len(word)  
        if word_length > max_length:
            max_length = word_length  
    return max_length

input_string = input()

result = find_longest_word_length(input_string)
print(result)