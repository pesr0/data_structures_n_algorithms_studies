def binary_search(arr: list, target: int) -> int:

    head_i = 0
    tail_i = len(arr)-1

    while head_i <= tail_i:
        mid_i = head_i + (tail_i-head_i)//2

        if arr[mid_i] == target:
            return mid_i
        
        if arr[mid_i] > target:
            tail_i = mid_i - 1
        
        if arr[mid_i] < target:
            head_i = mid_i + 1

    return -1

if __name__ == '__main__':
    test_arr = [1, 3, 6, 10, 13, 16, 19, 22, 26, 29, 35, 47, 55, 56, 57, 58, 59, 60, 69, 90, 101]

    index = binary_search(test_arr, 90)
    print(index)