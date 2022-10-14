'''
adapting merge fx to an existing algorithm on Pascal w/ input 1 and len(arr)
'''


def Merge(arr: [], index_left: int, middle: int, index_right: int):
    temp_left_part = arr[index_left-1:middle]
    temp_right_part = arr[middle:index_right]
    temp_arr = temp_left_part + temp_right_part
    indexes = list(range(index_left-1, middle, 1)) + list(range(middle, index_right, 1))
    p1_temp = 0
    p2_temp = len(temp_left_part)
    for i in indexes:
        if p1_temp == len(temp_arr):
            arr[i] = temp_arr[p2_temp]
            p2_temp += 1
        elif p2_temp == len(temp_arr):
            arr[i] = temp_arr[p1_temp]
            p1_temp += 1
        elif temp_arr[p1_temp] > temp_arr[p2_temp]:
            arr[i] = temp_arr[p2_temp]
            p2_temp += 1
        else:
            arr[i] = temp_arr[p1_temp]
            p1_temp += 1


def sort_by_merge(arr: [], index_left: int, index_right: int):
    if index_left < index_right:
        middle = int((index_left+index_right)/2)
        sort_by_merge(arr, index_left, middle)
        sort_by_merge(arr, middle+1, index_right)
        Merge(arr, index_left, middle, index_right)
    return arr