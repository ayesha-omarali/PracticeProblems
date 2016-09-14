'''
GOAL: Write a program to sort an array of strings so that all the anagrams are next to each other
'''

def sort_anagrams(INPUTS):
    INPUTS = [[make_dicts(item), item] for item in INPUTS]
    pairs = [[i[1], j[1]] for i in INPUTS for j in INPUTS if j[0] == i[0] and j[1] != i[1]]
    return [item for sublist in pairs for item in sublist]

def make_dicts(x):
    xd = {}
    for c in x:
        if c in xd.keys():
            xd[c] += 1
        else:
            xd[c] = 1
    return xd

#NOTE: this is not used in the GOAL algorithm.
def is_anagram(x, y):
    if len(x) != len(y):
        return False
    xd = {}
    for c in x:
        if c in xd.keys():
            xd[c] += 1
        else:
            xd[c] = 1
    yd = {}
    for c in y:
        if c in yd.keys():
            yd[c] += 1
        else:
            yd[c] = 1
    return xd == yd

# print is_anagram("deductions","discounted")
# print is_anagram('harmonicas','maraschino')
# print is_anagram("percussion", "supersonic")
# print is_anagram('dog', 'god')
# print is_anagram('ello', 'poppet')
# print is_anagram('cat', 'dog')

INPUTS = ['dog', 'deductions', 'maraschino', 'supersonic', 'god', 'percussion', 'maraschino', 'discounted']
print sort_anagrams(INPUTS)
