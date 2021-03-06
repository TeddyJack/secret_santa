from random import shuffle

with open('names.txt', encoding='utf-8') as f_in:
    names = f_in.read().splitlines()
    shuffle(names)

with open('pairs.txt', 'w', encoding='utf-8') as f_out:
    for i in range(-1, len(names) - 1):
        f_out.write(f'{names[i]} -> {names[i+1]}\n')
