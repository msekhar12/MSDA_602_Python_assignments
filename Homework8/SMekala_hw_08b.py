#Analyzing circles.png image

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
from skimage.data import camera
from skimage.filters import threshold_otsu
from skimage import io, filters
import os
import sys

def clear_scr():
    '''Clears the screen
    '''
    #To accommodate all Operating systems, I am using 2 commands
    try:
        unused_var = os.system('clear')
        unused_var = os.system('cls')
    except:
        pass
    
clear_scr()

print "You are analyzing the circles.png file"
print "                      -----------"
print "\nMake sure that you have this file in the current working directory."
print "\n\nIn this analysis, a series of images are displayed..."
print "\nJust close the image, when you want the program to proceed further..."

e = raw_input("\n\nPress ENTER to proceed now...")



matplotlib.rcParams['font.size'] = 9
try:
   image = ndi.imread('circles.png')
except:
    print "The circles.png file is not found. Closing the program..."
    sys.exit()

#Setting the threshold to 100.
thresh = 100

#Eliminating all the pixels which are less than the threshold (100)
#This is needed to eliminate the image overlap
filtered_array = image > thresh

#Preparing to plot the original and filtered images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')


ax2.imshow(filtered_array, cmap=plt.cm.gray)
ax2.set_title('Filtered')
ax2.axis('off')

plt.show()

#Labeling the objects in the filtered image
labels, count = ndi.label(filtered_array)

#Printing the number of regions found
print '%s regions found' % (count)

#displaying the image (filtered) with center of mass
fig, (ax3) = plt.subplots(1, figsize=(8, 8))

ax3.imshow(filtered_array,cmap=plt.cm.gray)
ax3.set_title('Filtered image with center points')

t = ndi.measurements.center_of_mass(filtered_array, labels, list(range(1,count+1)))
t_arr = np.array(t)

#Getting the center of mass coordinates
x = list(t_arr[:,1])
y = list(t_arr[:,0])

#Ovrelay the center of mass coordinates onto the filtered image
plt.scatter(x=x,y=y, c='r', s=100)


plt.show()

#Clear the screen
clear_scr()

print "\n\n"
print "The analysis of circles.png file is given below:"
print "                ----------- "
print "\n\nA total of %d objects found" % count

print "\n\nThe center of mass points in the form of (x,y) coordinates for the %d objects in the image are given below:" % count
print "    X              Y"
print "----------    ----------"
for a, b in zip(x,y):
    print "%10f    %10f" % (a,b)

