from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    prev=[0]*4
    prev[0]=max(points[0][1],points[0][2])
    prev[1]=max(points[0][0],points[0][2])
    prev[2]=max(points[0][0],points[0][1])
    prev[3]=max(points[0][0],max(points[0][1],points[0][2]))

    for day in range(1,n):
        temp=[0]*4
        for last in range(4):
            temp[last]=0
            for task in range(3):
                if task!=last:
                    point=points[day][task]+ prev[task];
                    temp[last]=max(temp[last],point);
        prev=temp
    return prev[3]
    pass
