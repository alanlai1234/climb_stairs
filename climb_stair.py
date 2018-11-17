#!/usr/bin/env python
# coding: utf-8


def climb(s):
    if s==1 or s==2 or s==3:
        return s
    else:
        return climb(s-1)+climb(s-2)+climb(s-3)
print(climb(3))



#bottom-up

def climb_bottom(s):
    if s==1 or s==2 or s==3:
        return s
    table=[0]*(s+1)
    table[1]=1
    table[2]=2
    table[3]=4
    
    for i in range(4, s+1):
        table[i]=table[i-1]+table[i-2]+table[i-3]
    return table[s]
climb_bottom(60)



#top-down

def climb_top(s):
    if s==1 or s==2 or s==3:
        return s
    
    table=[0]*(s+1)
    table[0]=1
    table[1]=1
    table[2]=2
    table[3]=4
    
    n=4
    while n<=s:
        if not table[n]:
            table[n]=table[n-1]+table[n-2]+table[n-3]
        n+=1
    return table[s]
climb_top(60)
