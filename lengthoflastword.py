def lengthoflastword(A):
    if A == '':
        return 0
    A = A[::-1]
    word = ''
    flag = True
    if A[0] == ' ':
        count = 0
        for i in A:
            if i != ' ':
                word += i
                flag = False
            elif i == ' ' and not flag:
                break
        A = word
    if A:
        i = A[0]
    else:
        return 0
    count = len(A) - 1
    while ' ' in A:
        A = A[:count]
        count -= 1
    count = 0
    for item in A:
        count += 1
    return count

print lengthoflastword("    ")
