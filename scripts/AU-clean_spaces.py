def clean_spaces(input_string):
    cleaned_string = input_string.strip()
    words = cleaned_string.split()
    return ' '.join(words)

input_str = input()
output_str = clean_spaces(input_str)
print(output_str)