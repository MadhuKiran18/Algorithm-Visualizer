def bubble_sort(arr):
    steps = []
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            steps.append(arr.copy())
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    steps.append(arr.copy())
    return steps


def merge_sort(arr):
    steps = []

    def merge_sort_helper(a):
        if len(a) > 1:
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]

            merge_sort_helper(left)
            merge_sort_helper(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1
                steps.append(a.copy())

            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
                steps.append(a.copy())

            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
                steps.append(a.copy())

    merge_sort_helper(arr)
    return steps