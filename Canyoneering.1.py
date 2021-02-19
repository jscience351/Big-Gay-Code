
import numpy as np
import matplotlib as plt
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import math
import random

class canyoneering:
    def __init__(self, length, width, height):
        self.length = length #determines x-dimension of base starting surface
        self.width = width #determines y-dimension of base starting surface
        self.height = height #determines relative intensity of hill formation ('z-dimension')

#TODO create initial surface
    #surface represented by grid (matrix/array) of numbers (each number representing height)
    #numbers are ranomly spaced in 

    def create_surface(self): #create initial surface to 'erode'
        veclength = self.length * self.width #create vector with enough numbers to fill a length*width matrix
        mean, sd = 0, self.height #height is standard deviation around mean height of zero
        heightlist = np.random.normal(mean, sd, veclength) #samples the proper number of random heights, around a mean of 0, with sd defined by 'height'
        heightlist = np.around(heightlist, 2) #rounds the heights to the nearest two decimal places
        heightlist = heightlist.reshape((self.width, self.length)) #turns the heights into a matrix with the proper dimensions for length and width
        print(heightlist)
        xlist = [] #creates empty list to hold x values (correspond to width)
        ylist = [] #creates empty list to hold y values (correspond to length)
        zlist= [] #creates empty list to hold z values (correspond to height)
        for y in range(self.length): #for each y value from 0 to the length...
            for x in range(self.width): #for each x value from 0 to the width...
                xlist.append(x) #add that x value in to a list of x values
                ylist.append(y) #add that y value to a list of y values
                z = heightlist[x,y] #find the z value (already in the matrix) for that [x,y] pair
                print('Z: ', str(z))
                zlist.append(z) #add that z value to the list of z values
        print('XLIST: ', xlist)
        print('LENXLST', str(len(xlist)))
        print('YLIST: ', ylist)
        print('LENYLIST: ', str(len(ylist)))
        print('ZLIST: ', zlist)
        print('LENZLIST: ', str(len(zlist)))
    
    #TODO turn length and width into meshgrid
        lengthlist, widthlist = np.arange(self.length), np.arange(self.width) #create arrays containing all possible numbers in length and width values
        meshlength, meshwidth = np.meshgrid(lengthlist, widthlist) #create meshgrid for those length and width arrays
        print('MESHLENGTH:')
        print(meshlength)
        print('MESHWIDTH:')
        print(meshwidth)

    #TODO select random points out of length, width and height 
        num_sampled = math.floor(len(xlist)/4) #use around 1/4 of the points in the matrix as sample points for extrapolation
        sample_points = random.sample(range(len(xlist)), num_sampled) #knowing the number of points to be sampled, chose the sample point indices
        print('SAMPLE POINTS: ', sample_points)
        xlist, ylist, zlist = np.asarray(xlist), np.asarray(ylist), np.asarray(zlist) #turn the x,y, and z lists into np arrays
        xsamples, ysamples, zsamples = xlist[[sample_points]], ylist[[sample_points]], zlist[[sample_points]] #choose the sample points from the arrays based on predetermined indices (same for each)
        print('XSAMPLES: ', xsamples)
        print('XYZsamples done')
        print('XSAMPLES TYPE: ', type(xsamples))
        print('YSAMPLES TYPE: ', type(ysamples))
        print('ZSAMPLES TYPE: ', type(zsamples))
        gridz0 = griddata((xsamples, ysamples), zsamples, (meshwidth, meshlength)) #apply griddata to extrapolate the rest of the height values
        print('GRIDZ0: ', gridz0)
        fig = plt.figure()
        ax = plt.axes(projection= '3d') #create 3D projection
        ax.plot_surface(meshwidth, meshlength, gridz0) #plot it using meshwidth as X, meshlength as Y, and gridz0 as Z
        plt.show()

    

#INPUTS
length = 100 #how long is the surface to be created?
width = 100 #how wide is the surface to be created?
height = 5 #how tall will the peaks/depressions in the surface be?

#INITIATE CLASS
canyonobject = canyoneering(length, width, height)

#RUN METHODS
canyonobject.create_surface() #creates the blank, contoured surface to eroded