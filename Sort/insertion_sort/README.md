### Code
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
```

### Arguments
- arr: the array to be sorted

### Time Complexity
- Best case: O(n)
- Average case: O(n^2)
- Worst case: O(n^2)

### How it works
The algorithm starts by picking the second element in the array and inserting it into the sorted array.
```python
    for i in range(1, len(arr)):
        # arr[0:i] is already sorted

        # insert arr[i] into arr[0:i]
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr
```