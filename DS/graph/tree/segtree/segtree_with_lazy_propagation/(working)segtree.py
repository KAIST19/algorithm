def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node * 2, start, (start + end) // 2)
        init(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            # https://book.acmicpc.net/ds/segment-tree-lazy-propagation
    