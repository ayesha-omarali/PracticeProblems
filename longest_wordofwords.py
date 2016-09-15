'''
GOAL: Given a list of words, find the longest word made of other words in the list
'''

def longest_wordofwords(INPUT):
    superwords = list(set([j for i in INPUT for j in INPUT if i in j and i != j]))
    superwords
    return max(superwords, key=len)
    #OR WITHOUT BUILT IN FUNCTION:
    # word, count = '', 0
    # for i in superwords:
    #     if len(i) > count:
    #         count = len(i)
    #         word = item
    # return item

INPUT = ['cat', 'banana', 'nana', 'dog', 'walk', 'walker', 'dogwalker']
print longest_superword(INPUT)
