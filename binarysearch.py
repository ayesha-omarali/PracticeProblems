'''
Basic implementation of binary search: a fun, simple function.
O(1) complexity & O(logn) performance
'''

def binarysearch(array, value):
    '''
    0 9  #print low, high
    5 9  #each time binaryrecursive is called
    5 6  #this demonstrates how binary search works!
    6 6
    6
    '''
    low = 0
    high = len(array) - 1
    while low <= high:
        print low, high
        mid = (low + high) / 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid
    return None

def binaryrecursive(array, value, low, high):
    '''
    0 9  #print low, high
    5 9  #each time binaryrecursive is called
    5 6  #this demonstrates how binary search works!
    6 6  #note how it's the same as above function!
    6
    '''
    if low > high:
        return None
    mid = (low + high) / 2
    if array[mid] < value:
        return binaryrecursive(array, value, mid + 1, high)
    elif array[mid] > value:
        return binaryrecursive(array, value, low, mid-1)
    else:
        return mid

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print binarysearch(array, 7)
# print binaryrecursive(array, 7, 0, len(array)-1)
