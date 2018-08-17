import math
import os
import random
import re
import sys


k = 0
m = 0
i = 0

n = int(input().strip())
x = bin(n)[2:]

for c in x:
    if c == '1':
        m += 1
    else:
        if k < m:
            k = m
        m = 0

# check whether the last run is greater than the current maximum
if k < m:
    k = m

print(k)



if __name__ == '__main__':
    n = int(input())
