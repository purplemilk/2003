import random #stringGenerator.py
import string
import time
from itertools import permutations

## anagram solution 1:
# checks letters off from s1 that occur within s2
def anagramSolution1(s1,s2):
	alist = list(s2)
	pos1 = 0
	# stillOK becomes false when no matching character was found in s2
	stillOK = True

# loop through all characters of s1
# while we do not find a character that is not present in other string
# if we find such character, then there is no need to check further
	while pos1 < len(s1) and stillOK:
		pos2 = 0
# found becomes true is we find a similar character in s2
		found = False

# check this char of s1 with each char of s2
		while pos2 < len(alist) and not found:
# if found similar character, set found to true
# else point to the next character of s2
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 = pos2 + 1

# if a matching character is found, remove it from the list
# so that it does not get matched again
# else if no matching character was found, set stillOK to false
		if found:
			alist[pos2] = None

		else:
			stillOK = False

		pos1 = pos1 + 1

	return stillOK


## anagram solution 2:
# sort and then compare the two strings
def anagramSolution2(s1,s2):
# store the strings in lists and then sort them
	alist1 = list(s1)
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()

# match each character of s1 to its corresponding character in s2
	pos = 0
	matches = True

	while pos < len(s1) and matches:

# if characters match, check next character
# else, set matches to False
	if alist1[pos]==alist2[pos]:
		pos = pos + 1
	else:
		matches = False

	return matches

## anagram solution 3:
# compare the first string with each possible permutation
# of the letters in the second string
def anagramSolution3(s1,s2):
# make a list of all permutaions of s2
	perms = [''.join(p) for p in permutations(s2)]
	found=False
# if any permutation is similar, set found to True
	for s in perms:
		if s1 == s:
			found = True
		break

	return found


## anagram solution 4:
# count the frequency of each letter in each string
def anagramSolution4(s1,s2):
# make two lists of 26 elements for each alphabet letter
	c1 = [0]*26
	c2 = [0]*26

# for each character in s1
	for i in range(len(s1)):
# find out the pos where it corresponds to in the list
		pos = ord(s1[i])-ord('a')
# increase the count of pos
		c1[pos] = c1[pos] + 1
# similar steps of s2
	for i in range(len(s2)):
		pos = ord(s2[i])-ord('a')
		c2[pos] = c2[pos] + 1
# check both the lists
# if all the indices have same count, then s1 and s2 are anagrams
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
# creates random string s1
s1=buildMyString(n)

# creates random string s2
# 50% of the times s1 is exactly same as s2
# 50% of the times s2 has one character that is different from s1
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

