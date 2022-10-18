'''
Task here: /src/interval_time_through_thorns_to_a_client/*.png
'''


import sys
import collections
import datetime


def interval_time_through_thorns_to_a_client(data):
    input_data_list = []
    # input_data_list.append(int(sys.stdin.readline().strip()))
    input_data_list.append(int(data[0].strip()))
    i = 1
    while len(input_data_list) < int(input_data_list[0])+1:
        # input_data_list.append(sys.stdin.readline().strip())
        input_data_list.append(data[i])
        i += 1
    count = int(input_data_list[0])
    input_data_list = [i.split(' ') for i in input_data_list[1:]]
    dict_of_taxi = collections.defaultdict(list)
    for taxi in input_data_list:
        date = datetime.datetime.strptime(taxi[0]+taxi[1]+taxi[2],'%d%H%M')
        dict_of_taxi[int(taxi[3])].append([taxi[4], date])

    result = [] * count
    for taxi,statuses in dict_of_taxi.items():
        sorted_values = sorted(statuses, key=lambda i: i[1])
        taxi_time_stamp = datetime.datetime(1900, 1, 1)
        start_stamp = None
        end_stamp = None
        for val in sorted_values:
            if val[0] == 'A':
                start_stamp = val[1]
            elif (val[0] == 'S' or val[0] == 'C') and start_stamp is not None:
                end_stamp = val[1]
                taxi_time_stamp = taxi_time_stamp + (end_stamp-start_stamp)
        if end_stamp is None:
            pass
        result = [int((taxi_time_stamp - datetime.datetime(1900, 1, 1)).total_seconds()/60)]
        dict_of_taxi[taxi] = result
    '''
    block for stdout
    '''
    for taxi in sorted(dict_of_taxi):
        if dict_of_taxi[taxi][0] == 0:
            continue
        sys.stdout.write(str(dict_of_taxi[taxi][0]))
        sys.stdout.write(' ')
    sys.stdout.write('\n')

    taxi_ordered = sorted((str(v[0]) for k,v in dict_of_taxi.items()), reverse=True)
    print(taxi_ordered)
    result_as_str = ' '.join(taxi_ordered)
    result_as_str += ' \n'
    return result_as_str
