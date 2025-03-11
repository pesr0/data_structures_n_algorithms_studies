def bubble_sort(arr: list) -> list:
    '''
    Bubble sort implementation
    In the worst case, the time complexity of this algo is O(n^2),
    since iterations over the entire list can happen up to n times. 

    Args:
    arr (list): list to be ordered

    Returns:
    list: arr sorted
    '''

    for _ in range(len(arr)-1):

        # controls early stopping 
        # if no switch happened, that means the list is already ordered
        switched = False

        for item_i in range(len(arr)-1):
            if arr[item_i] > arr[item_i+1]:
                arr[item_i], arr[item_i+1] = arr[item_i+1], arr[item_i]
            
                switched = True

        if not switched:
            break

    return arr


if __name__ == '__main__':
    ordered_arr = bubble_sort([10, 5, 90, 78, 23, 67, 99, 101, 999, 65, 13, 254, 876, 54, 19])
    print(ordered_arr)