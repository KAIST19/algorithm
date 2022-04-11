"""
Quicksort is an in-place sorting algorithm.

This sort is NOT STABLE.
"""
def quickselect(arr, k):
    """
    arr: list
    i: int
        1) this function returns the k-th smallest element in arr
        2) 0 <= i < len(arr)
    """
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i + 1

    def select(arr, left, right, k):
        pivot = partition(arr, left, right)
        if pivot == k:
            return arr[pivot]
        elif pivot > k:
            return select(arr, left, pivot - 1, k)
        else:
            return select(arr, pivot + 1, right, k)
    
    arr = arr.copy()
    return select(arr, 0, len(arr) - 1, k)
    

# Test
# arr = [1, 3, 2]
# print(sorted(arr))
# for i in range(len(arr)):
#     print(quickselect(arr, i), end=' ')