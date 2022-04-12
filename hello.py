from itertools import permutations


def quicksort(arr, tuple_series):
    """
    arr: list
    """
    def partition(arr, left, right):
        x = arr[right]
        i = left - 1

        for j in range(left, right):
            tuple_series.append((j + 1, right + 1, arr[j] <= x))
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i + 1
    
    def sort(left, right):
        if right <= left:
            return
        
        mid = partition(arr, left, right)
        sort(left, mid - 1)
        sort(mid, right)
    
    sort(0, len(arr) - 1)

# Test

for a, b, c, d in permutations([1, 2, 3, 4], 4):
    arr = [a, b, c, d]
    tuple_series = []
    quicksort(arr.copy(), tuple_series)
    if tuple_series[0] == (1, 4, False) and tuple_series[1] == (2, 4, False) and tuple_series[2] == (3, 4, False) and \
        tuple_series[4] == (2, 4, False):
        print(tuple_series, arr)
