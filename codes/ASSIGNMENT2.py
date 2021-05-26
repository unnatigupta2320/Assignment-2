import numpy as np
import matplotlib.pyplot as plt


#Quadrilateral vertices
M = np.array([0,0])
I = np.array([3.5,0])
S=np.array([5.18,6.27])
T=np.array([2.42,9.03])

def print_coordinates_of_triangle_MIS(m,i,s):
    """m, i and s are lengths of the sides of a triangle MIS"""

    M= (0, 0) # coordinates of vertex M

    I= (s, 0) # coordinates of vertex I
    

    S_x = i * Decimal(i**2 + s**2 - m**2) / (2 * i * s)
    S_y = Decimal(i**2 - S_x**2).sqrt() # square root

    S = (float(S_x), float(S_y)) # coordinates of vertex S

    # print
    vertices = zip(["M = ", "I= ", "S = "], [M, I, S])
    print('\n'.join([v[0] + str(v[1]) for v in vertices]))

    # test -- print coordinates of triangle given sides of length 6.5, 8.14, 3.5
    print_coordinates_of_triangle_MIS(6.5,8.14,3.5)

#Generating all lines
x_MI = line_gen(M,I)
x_IS = line_gen(I,S)
x_ST = line_gen(S,T)
x_TI = line_gen(T,I)

#Plotting all lines
plt.plot(x_MI[0,:],x_MI[1,:],label='$MI$')
plt.plot(x_IS[0,:],x_IS[1,:],label='$IS$')
plt.plot(x_ST[0,:],x_IS[1,:],label='$ST$')
plt.plot(x_TI[0,:],x_IS[1,:],label='$TI$')

plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.1), M[1] * (1 - 0.1) , 'M')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 - 0.2), I[1] * (1 - 0.1) , 'I')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 - 0.2), S[1] * (1 - 0.1) , 'S')
plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 - 0.2), T[1] * (1 - 0.1) , 'T')

Drawing_C = plt.Circle(( 0 , 0 ), 4,fill=False)
axes.add_artist( Drawing_C )
plt.plot(4, 0, 'o')
plt.text(4 * (1 + 0.04),0.1 , 'E1') 
plt.plot(0, 4, 'o')
plt.text(0.1 ,4.1, 'E2') 



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')