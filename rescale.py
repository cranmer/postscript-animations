import os, sys
import string
from math import log, pi

def formatSVM(tuple, label=1):
    outString = str(label)+" "
    for i in range(len(tuple)):
        outString += str(i+1)+":"+str(tuple[i])+" "
    return outString

def formatGP(tuple, label=1):
    outString = ""
    for i in range(len(tuple)):
        outString += str(tuple[i])+" "
    return outString


f = open(str(sys.argv[1]), 'r')
input = f.read()
f.close()

inputLines = input.split('\n')

Range    = range(8)
xform    = range(8)

Range[0] = 9.
Range[1] = pi
Range[2] = 5000.
Range[3] = 2.5
Range[4] = pi
Range[5] = 80.
Range[6] = 200.
Range[7] = 1.

xform[0] = None 
xform[1] = None 
xform[2] = lambda x: log(1.+x)
xform[3] = None 
xform[4] = None 
xform[5] = lambda x: log(1.+x)
xform[6] = lambda x: log(1.+x)
xform[7] = None 

Range[2] = xform[2](Range[2])
Range[5] = xform[5](Range[5])
Range[6] = xform[6](Range[6])

for i in range(len(inputLines))[:-1]:
    inputLine = inputLines[i].split()
    vars = []
    j = 0
    for var in inputLine:
        if xform[j] != None:
            var = xform[j](float(var))
        vars.append(float(var)/Range[j])
        j = j+1
    print formatGP(vars)
    
