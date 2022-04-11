"""
Builds the final sorted array (or list) one item at a time.

This sort is STABLE.

Time complexity:
Best: Omega(n)
Average: Theta(n^2)
Worst: O(n^2)
"""
def insertion_sort(arr):
    """
    arr: list
        1) The array to be sorted.
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr