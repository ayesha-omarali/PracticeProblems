def merge(right, left):
    i, j, = 0, 0
    answer = []
    while i < len(right) and j < len(left):
        if right[i] < left[j]:
            answer = answer + [right[i]]
            i += 1
        else:
            answer = answer + [left[j]]
            j += 1
    while i < len(right):
        answer = answer + [right[i]]
        i += 1
    while j < len(left):
        answer = answer + [left[j]]
        j += 1
    return answer

def mergesort(INPUT):
    if len(INPUT) <= 1:
        return INPUT
    m = len(INPUT) / 2
    right = INPUT[:m]
    left = INPUT[m:]
    right = mergesort(right)
    left = mergesort(left)
    result = merge(right, left)
    return result

print mergesort([4, 2, 6, 4, 1, 6, 10, 33, 0, 53, 3])
#output: [0, 1, 2, 3, 4, 4, 6, 6, 10, 33, 53]

