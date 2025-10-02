def find_synonym(synonym_pairs, word_to_find):
    synonym_dict = {}
    for pair in synonym_pairs:
        synonym_dict[pair[0]] = pair[1]
        synonym_dict[pair[1]] = pair[0]

    if word_to_find in synonym_dict:
        return synonym_dict[word_to_find]

n = int(input())  

synonym_input_list = []
for _ in range(n):
    pair = input().split()
    synonym_input_list.append(pair)

word_to_search = input()  

result = find_synonym(synonym_input_list, word_to_search)
print(result)

