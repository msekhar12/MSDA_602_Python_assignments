#Analyzing objects.png image

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
from skimage import io, filters
import os
import sys

import skimage.morphology as morph

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

print "You are analyzing the peppers.png file"
print "                      -----------"
print "\nMake sure that you have this file in the current working directory."
print "\n\nIn this analysis, a series of images are displayed..."
print "\nJust close the image, when you want the program to proceed further..."

e = raw_input("\n\nPress ENTER to proceed now...")


matplotlib.rcParams['font.size'] = 9

try:
  image = ndi.imread('peppers.png')
except:
  print "The peppers.png file is not found. Closing the program..."
  sys.exit()

#Applying the gaussian filter, to blurr the image
filtered_array = filters.gaussian_filter(image, sigma = 2, multichannel=False)

#Filtering out the pixels whose values are less than the mean of all the pixels
filtered_array = filtered_array > filtered_array.mean()


#Plotting the original and filtered image
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))

l = len(image.shape)
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')

filtered_array[:] = ndi.binary_opening(filtered_array,np.ones((np.ones(l) * 2)))
filtered_array[:] = ndi.binary_closing(filtered_array,np.ones((np.ones(l) * 2)))

ax2.imshow(filtered_array, cmap=plt.cm.gray)
ax2.set_title('filtered')
ax2.axis('off')


plt.show()

#Counting the objects...
labels, count = ndi.label(filtered_array)
print '%s regions found' % (count)

#Plotting the filtered image with center of mass coordinates
fig, (ax3) = plt.subplots(1, figsize=(8, 8))

ax3.imshow(filtered_array,cmap=plt.cm.gray)
ax3.set_title('Filtered image with center points')

t = ndi.measurements.center_of_mass(filtered_array, labels, list(range(1,count+1)))
t_arr = np.array(t)


x = list(t_arr[:,1])
y = list(t_arr[:,0])



plt.scatter(x=x,y=y, c='r', s=100)


plt.show()

clear_scr()

#printing final analysis report
print "\n\n"
print "The analysis of peppers.png file is given below:"
print "                ----------- "
print "\n\nA total of %d objects found" % count

print "\n\nThe center of mass points in the form of (x,y) coordinates for the %d objects in the image are given below:" % count
print "    X              Y"
print "----------    ----------"
for a, b in zip(x,y):
    print "%10f    %10f" % (a,b)
