FILE_IN = 'number_to_call'
FILE_OUT = 'number_to_call_'
POOL = [15, 13, 11, 9, 7, 5]

with open(FILE_IN, 'r') as f:
    numbers_pool = f.readlines()
    all_numbers_len = len(numbers_pool)
    one_part = all_numbers_len // len(POOL)

counter = 0

for i in POOL:

    if counter == len(POOL) - 1:
        with open(FILE_IN, 'r') as f:
            numbers_pool = f.readlines()
            with open('{}{}'.format(FILE_OUT, i), 'w') as ff:
                ff.writelines(numbers_pool)
        with open(FILE_IN, 'w') as f:
            pass

    else:
        with open(FILE_IN, 'r') as f:
            numbers_pool = f.readlines()
            with open('{}{}'.format(FILE_OUT, i), 'w') as ff:
                for x in range(one_part):
                    ff.write(numbers_pool.pop())
        with open(FILE_IN, 'w') as f:
            f.writelines(numbers_pool)
        counter += 1

    print(counter)
    print(len(POOL))
