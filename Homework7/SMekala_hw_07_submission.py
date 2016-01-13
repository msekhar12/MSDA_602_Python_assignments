import sys
import math
import os
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit

class numeric_list:
    'Class for numeric list'
  
    def __init__(self, num_list):
        self.ls = list()
        for self.i in range(len(num_list)):
            try:
                self.ls.append(float(num_list[self.i]))
            except:
                print "Data exception:"
                sys.exit()

    def average(self):
        self.run_total = float(0)
        self.n = len(self.ls)
        for self.i in range(self.n):
            self.run_total = self.run_total + self.ls[self.i]
        return self.run_total/self.n

    def sd(self):
        self.avg = numeric_list.average(self)
        self.sd_sq = 0
        self.n = len(self.ls)
        for self.i in range(self.n):
            self.sd_sq = self.sd_sq + ((self.avg - self.ls[self.i]) * (self.avg - self.ls[self.i]))
        if self.n <= 1:
            print "Error in finding Std. Dev. \n The supplied input has only 1 element"
        else:
            self.sd = math.sqrt(self.sd_sq/ (self.n-1))
            return self.sd

    def __repr__(self):
        return str(self.ls)


def clear_scr():
    '''Clears the screen
    '''
#To accommodate all Operating systems, I am using 2 commands
    try:
        unused_var = os.system('clear')
        unused_var = os.system('cls')
    except:
        pass
    



def read_file():
    '''Reads the supplied file, and returns a 2 element dictionary of numeric list objects'''

    clear_scr()

    s = raw_input("\nEnter File location. To quit, press ENTER on blank input\n ==>")    
    while True:
        if s == '':
            print '\n\nGood Bye'
            sys.exit()
        
        try:
            fsock = open(s)
        except:
            print "\nThe given file location is incorrect. Enter file's location (complete path) again or EXIT to quit\n"
            s = raw_input("==>")
            continue
        else:
            break

    try:
            file_lines = fsock.readlines()
            fsock.close()
    except:
            print "\nUnable to read file. Terminating the program.\n"
            sys.exit()
       
    else:

            l = [(i.rstrip("\n")).split(",")for i in file_lines]
            body_list = list()
            brain_list = list()
            

            for j in range(1,len(l)):
                body_list.append(l[j][1])
                brain_list.append(l[j][2])

            return {"body_weights":body_list,"brain_weights":brain_list}

def get_regression_components(x,y):
    '''Takes 2 numeric lists, and returns averages, and std deviations,
       and corff of correlation via a dict object
    '''
    n = len(x)

    #Converting the input lists to numeric lists (numeric_list objects)

    x = numeric_list(x)
    y = numeric_list(y)

    #Getting the averages and std.deviations of x and y numeric_list objects
    x_avg = x.average()
    x_sd  = x.sd()

    y_avg = y.average()
    y_sd  = y.sd()

    #Finding the coeff of corr
    temp_sum = float(0)
    for i in range(n):
        temp_sum = temp_sum + (((x.ls[i] - x_avg)/x_sd) * ((y.ls[i] - y_avg)/y_sd))
    coeff_of_corr = temp_sum/(n-1)

    #Return a dict. object with means, std. deviations and coeff of corr
    return ({"x_avg":x_avg,"x_sd":x_sd,"y_avg":y_avg,"y_sd":y_sd,"coeff_of_corr":coeff_of_corr})


def func(x, a, b):
    return a * x + b


def manual_regression(x, y):
    #Calling the Get_regression_components function with the above 2 lists as input
    brain_weights = x
    body_weights = y
    regression_components = get_regression_components(brain_weights, body_weights)

    #Getting the output of Get_regression_components into variables
    #for readibility
    brain_weights_avg = regression_components["x_avg"]
    brain_weights_sd = regression_components["x_sd"]

    body_weights_avg = regression_components["y_avg"]
    body_weights_sd =  regression_components["y_sd"]


    coeff_of_corr = regression_components["coeff_of_corr"]
    
    #Finding the slope of the regression line
    slope = coeff_of_corr * body_weights_sd / brain_weights_sd

    #Finding the intercept of the regression lone 
    intercept = body_weights_avg  - (slope * brain_weights_avg)
    print "\n"
    print "(1). Regular derivation using least squares method"
    print "--------------------------------------------------"
    print "Using manual least squares derivation method we obtained the following linear model:"

    print_regression_line(slope, intercept)


