class CarEvaluation:
    'Contains the cars evaluation information'
    carCount = 0

    #These dictionaries will help us to assign numeric values to categorical values like vhigh etc.
    
    buying_index = {"v-high":4,"vhigh":4, "high":3, "med":2, "low":1}
    maint_index =  {"v-high":4, "vhigh":4, "high":3, "med":2, "low":1}
    doors_index = {"2":2, "3":3, "4":4, "5-more": 5, "5more": 5}
    persons_index = {"2":2, "4":4, "more":5}
    lug_boot_index = {"small":1, "med":2, "big":3}
    safety_index = {"low":1, "med":2, "high":3}
    
    def __init__(self, buying, maint, doors, persons, lug_boot, safety, category):
        self.buying = buying
        self.maint=maint
        self.doors=doors
        self.persons=persons
        self.lug_boot=lug_boot
        self.safety=safety        
        self.category = category

        #The following try/except blocks will handle incorrect data to the dictionaries defined
        
        try:
            self.buying_numeric = CarEvaluation.buying_index[str(self.buying).lower()]
        except:
            print "\n\nData Error: Buying must be one of v-high, high, med, low. \n\nBut you entered: " + str(self.buying) + ", which, is invalid. \n Skipping this record, and proceeding with the rest..."
            self.buying_numeric = -99
            raise ValueError()
            
        try:
            self.maint_numeric = CarEvaluation.maint_index[str(self.maint).lower()]
        except:
            print "\n\nData Error: Maintenance must be one of v-high, high, med, low. \n\nBut you entered: " + str(self.maint) + ", which, is invalid. \n Skipping this record, and proceeding with the rest..."
            self.maint_numeric = -99
            raise ValueError()
        
        try:
            self.doors_numeric = CarEvaluation.doors_index[str(self.doors).lower()]
        except:
            print "\n\nData Error: Doors must be one of 2, 3, 4 or 5more or 5-more. \n\nBut you entered:" + str(self.doors) + ", which, is invalid. \n Skipping this record, and proceeding with the rest..."
            self.doors_numeric = -99
            raise ValueError()
        
        try:
            self.persons_numeric = CarEvaluation.persons_index[str(self.persons).lower()]
        except:
            print "\n\nData Error: Persons must be one of 2, 4 or more. \n\nBut you entered: " + str(self.persons) + ", which, is invalid. \n Skipping this record, and proceeding with the rest..."
            self.persons_numeric = -99
            raise ValueError()
        

        try:
            self.lug_boot_numeric = CarEvaluation.lug_boot_index[str(self.lug_boot).lower()]
        except:
            print "\n\nData Error: Luggage boot must be one of small/med/big. \n\nBut you entered: " + str(self.lug_boot) + ", which, is invalid. \n Skipping this record, and proceeding with the rest..."
            self.lug_boot_numeric = -99
            raise ValueError()

        try:
            self.safety_numeric = CarEvaluation.safety_index[str(self.safety).lower()]
        except:
            print "\n\nData Error: Safety must be one of low/med/high. \n\nBut you entered: " + str(self.safety) + ", which, is invalid. \n Skipping this record, and proceeding with the rest..."
            self.safety_numeric = -99
            raise ValueError()

        CarEvaluation.carCount += 1

    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s" % (self.buying, self.maint, self.doors, self.persons, self.lug_boot, self.safety, self.category)

def write_file(cars, row_count):
    '''Writes a list to a file
       Parms:
       cars: A list of carsevaluation objects
       row_count: Number of carsEvaluation objects contained in cars parm, to be written to a file

       Returns: None
    '''

    
    print "\n\nEnter out put file name\n"
    print "By default, the file will be created in the current directory\n"
    print "You may enter absolute file name also."
    print "To cancel, press ENTER"

    out_file = raw_input("Output file name==> ")
    if out_file.upper() == '':
        return None
    
    append_choice = raw_input("\n\n Do not want to append the output to the file? \n\n YES/NO \n\n NO is the default.\n\n  Your choice please ==>")
    if append_choice.upper() == "YES" or append_choice.upper() == "Y":
      try:
        write_file_sock = open(out_file, 'a')
      except:
        print "Problem in opening the file in Write mode. Check the path/permissions"
    else:
      try:  
        write_file_sock = open(out_file, 'w')
      except:
        print "Problem in opening the file in Write mode. Check the path/permissions"
        
    for i in range(row_count):
        write_file_sock.write(str(cars[i])+"\n")

    write_file_sock.close()

    print "\n\n Successfully written the output to the file: " + out_file + "\n\n"
    

