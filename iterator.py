'''
This is a practice problem to create two iterators and then creating an interator that iterates over the iterators! #meta
'''
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# for c in Counter(0, 25):
#     print c

class Alphabet:
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, low, high):
        self.current = low
        self.high = len(self.alpha) - 1

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.alpha[self.current - 1]

# for c in Alphabet(0, 25):
#     print c

class IteratoringIterators:
    def __init__(self, iterator1, iterator2):
        self.iterator1 = iterator1
        self.iterator2 = iterator2

    def __iter__(self):
        return self

    def next(self):
        #Raising stop iteratorion is done with the iterators!
        if self.iterator1.current > self.iterator1.high and self.iterator2.current < self.iterator2.high:
            #if iterator1 is done but iterator2 is not
            return self.iterator2.next()
        elif self.iterator2.current > self.iterator2.high and self.iterator1.current < self.iterator1.high:
            #vice versa
            return self.iterator1.next()
        if self.iterator2.current > self.iterator1.current:
            #alternating iterators
            return self.iterator1.next()
        else:
            return self.iterator2.next()

for c in IteratoringIterators(Alphabet(0, 40), Counter(0, 40)):
    print c

'''
Excerpt from output:
0
a
1
b
2
c
3
d
4
e
5
f
6
g
7
h
8
i
... ... ...
y
25
z
26
27
28
29
30
31
32
33
34
35
36
37
38
39
'''
