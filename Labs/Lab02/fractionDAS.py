#fractionDAS.py
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


fp = open("lab02data.txt","r")
line = fp.readline()  #ignore first line
line = fp.readline()
while line!="":
    #   x = Fraction(1, 2)  this is left over from original code
    #   y = Fraction(2, 3)  this is left over from original code

    fouritems=line.split()
    x = Fraction(int(fouritems[0]),int(fouritems[1]))
    y = Fraction(int(fouritems[2]),int(fouritems[3]))

    print("x is ",x)
    print("y is ",y)
    print("sum is", x + y)
    print("x is the same fraction as y:", x == y)
    print("The next pair of fractions ...")
    line=fp.readline()
