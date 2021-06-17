
#DaRk DeveloPer

import sys

# taking input as string
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda: list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
mod = 10 ** 9 + 7;
Mod = 998244353;
INF = float('inf')
# ______________________________________________________________________________________________________
from math import *
from bisect import *
from heapq import *
from collections import defaultdict as dd
from collections import OrderedDict as odict
from collections import Counter as cc
from collections import deque
from itertools import groupby

sys.setrecursionlimit(20 * 20 * 20 * 20 + 10)  # this is must for dfs
MAX = 10 ** 5
"""TLE

	n,m=takeivr()

	arr=takeiar()

	if m==n:
		print(0)
		return 
	if m==1:
		print(len(set(arr))-1)
		return

	s=set() 

	for i in range(0,n-m+1):
		s.add(sum(arr[i:i+m]))
	print(len(s)-1)




	return
"""

def solve():



   n,m=takeivr()

   arr=takeiar()

   if m==n:
   	print(0)
   if m==1:
   	print(set(arr)-1)
   dict_1=dd(dict)

   for i in range(n):

   	if arr[i] not in dict_1[i%m]:
   		dict_1[i%m][arr[i]]=1
   	else:
   		dict_1[i%m][arr[i]]+=1

   count=0

   

   for i in dict_1.keys():

 

   	count+=sum(dict_1[i].values())-max(dict_1[i].values())

   print(count)





   return 


def main():
    global tt


   
    t = 1
    t = takein()
    # t = 1
    for tt in range(1, t + 1):
        solve()
   


# ---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def takein():
    return (int(sys.stdin.readline().rstrip("\r\n")))


# input the string

def takesr():
    return (sys.stdin.readline().rstrip("\r\n"))


# input int array
def takeiar():
    return (list(map(int, sys.stdin.readline().rstrip("\r\n").split())))


# input string array
def takesar():
    return (list(map(str, sys.stdin.readline().rstrip("\r\n").split())))


# innut values for the diffrent variables
def takeivr():
    return (map(int, sys.stdin.readline().rstrip("\r\n").split()))


def takesvr():
    return (map(str, sys.stdin.readline().rstrip("\r\n").split()))


# ------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#


def ispalindrome(s):
    return s == s[::-1]


def invert(bit_s):
    # convert binary string
    # into integer
    temp = int(bit_s, 2)

    # applying Ex-or operator
    # b/w 10 and 31
    inverse_s = temp ^ (2 ** (len(bit_s) + 1) - 1)

    # convert the integer result
    # into binary result and then
    # slicing of the '0b1'
    # binary indicator
    rslt = bin(inverse_s)[3:]

    return str(rslt)


def counter(a):
    q = [0] * max(a)
    for i in range(len(a)):
        q[a[i] - 1] = q[a[i] - 1] + 1
    return (q)


def counter_elements(a):
    q = dict()
    for i in range(len(a)):
        if a[i] not in q:
            q[a[i]] = 0
        q[a[i]] = q[a[i]] + 1
    return (q)


def string_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97] + 1
    return (q)


def factorial(n, m=1000000007):
    q = 1
    for i in range(n):
        q = (q * (i + 1)) % m
    return (q)


def factors(n):
    q = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: q.append(i); q.append(n // i)
    return (list(sorted(list(set(q)))))


def prime_factors(n):
    q = []
    while n % 2 == 0: q.append(2); n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0: q.append(i); n = n // i
    if n > 2: q.append(n)
    return (list(sorted(q)))


def transpose(a):
    n, m = len(a), len(a[0])
    b = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
    return (b)


def power_two(x):
    return (x and (not (x & (x - 1))))


def ceil(a, b):
    return -(-a // b)


def seive(n):
    a = [1]
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p = p + 1
    for p in range(2, n + 1):
        if prime[p]:
            a.append(p)
    return (a)


def isprime(n):
    if (n > 2 and not n % 2) or n == 1:
        return False


    for i in range(3, int(n ** 0.5 + 1), 2):
        if not n % i:
            return False

    return True

# -----------------------------------------------------------------------#
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline

main()
