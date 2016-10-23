#AYESHA OMARALI
'''
GOAL: Given an integer, return a string of words with the equivalent value.
i.e. 123 => one hundred and twenty three
'''

#MAPS NUMBERS TO BASE WORDS AND ADJUSTS FOR SPECIAL CASES, LIKE TENS
ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
tens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
supers = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

class NumToWord(object):
    def __init__(self, num):
        self.num = str(num)
        if '-' in self.num:
            self.negative = True
            self.num = self.num.strip('-')
        else:
            self.negative = False

    #CHECKS CASES THAT CAN BE DIRECTLY DERIVED FROM ONLY THE DICTIONARIES
    def pre_process(self, length):
        if length == 1:
            return ones[self.num]
        if length == 2:
            if self.num.startswith('1'):
                return tens[self.num]
            return supers[self.num[0]] + '-' + ones[self.num[1]]
        return None

    #DECIDES WHICH CASES TO EVALUATE AND ADD TO RESULT, CALLS HELPER TO FINALIZE THE RESULT
    def num_to_word(self):
        result, million, thousand, hundred, length = '', False, False, False, len(self.num) #CREATE FLAGS IN ORDER TO DETERMINE HOW LARGE OF A CASE TO CONSIDER
        if self.pre_process(length):
            return self.pre_process(length)
        if length >= 3:
            thousand = True
            hundred = True
        if length > 6:
            million = True
        if length % 3 == 0:
            lst = [self.num[i:i+3] for i in range(0, length, 3)] #LIST DIVIDES NUMBER INTO THREES TO CATEGORIZE LATER
        if length % 3 == 1:
            temp = self.num[0]
            lst = [self.num[i:i+3] for i in range(1, length, 3)]
            if million:
                result, million = ones[temp] + ' million ', False
            elif thousand:
                result, thousand = ones[temp] + ' thousand ', False
        if length % 3 == 2:
            temp, lst = self.num[:2], temp + [self.num[i:i+3] for i in range(2, length, 3)]
            if temp.startswith('1'):
                result = tens[temp]
            else:
                result = supers[temp[0]] + '-' + ones[temp[1]]
            if million:
                result, million = result + ' million ', False
            elif thousand:
                result, thousand = result + ' thousand ', False
        result = self.helper(lst, result, million, thousand)
        return self.final(result)

    #ITERATES AND ADJUSTS FOR MILLIONS AND THOUSANDS WHILE ADDING "AND" IN APPROPRIAE PLACES
    def helper(self, lst, result, million, thousand):
        length = len(lst)
        count = 0
        for i in lst:
            count += 1
            legend = ones[i[0]]
            ary = i[1:]
            if ary.startswith('1'):
                ary = tens[ary]
            else:
                ary = supers[ary[0]] + '-' + ones[ary[1]]
            if count == length:
                text = legend + ' hundred and ' + ary
            else:
                if million:
                    text = legend + ' hundred ' + ary + ' million, '
                    million = False
                elif thousand:
                    text = legend + ' hundred ' + ary + ' thousand, '
                    thousand = False
            result = result + text
        return result

    def final(self, result): #CHECKS NEGATIVE CASE
        if self.negative:
            result = "negative " + result
            return result
        return result

def main(): #TEST CASES, ALL RETURN SUCCESS
    INPUT = '1234567'
    ANS = "one million two hundred thirty-four thousand five hundred and sixty-seven"
    OUTPUT = NumToWord(INPUT).num_to_word()
    print(OUTPUT)
    if ANS == OUTPUT:
        print('** SUCCESS! **')
    ANS = 'forty-two'
    OUTPUT = NumToWord('42').num_to_word()
    print(OUTPUT)
    if ANS == OUTPUT:
        print('** SUCCESS! **')
    ANS = 'one hundred and forty-two'
    OUTPUT = NumToWord('142').num_to_word()
    print(OUTPUT)
    if ANS == OUTPUT:
        print('** SUCCESS! **')
    ANS = 'nineteen'
    OUTPUT = NumToWord('19').num_to_word()
    print(OUTPUT)
    if ANS == OUTPUT:
        print('** SUCCESS! **')
    OUTPUT = NumToWord('-999999999').num_to_word()
    print(OUTPUT)


if __name__ == '__main__':
    main()
