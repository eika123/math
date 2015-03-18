import numpy as np
#from numpy import pi, sin, cos, sqrt, exp, linspace  # numpy faster on vectors
from math import pi, sin, cos, sqrt, exp # math module faster on scalars

N = 30
x = linspace(0, pi, N)


# N argument in function and global N above are in different scopes
def trapezoidal_method(f, a, b, N):
    # exercise: turn the loop into an inner product
    # look up numpy.inner
    # gives faster summing, but more memory usage
    """ Integrate f from a to b using the trapezoidal method """

    x = linspace(a, b, N)
    
    s = 0
    #x.shape[0] is the number of elements in x
    for k in xrange(x.shape[0]):
        s = s + (x[k+1] - x[k])*(f(x[k+1]) - f(x[k]))
    s = s*0.5
    return s

def rectangle_rule(f, a, b, N):
    """ integrate f with rectangles """
    # use no vectors, saves memory
    # slow loops
    dx = (b - a)/float(N)
    x_ = a
    x  = a + dx 

    s = 0
    while x <= b:
        x_mid = (x + x_)/2.0
        s += f(x_mid)*dx # add term to Riemann sum
        
        # update x and x_
        x += dx
        x_ = x

    return s


def f(x):
    # test example, compare to hand computation
    return sin(x) + 3*cos(x)

def f(x):
    # has no closed form integral!
    return exp(-x**2)

# more exercises for numerical integration:
# look up scipy.integrate for quadrature rules and ODE integrators.
# These are implemented in compiled languagues,
# but work out of the box in python
#
# look up numpy.vectorize for turning ordinary python functions 
# into vectorized functions that are evaluated very fast on arrays
#
#
# more ideas: look up scipy.fft and do compression of sound files,
# relevant in the physics curriculum.
# see e.g http://www.uio.no/studier/emner/matnat/math/MAT-INF2360/v15/kompendium/applinalgpython.pdf
# for a quite comprehensive introduction
#
# use the implemented integration rules to calculate fourier series
# possibilities are infinite!

