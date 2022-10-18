'''
Task here: /src/tricky_cipher/*.png
'''

import sys


def tricky_cipher(data):
    input_data_list = []
    '''
    block for stdin
    '''
    # input_data_list.append(sys.stdin.readline().strip())
    # while True:
    #     input_data_list.append(sys.stdin.readline().strip())
    #     if len(input_data_list) == input_data_list[0]:
    #         break
    input_data_list.append(data[0])
    i = 1
    while len(input_data_list) < int(input_data_list[0])+1:
        input_data_list.append(data[i])
        i += 1

    # input_data_list.append(data[1])
    # input_data_list.append(data[2])
    result = ['']*int(input_data_list[0])
    for (index,person) in enumerate(input_data_list[1:]):
        person_list = person.split(',')
        len_set_of_fio = len(set(person_list[0] + person_list[1] + person_list[2]))
        list_of_d = [int(y) for i in person_list[3:4] for y in i]
        list_of_m = [int(y) for i in person_list[4:5] for y in i]
        sum_of_dm_64 = (sum(list_of_d) + sum(list_of_m))*64
        lower_char = ord(person_list[0][0].lower())
        first_char_of_f_256 = (lower_char - 96) * 256
        summ_of_fio_dm_fchar = len_set_of_fio + sum_of_dm_64 + first_char_of_f_256
        summ_of_fio_dm_fchar_hex = hex(summ_of_fio_dm_fchar).split('x')[-1]
        result[index] = summ_of_fio_dm_fchar_hex[-3:-1].upper() + summ_of_fio_dm_fchar_hex[-1].upper()
        while len(result[index]) < 3:
            result[index] = '0' + result[index]
    '''
    block for stdout
    '''
    # for (index,item) in enumerate(result):
    #     sys.stdout.write(item)
    #     sys.stdout.write(' ')
    # sys.stdout.write('\n')

    result_as_str = ' '.join(result)
    result_as_str = result_as_str + ' \n'

    return result_as_str

