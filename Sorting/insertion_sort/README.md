# Insertion Sort

## Code
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
```

## Arguments

- arr: the array to be sorted

## How it works

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