def sort_car_objects(cars, sort_choice, asc_desc_choice):
     '''
       Sorts a list of carEvaluation objects, based on a supplied attribute of carsEvaluation object.

       Parms:
          cars: A list of carsEvaluation objects
          sort_choice: A numeric value between 1 to 6
            If sort_choice is 1 then the cars list is sorted by buying attribute
            If sort_choice is 2 then the cars list is sorted by maint attribute
            If sort_choice is 3 then the cars list is sorted by doors attribute
            If sort_choice is 4 then the cars list is sorted by persons attribute
            If sort_choice is 5 then the cars list is sorted by lug_boot attribute
            If sort_choice is 6 then the cars list is sorted by safety attribute
          asc_desc_choice:
            "ASC" To sort the data in ascending order
            "DESC" To sort the data in descending order

       The function returns a sorted carsEvaluation objects list 
       
     '''


     if asc_desc_choice == "ASC":
         
         if sort_choice == 1:
             return sorted(cars, key = lambda x: x.buying_numeric)
            
         if sort_choice == 2:
             return sorted(cars, key = lambda x: x.maint_numeric)

         if sort_choice == 3:
             return sorted(cars, key = lambda x: x.doors_numeric)

         if sort_choice == 4:
             return sorted(cars, key = lambda x: x.persons_numeric)


         if sort_choice == 5:
             return sorted(cars, key = lambda x: x.lug_boot_numeric)

         if sort_choice == 6:
             return sorted(cars, key = lambda x: x.safety_numeric)


     if asc_desc_choice == "DESC":
         if sort_choice == 1:
             return sorted(cars, reverse= True, key = lambda x: x.buying_numeric)
            
         if sort_choice == 2:
             return sorted(cars, reverse= True, key = lambda x: x.maint_numeric)

         if sort_choice == 3:
             return sorted(cars, reverse= True, key = lambda x: x.doors_numeric)

         if sort_choice == 4:
             return sorted(cars, reverse= True, key = lambda x: x.persons_numeric)


         if sort_choice == 5:
             return sorted(cars, reverse= True, key = lambda x: x.lug_boot_numeric)

         if sort_choice == 6:
             return sorted(cars, reverse= True, key = lambda x: x.safety_numeric)



def clear_scr():
    '''Clears the screen
    '''
    try:
        unused_var = os.system('clear')
        unused_var = os.system('cls')
    except:
        pass
    

def read_cars_file():
    '''Reads the supplied file, and prepares a carsEvaluation objects list'''

    clear_scr()

    s = raw_input("\nEnter File location. To quit, type EXIT and press Enter\n ==>")    
    while True:


        if s.upper() == 'EXIT': sys.exit()
        
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
            cars = list()
            junk_cars = 0
            for j in range(len(l)):
                buying = l[j][0]
                maint = l[j][1]
                doors = l[j][2]
                persons = l[j][3]
                lug_boot = l[j][4]
                safety = l[j][5]
                category = l[j][6]
                
                
                try:
                     car_obj = CarEvaluation(buying, maint, doors, persons, lug_boot, safety, category)
                except:
                     junk_cars += 1
                     continue
                else:
                    cars.append(car_obj)

            if junk_cars > 0: print "\n\nNumber of observations skipped, due to incorrect format: %d \n\n" % (junk_cars)
            return cars


def search_cars_file(cars):
 '''
       Always searchs the words given in the home work. Not dynamic search
 '''
 while True:   
    clear_scr()
    print "\n\n\n                SELECT one of the following searches "
    print "                ------ --- -- --- --------- -------- "
    print "\n\n(Only these CANNED Searches are available, as per the HOME WORK. \nDynamic Search is NOT implemented yet):"
    print "\n 1. Search high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order"
    print "\n 2. Search 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more"
    print "\n                * * * * * Exit - Just press ENTER * * * * * "
    
    choice = raw_input("\nEnter your search choice (1 or 2) ==>")
    if choice == '': return None
    
    try:
        if int(choice) <1 or int(choice) > 2:
            print "You can select only 1 or 2 or 3 only"
            continue
    except:
            print "You can select only 1 or 2 or 3 only"
            continue
    searched_cars = list()
    if choice == "1":
        
       for i in range(len(cars)):
             if re.search(r'vhigh|high', cars[i].buying, re.IGNORECASE) and re.search(r'vhigh|high', cars[i].maint, re.IGNORECASE) and re.search(r'vhigh|high',cars[i].safety,re.IGNORECASE):
                          searched_cars.append(cars[i])

       searched_cars = sorted(searched_cars, key = lambda x: x.doors_numeric)

    
    

    if choice == "2":

       for i in range(len(cars)):
           if re.search('vhigh', cars[i].buying, re.IGNORECASE) and re.search('med', cars[i].maint, re.IGNORECASE) and cars[i].doors_numeric == 4 and cars[i].persons_numeric >= 4:
                               searched_cars.append(cars[i])


       
    for i in range(len(searched_cars)):
      print searched_cars[i]


    print "\n\n Do you want to SAVE these results to a file?"
    print "                ----"
    print "\nYour choice can be (Yes/No). \n Press ENTER to EXIT"
    write_choice = raw_input("\n Your choice please==>")
    if write_choice.upper() == "Y" or write_choice.upper() == "YES":
        write_file(searched_cars,len(searched_cars))
    break

    

