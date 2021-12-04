import random
import datetime

with open('names.txt', encoding='utf-8') as f_in:
    names = f_in.read().splitlines()

random.shuffle(names)

with open('pairs.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('Пары составлены: {}\n\n'.format(datetime.datetime.now()))
    line = ''
    for i in range(len(names)):
        next_idx = 0 if i == len(names) - 1 else i + 1
        line = '{} -> {}\n'.format(names[i], names[next_idx])
        f_out.write(line)
