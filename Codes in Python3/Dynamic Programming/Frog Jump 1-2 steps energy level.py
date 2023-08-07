from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    prev=0
    prev2=0
    for i in range(1,n):
        fs=prev+abs(heights[i]-heights[i-1])
        ss=inf
        if i>1:
            ss=prev2+abs(heights[i]-heights[i-2])
        cur=min(fs,ss)
        prev2=prev
        prev=cur
    return prev
    pass
