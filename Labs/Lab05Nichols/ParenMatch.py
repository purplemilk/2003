#Program created by Katy M. Nichols
# CS 2003-L2
# Lab 04

#Algorithm ParenMatch(X):
#Input: A string X of n tokens, each of which is either
#a grouping symbol from the lefty list of three symbols:  ( { [   or
#the righty list of three symbols:  ) } ]   or from
#the list of single character upper case variables: A B C ... Z  or from
#the list of arithmetic binary operators:  + - * /’
#Output: True if and only if all the grouping symbols in X match; otherwise, print False.

def ParenMatch(x):
    
    s = []

    for c in x:

        if c in '({[':
            s.append(c)

        elif c in ')}]':

            if len(s) == 0 :
                return False

            x = s.pop()

            if c==')' and x!='(':
                return False

            elif c=='}' and x!='{':
                return False

            elif c==']' and x!='[':
                return False

    return len(s) == 0
    
print(ParenMatch("A*B+C*D"))
print(ParenMatch("(A+B)*(C-(D-E))*(F+G)"))
print(ParenMatch("((A+{B+C}-[D—E])+[F]-[G]"))
print(ParenMatch("(A+B)*(C+D)"))
print(ParenMatch("A/B—C+D*E-A*C"))
print(ParenMatch("(((A/B)-C)+(D*E))-A*C)"))
print(ParenMatch("A/(B-C+D))*(E-A)*C"))