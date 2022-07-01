# Merge Sort

## Code
```python
def merge_sort(arr):
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
```

## Arguments
- arr: the array to be sorted

## How it works
This code breaks down into two parts: merge, sort
- merge: merge the two sorted arrays into one sorted array
- sort: divide the array into two parts and sort them recursively

### merge
```python
def merge(low, mid, high):
    temp = []
    l, h = low, mid

    # merge the two sorted arrays into temp
    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1
    
    # add the rest of the elements to the temp array
    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < high:
        temp.append(arr[h])
        h += 1
    arr[low:high] = temp
```

### sort
```python
def sort(low, high):
    if high - low < 2:
        return

    # divide and conquer
    mid = (low + high) // 2
    sort(low, mid)
    sort(mid, high)
    merge(low, mid, high)
```

