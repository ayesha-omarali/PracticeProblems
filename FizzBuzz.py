'''
** The classic interview question **
GOAL: Program that prints numbers 1 to x, but for the multiples of three, print "fizz"
    and for multiples of 5 print "buzz", and for multiples of both print "fizzbuzz" (instead of the integer).
'''

class FizzBuzz(object):
    def __init__(self, up_until):
        self.num = up_until

    def fizzbuzz_modulo(self):
        x = 1
        while x <= self.num:
            if x % 3 == 0 and x % 5 == 0:
                print "FizzBuzz"
            elif x % 5 == 0:
                print "Buzz"
            elif x % 3 == 0:
                print "Fizz"
            else:
                print x
            x += 1
        return "Done!"

    def fizzbuzz_modulo_1(self):
        for x in range(1, self.num + 1):
            s = ""
            if x % 3 == 0:
                s += "Fizz"
            if x % 5 == 0:
                s += "Buzz"
            if s == "":
                s = x
            print s
        return "Done!"

    def fizzbuzz_one_liner(self):
        print '\n'.join(['Fizz'*(x % 3 == 2) + 'Buzz'*(x % 5 == 4) or str(x + 1) for x in range(0, self.num)])
        return "Done!"

    def fizzbuzz_bitwise(self):
        c = 0
        acc = 810092048
        words = ['null', 'Fuzz', 'Buzz', 'FizzBuzz']
        for i in range(1, self.num + 1):
            c = acc & 3
            acc = acc >> 2 | c << 28
            if words[c] == 'null':
                print i
            else:
                print words[c]
        return "Done!"

print FizzBuzz(15).fizzbuzz_modulo()
print FizzBuzz(15).fizzbuzz_modulo_1()
print FizzBuzz(15).fizzbuzz_one_liner()
print FizzBuzz(15).fizzbuzz_bitwise()
