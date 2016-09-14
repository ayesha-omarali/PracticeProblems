'''
GOAL: Use quicksort algorithm to sort an unsorted array.
The pivot variable is a random number used to compare; I grabbed the last item of the array to start off with, then used the item on the right side
    of my invisible wall.
    This is a good and bad thing -- as the pivot could possibly be a highest or lowest value in the array, leading to the worst case runtime of O(n^2); however on average this
    comparison yields a O(nlogn) runtime -- n for the total comparisons of array of length n, and logn for the number
    of times we divide the list with the invisible wall.

Ultimately, the real benefit of quicksort over mergesort -- despite its worst case runtime of O(n^2) and mergesort's consistent O(nlogn) -- is
    that quicksort requires little additional space and has good cache locality, making it faster in many practical cases.
    In addition, it's easy to avoid the worst runtime for quicksort by having an intelligent choice for pivot, such as picking randomly or choosing a median value.
'''

class QuickSort(object):
    def __init__(self, array):
        self.array = array
        print self.sort(self.array)

    def sort(self, array):
        less = []
        equal = []
        greater = []
        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                if x == pivot:
                    equal.append(x)
                if x > pivot:
                    greater.append(x)
            return self.sort(less)+equal+self.sort(greater)
        return array

INPUT = [6, 5, 1, 3, 8, 4, 7, 9, 2]
QuickSort(INPUT)
INPUT = [5, 6, 456, 34, 1, 88, 4, 2, 0]
QuickSort(INPUT)
#tests pass! yay!
