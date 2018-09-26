#Modified Lab 02 code written by Katy M. Nichols
#Tuesday 
August 28, 2018
#Class: 2003-L2 

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

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - \
        self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num *otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
      
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def show(self):
        print(self.num,"/",self.den)

    def __le__(self, otherfraction):
        k= (self.den * otherfraction.num)/otherfraction.den;
        if(self.num<=k):
            return True;
        else:
            return False;

fp = open("lab02data.txt","r")
line = fp.readline()  #ignore first line
line = fp.readline()

while line!="":

    fouritems=line.split()

    x = Fraction(int(fouritems[0]),int(fouritems[1]))
    y = Fraction(int(fouritems[2]),int(fouritems[3]))

    print("The first fraction is: ",x)
    print("the second fraction is ",y)
    print("The sum of two fraction is", x + y)
    print("The difference of the two fraction is: ",x-y)
    print("The product of the two fraction is : ", x*y)
    print("The first fraction is divided by the second fraction is: ",x/y)
    print("the first fraction is <= the second fraction: ",x<=y)
    print()
    print("The next pair of fractions ...")
    print()
    line=fp.readline()

