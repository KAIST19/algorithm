"""
merge sort is an efficient, general-purpose, and comparison-based sorting algorithm.

This sort is STABLE.

Time complexity:
Best: Omega(n log n)
Average: Theta(n log n)
Worst: O(n log n)
"""
def merge_sort(arr):
    """
    arr: list
        1) The array to be sorted.
    """
    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        arr[low:high] = temp

    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    return sort(0, len(arr))


# Test
arr = [5, 2, 4, 6, 1, 3]
merge_sort(arr)
print(arr)  