import math
#################################################
#Project 1a - Matrix Transformations
#CS 3451 - Computer Graphics
#Bryce Watson
#################################################

# Matrix Stack Library
# Instance Variables
global A
global stack
stack = []
A = [[1, 0, 0, 0], 
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

def gtInitialize():
    #init to an identity matrix
    global A 
    global stack
    stack = []
    A = [[1, 0, 0, 0], 
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    stack.insert(0, A)

def gtPushMatrix():
    #duplicates current matrix on top of the stack
    global stack
    global A
    stack.insert(0, A)


def gtPopMatrix():
    global stack
    if (stack and len(stack) > 1):
        stack.pop()
    else:
        print("Error: Cannot use pop() on an empty stack")

def gtTranslate(x, y, z):
    # 3x3 matrix
    global A
    # 3x4 matrix
    Y = [[1, 0, 0, x], 
         [0, 1, 0, y],
         [0, 0, 1, z],
         [0, 0, 0, 1]]
    A = matmult(A, Y)
    stack[0] = A

    
def gtScale(x, y, z):
    global A
    Y = [[x, 0, 0, 0], 
         [0, y, 0, 0],
         [0, 0, z, 0],
         [0, 0, 0, 1]]
    A = matmult(A, Y)
    stack[0] = A


def gtRotateX(theta):
    global A
    Y = [[1, 0, 0, 0],
        [0, cos(radians(theta)), -sin(radians(theta)), 0],
        [0, sin(radians(theta)), cos(radians(theta)), 0],
        [0, 0, 0, 1]]
    A = matmult(A, Y)
    stack[0] = A


def gtRotateY(theta):
    global A
    Y = [[cos(radians(theta)), 0, sin(radians(theta)), 0],
         [0, 1, 0, 0],
         [-sin(radians(theta)), 0, cos(radians(theta)), 0],
         [0, 0, 0, 1]]
    A = matmult(A, Y)
    stack[0] = A


def gtRotateZ(theta):
    global A
    Y = [[cos(radians(theta)), -sin(radians(theta)), 0, 0],
         [sin(radians(theta)), cos(radians(theta)), 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    A = matmult(A, Y)
    stack[0] = A

def gtGetMatrix():
    global A
    return A


def print_ctm():
    # for i in range(len(A[0])):
    #     print A[i]
        
    
    for j in range(len(stack[0][0])):
        print stack[0][j]
    print "\n"
    
#function for matrix multiplication
def matmult(a,b):
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]