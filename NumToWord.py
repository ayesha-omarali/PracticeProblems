'''
GOAL: Given an integer (already converted into a string), return a string of words with the equivalent value.
i.e. 123 => one hundred and twenty three
'''


ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
tens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
supers = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}


class NUMTOWORD(object):
    def __init__(self, num):
        self.num = num

    def num_to_word(self):
        length = len(self.num)
        if length == 1:
            return ones[self.num]
        if length == 2:
            if self.num.startswith('1'):
                return tens[self.num]
            return supers[self.num[0]] + '-' + ones[self.num[1]]
        if length == 3:
            hundred = True
        if length > 3:
            thousand = True
        if length > 6:
            million = True

        if length % 3 == 0:
            lst = [self.num[i:i+3] for i in range(0, length, 3)]
        if length % 3 == 1:
            temp = self.num[0]
            lst = [self.num[i:i+3] for i in range(1, length, 3)]
            if million:
                result = ones[temp] + ' million '
                million = False
            elif thousand:
                result = ones[temp] + ' thousand '
                thousand = False
        if length % 3 == 2:
            temp = self.num[:2]
            lst = temp + [self.num[i:i+3] for i in range(2, length, 3)]
            if temp.startswith('1'):
                result = tens[temp]
            else:
                result = supers[temp[0]] + '-' + ones[temp[1]]
            if million:
                result = result + ' million '
                million = False
            elif thousand:
                result = result + ' thousand '
                thousand = False

        result = self.helper(lst, result, million, thousand)
        return result

    def helper(self, lst, result, million, thousand):
        for i in lst:
            legend = ones[i[0]]
            ary = i[1:]
            if ary.startswith('1'):
                ary = tens[ary]
            else:
                ary = supers[ary[0]] + '-' + ones[ary[1]]
            if i == lst[-1]:
                text = legend + ' hundred and ' + ary
            else:
                if million:
                    text = legend + ' hundred ' + ary + ' million '
                    million = False
                elif thousand:
                    text = legend + ' hundred ' + ary + ' thousand '
                    thousand = False
            result = result + text
        return result

def main():
    INPUT = '1234567'
    ANS = "one million two hundred thirty-four thousand five hundred and sixty-seven"
    OUTPUT = NUMTOWORD(INPUT).num_to_word()
    print OUTPUT
    if ANS == OUTPUT:
        print '** SUCCESS! **'
    ANS = 'forty-two'
    OUTPUT = NUMTOWORD('42').num_to_word()
    print OUTPUT
    if ANS == OUTPUT:
        print '** SUCCESS! **'



if __name__ == '__main__':
    main()
