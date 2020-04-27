import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
# game loop
bomb_dir = input()
while True:
    U, UR, R, DR, D, DL, L, UL = 1,1,1,1,1,1,1,1
    while bomb_dir == "U":
        a= y0-U
        if a<0:
            y0=0
        else:
            y0=a
        U*=2
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "UR":
        a= y0-UR
        if a<0:
            y0=0
        else:
            y0=a
        b = x0 + UR
        if b>w:
            x0 = w-1
        else:
            x0 = b
        UR*=2 
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "R":
        b = x0 + R
        if b>w:
            x0 = w-1
        else:
            x0 = b
        R*=2
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "DR":
        b = y0 + DR
        a = x0 + DR
        if a>w:
            x0=w-1
        else:
            x0=a
        if b>h:
            y0=h-1
        else:
            y0=b
        DR*=2 
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "D":
        a = y0 + D
        if a>h:
            y0=h-1
        else:
            y0=a
        D*=3
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "DL":
        b=y0+DL
        a=x0-DL
        if b>h:
            y0=h-1
        else:
            y0=b
        if a>w:
            x0=w-1
        else:
            x0=a
        DL*=2 
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "L":
        a = x0-L
        if a<0:
            x0=0
        else:
            x0=a
        L*=2 
        print(str(x0), str(y0))
        bomb_dir = input() 
    while bomb_dir == "UL":
        b= y0-UL 
        a= x0-UL
        if a<0:
            x0=0
        else:
            x0=a
        if b<0:
            y0=0
        else:
            y0=b
        UL*=2 
        print(str(x0), str(y0))
        bomb_dir = input() 
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # the location of the next window Batman should jump to.