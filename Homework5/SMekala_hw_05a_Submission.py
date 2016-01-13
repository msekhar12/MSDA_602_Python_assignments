import sys
import math
import os

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


if __name__ == '__main__':

    #Read the file first!!
    animal_weights_dict =  read_file()

    #Getting the body and brain weights into two lists
    body_weights = animal_weights_dict["body_weights"]
    brain_weights = animal_weights_dict["brain_weights"]

    #Calling the Get_regression_components function with the above 2 lists as input
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

    #Printing the regression line.
    #Purposefully avoided the usage of format (like %+f), to enhance readibility
    #of the equation
    print "\n\nThe linear regression equation is given below:\n"
    if intercept > 0:
         print "               bo = %f * br + %f" % (slope, intercept)
    if intercept < 0:
        intercept = -1 * intercept
        print "                bo = %f * br - %f" % (slope, intercept) 
    if intercept == 0:
       print "                 bo = %f * br" % (slope) 


    
    
