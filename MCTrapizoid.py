# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:27:06 2023

@author: be
"""

# -*- coding: utf-8 -*

def MCint(f, a, b, n):

    """
    Parameters
    ----------
    f : TYPE function
    f returns a float between a and b
    a : TYPE float
    DESCRIPTION. lower limit
    b : TYPE float
    DESCRIPTION. upper limit
    n : TYPE int
    DESCRIPTION, number of random points to take in the box
    Returns
    -------
    integral of f from a to b
    """
    from random import random
    import numpy as np
    # random returns a random number betwee 0 and 1
    
    maxF = -2
    
    area = 0
    saveX = []
    saveY = []
    for i in range(n):

        # generate a random point in the boxc
        # x between a and b
        # z between 0 and maxF
        randNoX = random()*(b-a) + a
        randNoY = random()*maxF
        saveX.append(randNoX)
        saveY.append(randNoY)


    if randNoY <= f(randNoX): area += 1

    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    print(min(saveX), max(saveX))
    print(min(saveY), max(saveY))
    return(integral)


def trap(f,a,b,n):
    """
    
    
    Parameters
    ----------
    f : TYPE: Float
    DESCRIPTION: Function of 1 variable x
    a : TYPE: float
    DESCRIPTION: left side of intergrate region
    b : TYPE: Float
    DESCRIPTION: Right side of integrate region
    n : TYPE Integer
    DESCRIPTION: How many Trapazoid to use
    
    Returns
    -------
    Intergral
    
    """
    import numpy as np
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    sumInt = 0
    for i in range((n+1)):
        if i == 0 or i ==n:
            sumInt += f(x[i])/2
        else:
            sumInt += f(x[i])
    integral = h*sumInt
    return(integral)


if __name__ == "__main__":

    # import numpy as np
    # import matplotlib.pyplot as plt
    def f(x):
        return x**2
    
    area = MCint(f, 0.5, 2., 50000)
    
    print(round(area, 2))
    print(f'int {area: 0.2f}')
    
    area2 = trap(f, 0, 1, 100)
    print(area2)
    