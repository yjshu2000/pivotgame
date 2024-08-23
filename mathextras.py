#lol yea extras for pivot. dont forget this file when moving pivot file ;w;

from math import *


def dist(x1,y1,x2,y2):
    '''calculate distance between two points (2d only :/)'''
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)


def dot(v,w):
    '''take 2 lists of int values as vectors; return dot product'''
    ans = 0
    for i in range(len(v)):
        ans = ans + v[i]*w[i]
    return ans

def cross2(x1,y1,x2,y2):
    '''cross product 2d'''
    return (x1*y2 - x2*y1)

def vmag(v):
    '''returns the magnitude of vector v'''
    ans = 0
    for i in range(len(v)):
        ans += (v[i])**2
    ans = sqrt(ans)
    return ans


def angdifnope(u,v):
    '''return the angle difference between two vectors'''
    theta = acos(dot(u, v) / (vmag(u) * vmag(v)))
    return theta

def angdif(u,v):
    '''return the angle difference between two vectors— specifically,
going clockwise.'''
    do = dot(u,v)
    det = cross2(u[0],u[1], v[0],v[1])
    theta = atan2(det,do)
    return theta

def vectorize(v,w):
    '''takes 2 points in space and converts them to vector going from v->w'''
    ans = []
    for i in range(len(v)):
        ans.append(v[i]-w[i])
    return ans

