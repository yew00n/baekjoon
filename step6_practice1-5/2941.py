croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = str(input())

for croatian_word in croatia:
    word = word.replace(croatian_word, '*')

print(len(word))
