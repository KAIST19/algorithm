# Quick Sort

## Code
```python
def quicksort(arr):
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
```

## Arguments
- arr: the array to be sorted

## How it works
This code breaks down into two parts: partition, sort
- partition: partition the array into two parts
- sort: divide the array into two parts and sort them recursively

### Partition

```python
def partition(arr, left, right):
    x = arr[right] # pivot
    i = left - 1

    # while going through all the elements (j), if it's smaller than the pivot, send it to the left.
    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # now, arr[1:i+1] is smaller than the pivot
    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1 # becomes mid
```

### Sort

```python
def sort(left, right):
    if right <= left:
        return
    
    mid = partition(arr, left, right)
    sort(left, mid - 1)
    sort(mid, right)

sort(0, len(arr) - 1)
```