"""
Quicksort is an in-place sorting algorithm.

This sort is NOT STABLE.

Time complexity:
Best: Omega(n^2)
Average: Theta(n log n)
Worst: O(n log n)
"""
def quicksort(arr):
    """
    arr: list
    """
    def partition(arr, left, right):
        x = arr[right]
        i = left - 1
        for j in range(left, right):
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
# arr = [5, 2, 4, 6, 1, 3]
# quicksort(arr)
# print(arr)  