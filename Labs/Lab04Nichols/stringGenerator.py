        import random      #stringGenerator.py
        import string
        import time
        from itertools import permutations

        def anagramSolution1(s1,s2):
            alist = list(s2)

            pos1 = 0
            stillOK = True

            while pos1 < len(s1) and stillOK:
                pos2 = 0
                found = False
                while pos2 < len(alist) and not found:
                    if s1[pos1] == alist[pos2]:
                        found = True
                    else:
                        pos2 = pos2 + 1

                if found:
                    alist[pos2] = None
                else:
                    stillOK = False

                pos1 = pos1 + 1

            return stillOK

        def anagramSolution2(s1,s2):
            alist1 = list(s1)
            alist2 = list(s2)

            alist1.sort()
            alist2.sort()

            pos = 0
            matches = True

            while pos < len(s1) and matches:
                if alist1[pos]==alist2[pos]:
                    pos = pos + 1
                else:
                    matches = False

            return matches

        #anagramSolutions3 is not implemented in Miller notes
        def anagramSolution3(s1,s2):
            perms = [''.join(p) for p in permutations(s2)]
            found=False
            for s in perms:
                if s1 == s:
                    found = True
                    break
            return found

        def anagramSolution4(s1,s2):
            c1 = [0]*26
            c2 = [0]*26

            for i in range(len(s1)):
                pos = ord(s1[i])-ord('a')
                c1[pos] = c1[pos] + 1

            for i in range(len(s2)):
                pos = ord(s2[i])-ord('a')
                c2[pos] = c2[pos] + 1

            j = 0
            stillOK = True
            while j<26 and stillOK:
                if c1[j]==c2[j]:
                    j = j + 1
                else:
                    stillOK = False

            return stillOK

        def buildMyString(n):
            s=""
            for i in range(n):
                aletter=random.choice(string.letters)
                s=s+aletter
            return(s)

        #-- the root (main) program starts here

        string.letters = 'abcdefghijklmopqrstuvwxyz'

        n=11
        s1=buildMyString(n)

        if random.uniform(0.0,1.0)<.5:
            r=random.randrange(0,n-1)
            aletter = random.choice(string.letters)
            s2=s1[0:r]+aletter+s1[r+1:n]
        else:
            s2=s1

        print("s1 is: ",s1)
        print("s2 is: ",s2)

        print("\n...timing anagramSolution1 with n = ",n)
        start=time.time()
        print(anagramSolution1(s1,s2))
        print(time.time()-start)

        print("\n...timing anagramSolution2 with n = ",n)
        start=time.time()
        print(anagramSolution2(s1,s2))
        print(time.time()-start)

        print("\n...timing anagramSolution3 with n = ",n)
        start=time.time()
        print(anagramSolution3(s1,s2))
        print(time.time()-start)

        print("\n...timing anagramSolution4 with n = ",n)
        start=time.time()
        print(anagramSolution4(s1,s2))
        print(time.time()-start)