def stats_regression(x, y):

    #from scipy import stats
    #import numpy as np
    #x = np.random.random(10)
    #y = np.random.random(10)

    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    print "\n"
    print "(2). scipy's stats.linregress() method"
    print "--------------------------------------"

    print "Using scipy's stats.linregress() function, obtained the following linear model:"
    print_regression_line(slope, intercept)


def curve_fit_regression(x, y):

    # Executing curve_fit to fit the data
    popt, pcov = curve_fit(func, x, y)
    
    # popt returns the best fit values for parameters of
    # the given model (func).
    print "\n"
    print "(3). scipy's curve_fit() method"
    print "-------------------------------"
    print "Using curve_fit(), obtained the following linear model"
    slope = popt[0]
    intercept = popt[1]
    print_regression_line(slope, intercept)



def print_regression_line(slope, intercept):
    #Printing the regression line.
    #Purposefully avoided the usage of format (like %+f), to enhance readibility
    #of the equation

    if intercept > 0:
         print "               bo = %f * br + %f" % (slope, intercept)
    if intercept < 0:
        intercept = -1 * intercept
        print "                bo = %f * br - %f" % (slope, intercept) 
    if intercept == 0:
       print "                 bo = %f * br" % (slope) 


if __name__ == '__main__':
    import timeit
    
    #Read the file first!!
    animal_weights_dict =  read_file()

    #Getting the body and brain weights into two lists
    body_weights = animal_weights_dict["body_weights"]
    brain_weights = animal_weights_dict["brain_weights"]


    body_weights_arr = np.array(body_weights)
    brain_weights_arr = np.array(brain_weights)
    x = brain_weights_arr.astype(float)
    y = body_weights_arr.astype(float)


    loops = 1

    #Calling the manual_regression() function
    setup = "from __main__ import manual_regression, brain_weights, body_weights"
    print "\n"
    print "Linear models of brain and body data set"
    print "------ ------ -- ----- --- ---- ---- ---"
    

    
    print "Runtime: %s loops = %s seconds" %(loops, timeit.timeit("manual_regression(brain_weights, body_weights)", setup = setup, number = loops)) 


    #Calling the stats_regression() function, which uses the stats package of scipy
    setup = "from __main__ import stats_regression, x,y"
    print "Runtime: %s loops = %s seconds" %(loops, timeit.timeit("stats_regression(x, y)", setup = setup, number = loops)) 


    #Calling the curve_fit_regression() function in the scipy's optimize pakage
    setup = "from __main__ import curve_fit_regression, x, y"
    print "Runtime: %s loops = %s seconds" %(loops, timeit.timeit("curve_fit_regression(x, y)", setup = setup, number = loops)) 

    #The regression on the file brainandbody.csv is showing that the manual computation is the fastest.

    print "\n\nThe runtimes shown above confirms that the stats.linregress() method is the slowest"

    print "\nLet us try the execution on 1000000 random observations for brain and body..."
    print "We will generate 1000000 random observations for brain and body, and apply the linear regression methods to check which method is efficient"
    print "\n\n"
    print "Linear models of brain and body with 1000000 random observations"
    print "------ ------ -- ----- --- ---- ---- ------- ------ ------------"

    print "\nHere are the performance results on 1000000 random observations:"
    

    x_arr = np.random.random(1000000)
    y_arr = np.random.random(1000000)

    x_list = list(x_arr)
    y_list = list(y_arr)

    #Calling the manual_regression() function on random data
    setup = "from __main__ import manual_regression, x_list, y_list"
    print "Runtime: %s loops = %s seconds" %(loops, timeit.timeit("manual_regression(x_list, y_list)", setup = setup, number = loops)) 


    #Calling the stats_regression() function, which uses the stats package of scipy. Called this on random data
    setup = "from __main__ import stats_regression, x_arr,y_arr"
    print "Runtime: %s loops = %s seconds" %(loops, timeit.timeit("stats_regression(x_arr, y_arr)", setup = setup, number = loops)) 


    #Calling the curve_fit_regression() function which uses the scipy's optimize pakage. Called this on random data
    setup = "from __main__ import curve_fit_regression, x_arr, y_arr"
    print "Runtime: %s loops = %s seconds" %(loops, timeit.timeit("curve_fit_regression(x_arr, y_arr)", setup = setup, number = loops))
    print "\n"
    print "Conclusion:"
    print "-----------"
    print "As the number of observations grow, the curve_fit() and stats.linregress() seems to outperform the manual computation. The stats.linregression() method has the best performance(least run-time)"
