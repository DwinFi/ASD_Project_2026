def gnome_sort(arr):
    a = arr.copy()
    n = len(a)
    index = 0
    while index < n:
        if index == 0 or a[index] >= a[index - 1]:
            index += 1
        else:
            a[index], a[index - 1] = a[index - 1], a[index]
            index -= 1
    return a