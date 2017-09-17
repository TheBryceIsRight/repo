# Drawing Routines, like OpenGL

from matlib import *

#Instance Variables
global vertice_list
global current_mat
global right
global left
global top
global bottom
global far
global near
global vertice_list
global isOrthographic
global fov
global near_persp
global far_persp
global ortho_matrix
global width
global height
global k

vertice_list = []
width = 800
height = 800

#scaling transformation matrix from class

# Here is how those new methods are integrated with the (a) part of the project:
# 1. You do all the Scales, Rotates, Translates and so on on your matrix stack. 
# 2. You get the current CTM (there are multiple ways to go about it and gtGetMatrix is a great way to do it)
# 3. When you want to draw a point on the screen, you get your point in a 3D space by doing CTM * [x, y, z] 
# (x, y, z are coordinates of the point , given to you in gtVertex()) and then apply either gtOrtho() 
# or gtPerspective() to the result of the (CTM * [x, y, z]). 

def gtOrtho(_left, _right, _bottom, _top, _near, _far):
    #Assigning of global variables
    global right
    global left
    global top
    global bottom
    global far
    global near
    global ortho_matrix
    global persp_matrix
    global isOrthographic
    
    left = _left
    right = _right
    top = _top
    bottom = _bottom
    near = _near
    far = _far
    
    x_scalar = width/(right - left)
    x_trans = -left
    y_scalar = height/(top - bottom)
    y_trans = -bottom

    ortho_matrix =  [[x_scalar, 0, 0, x_trans],
                     [0, y_scalar, 0, y_trans],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]

    
    isOrthographic = True
    pass
    
def gtPerspective(_fov, _near, _far):
    
    #Instance variables
    global fov
    global near_persp
    global far_persp
    global persp_matrix
    global isOrthographic
    global k
    fov = _fov
    far_persp = _far
    far = _far
    near_persp = _near
    near = _near
    isOrthographic = False
    
    #Math for the perspective matrix
    k = math.tan(fov/2)
    pass

def gtBeginShape():
    global vertice_list
    vertice_list = []
    pass

def gtEndShape():
    
    #the function where it happpens
    #two transormations - 1 to take it from 0:800 to -400:400, 2nd one is projection
    
    for i in range(1,len(vertice_list), 2):
        #Points are represented through the following formula:
        #ortho || persp * (CTM * point)
        pt1 = vertice_list[i-1]
        pt2 = vertice_list[i]
            
        if(isOrthographic == True):
            print "Point 1 : " + str(pt1[0][0]) + ", " + str(pt1[1][0]) + ", " + str(pt1[2][0])
            ctm = gtGetMatrix()            
            pt1 = matmult(ctm, pt1)
            pt2 = matmult(ctm, pt2)
            print "Point 1 after CTM: " + str(pt1[0][0]) + ", " + str(pt1[1][0]) + ", " + str(pt1[2][0])
            pt1[0][0] = (width/(right - left)) * (pt1[0][0] - left)
            pt1[1][0] = (height/(top - bottom)) * (pt1[1][0] - bottom)
            pt2[0][0] = (width/(right - left)) * (pt2[0][0] - left)
            pt2[1][0] = (height/(top - bottom)) * (pt2[1][0] - bottom)
            print "Point 1 after Ortho: " + str(pt1[0][0]) + ", " + str(pt1[1][0]) + ", " + str(pt1[2][0])
            line(pt1[0][0], pt1[1][0], pt1[2][0], pt2[0][0], pt2[1][0], pt2[2][0])
        else:
            print "Point 1 : " + str(pt1[0][0]) + ", " + str(pt1[0][1]) + ", " + str(pt1[0][2])
            pt1 = matmult(gtGetMatrix(), pt1)
            print "Point 1 after CTM: " + str(pt1[0][0]) + ", " + str(pt1[0][1]) + ", " + str(pt1[0][2])
            pt1[0][0] =  (pt1[0][0] + k) * (width/(2*k))
            pt2 = matmult(gtGetMatrix(), pt2)
            pt1[0][1] =  (pt1[0][0] + k) * (height/(2*k))
            pt2 = matmult(gtGetMatrix(), pt2)
            print "Point 1 after Perspective: " + str(pt1[0][0]) + ", " + str(pt1[0][1]) + ", " + str(pt1[0][2]) + "\n"
        
    
    pass
    
def getPointValues(pt1):
    return [[pt1[0]], [pt1[1]], [pt1[2]]]


def gtVertex(x, y, z):
    #is apparently also known as gtAddVertex
    #used for adding vertices to the global list of points
    vertice_list.append([[float(x)], [float(y)], [float(z), 1]])
    
    pass