if __name__ == "__main__":
    import re
    import sys
    import os

    cars = read_cars_file()
    


    while True:
                print "\n\n     MAIN ANALYSIS MENU   "
                print "     ---- -------- ----   \n"
                print " 1. Fetch/Sort Data    \n"
                print " 2. Search Data \n"
                print " 3. Read another file  \n"
                print " 4. Exit \n"
                choice = raw_input("Enter your choice ==>")

                
                if choice == str(4):
                    print "\nGood bye"
                    sys.exit()

                if choice == str(1):
                  clear_scr()
                  while True:

                            print "       Fetch/Sort Data      "
                            print "       ---------------      "
                            row_count = raw_input("\n\n  * Enter How many rows to fetch?\n  * To get all rows, press ENTER. \n  * For main menu, enter MAIN. \n  * To quit, enter EXIT \n\n Your choice please ==>")
                            #print row_count

                            if row_count.upper() == "EXIT":
                                print "Good Bye"
                                sys.exit()
                                
                            if row_count.upper() == "MAIN":
                                clear_scr()
                                break

                            if row_count != '':
                              try:
                                row_count = int(row_count)
                              except:
                                print "\nEnter Numeric values as row count"
                                continue

                            if row_count <= 0:
                                print "You cannot enter negative value or zero as row count"
                                continue

                            if row_count == '':
                                row_count = len(cars)

                            print "\n Do you want to SORT the data?"
                            print "                ---- \n"
                            print " \n****            Enter YES or NO       **** "
                            print "                      ---    --  "
                            print "\n NO is the default. \n\n You may also press ENTER on blank input, to say NO"
                            order_choice = raw_input("   \n   Your Choice please ==>")

                            while True:
                                    if order_choice.upper() == 'Y' or order_choice.upper() == "YES":
                                        print "       SORT CHOICES "
                                        print "       ---- ------- "
                                        print "\n 1. Buying"
                                        print " 2. Maintenance"
                                        print " 3. Doors"
                                        print " 4. Persons"
                                        print " 5. Luggage Capacity"
                                        print " 6. Safety"
                                        print "\n To exit, type EXIT"
                                        

                                        sort_choice = raw_input("Enter your choice (1, 2, 3, 4, 5, 6). \n\nType EXIT to go back to previous menu. ==>")
                                        if re.match(r'\s*exit\s*',sort_choice, re.IGNORECASE): break

                                        #if sort_choice.upper() == "EXIT": break

                                        try:
                                            if int(sort_choice) < 1 or int(sort_choice) > 6:
                                                print "You entered, incorrect choice. Please enter any choice between 1 to 6, as per the below menu"
                                                continue
                                        except:
                                            print "You entered, incorrect choice. Please enter any choice between 1 to 6, as per the below menu"
                                            continue

                                        sort_choice = int(sort_choice)
                                        
                                        asc_desc_choice = raw_input("In which order (Asc/Desc). Defaulat is Asc==>")

                                        if asc_desc_choice.upper() == "D" or asc_desc_choice.upper() == "DESC":
                                            asc_desc_choice = "DESC"
                                        else:
                                            asc_desc_choice = "ASC"
                                                
                                        cars_sorted = sort_car_objects(cars, sort_choice, asc_desc_choice)
                                         
                                        for k in range(row_count):
                                             print cars_sorted[k]
                                        print "\n\n Do you want to WRITE the OUTPUT to a file?"
                                        print "                -----     ------"
                                        print " \n****            Enter YES or NO       **** "
                                        print "                      ---    --  "
                                        print "\n NO is the default. \n\n You may also press ENTER on blank input, to say NO"
                                        write_choice = raw_input("   \n   Your Choice please ==>")
                                        if write_choice.upper() == "YES" or write_choice.upper() == "Y":
                                            write_file(cars_sorted, row_count)

                                        break
                                    else:
                                        for k in range(row_count):
                                            print cars[k]
                                        print "\n\n Do you want to WRITE the OUTPUT to a file?"
                                        print "                -----     ------"
                                        print " \n****            Enter YES or NO       **** "
                                        print "                      ---    --  "
                                        print "\n NO is the default. \n\n You may also press ENTER on blank input, to say NO"
                                        write_choice = raw_input("   \n   Your Choice please ==>")


                                        if write_choice.upper() == "YES" or write_choice.upper() == "Y":
                                            write_file(cars, row_count)

                                        break
                            break                                        
                                                  
                else:
                    if choice == str(3):
                        read_cars_file()
                    else:
                        if choice == str(2):
                           search_cars_file(cars)
                        else:
                           print "Incorrect choice. Select proper choice \n"
