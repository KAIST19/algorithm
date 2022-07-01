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
This code breaks down into two parts:
```python
def quicksort(arr):
    # while going through all the elements (j), if it's smaller than the pivot, send it to the left.
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