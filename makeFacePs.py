import os, sys
import string
from math import log, pi

def PostScriptHeader():
    print """%!PS-Adobe-2.0
%%BoundingBox: 0 -500 700 800
% Demonstrate shading and width in drawing lines and filling shapes
% Define an operator box which builds a path for a one inch square box
% Note that box does not draw or fill the box.
/ellipse {
%  moveto                                % Current point is on stack
    gsave
    translate
  newpath
  gsave
  scale                                 % set x-y scale for ellipse
  0 0 10 0 360 arc
%  closepath                             % Bottom
    stroke
  grestore
  grestore
} def
 
/mouth {
    gsave
   translate
   newpath
   scale
   0 0 10 180 0 arc
   stroke
   grestore
   grestore
                                                                                
} def
                                                                                
/face {
    gsave
    translate
    gsave
    headsquat 1 scale
    10 10 0 0 ellipse
    grestore
    gsave
    -30 30 translate
    eyeangle rotate
    eyesquint 1 0 0  ellipse
    grestore
    gsave
    30 30 translate
    -1 eyeangle mul rotate
    eyesquint 1 0 0 ellipse
    grestore
    5 smile 0 -40 mouth
                                                                                
    grestore
%    0 200 translate
} def
"""

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

def formatPS(tuple, x, y):
    outString = ""
    outString+= '/headsquat %s def\n' %(tuple[0])
    outString+= '/eyeangle %s def\n' %(tuple[2])
    outString+= '/smile %s def\n' %(tuple[3])
    outString+= '/eyesquint %s def\n' %(tuple[4])
    outString+= '2 %f %f  face\n' %(x,y)
    return outString

f = open(str(sys.argv[1]), 'r')
input = f.read()
f.close()

inputLines = input.split('\n')

PostScriptHeader()
print "400 200 moveto"
#for i in range(len(inputLines))[:-1]:
for i in range(80):
    vars = inputLines[i].split()
    if i%4==1:
        print formatPS(vars, 500, 200)
        print "400 200 moveto"
        print "showpage"
    elif i%4==2:
        print "200 400 moveto"
        print formatPS(vars, 200, 500)
    elif i%4==3:
        print formatPS(vars, 500, 500)
        print "400 400 moveto"
    else:
        print formatPS(vars, 200, 200)
        print "200 200 moveto"
        

