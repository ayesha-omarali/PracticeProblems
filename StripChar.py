'''
GOAL: Given a string, return the same string with all duplicate characters removed
'''

import collections

class STRIPCHAR(object):

    def __init__(self, INPUT):
        self.INPUT = INPUT
        self.chars = INPUT.lower().replace(' ', '')
        self.dic = collections.defaultdict(int)

    def strip_char(self):
        for c in self.chars:
            self.dic[c] += 1
        cleaned = {key: value for key, value in self.dic.items() if value is not 1}
        for key in cleaned.keys():
            self.INPUT = self.INPUT.replace(key, '')
            self.INPUT = self.INPUT.replace(key.upper(), '')
        return self.INPUT


def main():
    print "**** TEST 0 ****"
    INPUT = 'HeLlo dEar'
    print "INPUT: %s" %INPUT
    OUTPUT = STRIPCHAR(INPUT).strip_char()
    print "OUTPUT: %s" %OUTPUT
    print

    print "**** TEST 1 ****"
    INPUT = "I dO NoT eAt PiZza When plaYing hoP SkotCH"
    print "INPUT: %s" %INPUT
    OUTPUT = STRIPCHAR(INPUT).strip_char()
    print "OUTPUT: %s" %OUTPUT
    print

    print "**** TEST 1 ****"
    INPUT = "wHat Would yoU do if I jumpEd under the BaNANA tree?"
    print "INPUT: %s" %INPUT
    OUTPUT = STRIPCHAR(INPUT).strip_char()
    print "OUTPUT: %s" %OUTPUT
    print


if __name__ ==  '__main__':
    main()
