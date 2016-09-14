'''
GOAL: Use quicksort algorithm to sort an unsorted array.

The wall varaible is an invisible wall, which prevents the necessity of creating a new empty list and moving
    the sorted items to that list. As I compare and sort the items, I put them in relation to this wall
    and then "move" the wall by increasing its index.
The pivot variable is a random number used to compare; I grabbed the last item of the array to start off with, then used the item on the right side
    of my invisible wall.
    This is a good and bad thing -- as the pivot could possibly be a highest or lowest value in the array, leading to the worst case runtime of O(n^2); however on average this
    comparison yields a O(nlogn) runtime -- n for the total comparisons of array of length n, and logn for the number
    of times we divide the list with the invisible wall.

Ultimately, the real benefit of quicksort over mergesort -- despite its worst case runtime of O(n^2) and mergesort's consistent O(nlogn) -- is
    that quicksort requires little additional space and has good cache locality, making it faster in many practical cases.
    In addition, it's easy to avoid the worst runtime for quicksort by having an intelligent choice for pivot.
'''

class QuickSort(object):
    def __init__(self, array):
        self.array = array
        self.pivot = array[-1]

    def sort(self):
        wall = 0
        while len(self.array[wall:]) > 1:
            for i in self.array[wall:]:
                if i < self.pivot:
                    i_index = self.array.index(i)
                    self.array[i_index],self.array[wall] = self.array[wall], self.array[i_index]
                    wall += 1
            i_index = self.array.index(self.pivot)
            self.array[i_index], self.array[wall] = self.array[wall], self.array[i_index]
            wall += 1
            if len(self.array[wall:]) > 2:
                self.pivot = self.array[wall]
            else:
                if self.array[-2] > self.array[-1]:
                    self.array[-2], self.array[-1] = self.array[-1], self.array[-2]
        return self.array

INPUT = [6, 5, 1, 3, 8, 4, 7, 9, 2]
print QuickSort(INPUT).sort()
INPUT = [5, 6, 456, 34, 1, 88, 4, 2, 0]
print QuickSort(INPUT).sort()
#tests pass! yay!
