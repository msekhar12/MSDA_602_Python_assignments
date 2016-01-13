class CarEvaluation:
    'Contains the cars evaluation information'
    carCount = 0
    def __init__(self, brand, price, safety):
        self.brand = brand
        self.price = price
        self.safety = safety
        
        self.price_numeric = 0

        if price == "High": self.price_numeric = 3
        if price == "Med": self.price_numeric = 2
        if price == "Low": self.price_numeric = 1
        
        CarEvaluation.carCount += 1

    def showEvaluation(self):
        print "The %s has a %s price and it's safety is rated a %d" % (self.brand, self.price, self.safety)

    def __repr__(self):
        return "%s" % (self.brand)
    



def sortbyprice(L, Order):
    '''Sorts a list of CarEvaluation Objects by price'''

    if isinstance(L, list):
        if Order.upper() == "ASC": return sorted(L, key = lambda x: x.price_numeric)
        else:
            if Order.upper() == "DES": return sorted(L, reverse=True, key = lambda x: x.price_numeric)
            else: print "Incorrect order is supplied. Order must be Asc or Des"
    else: print "List object is NOT supplied"


def searchforsafety(L, Safety):
    '''searches Safety and returns True/False, if present'''

    if isinstance(L, list):
       for i in range(len(L)):
          if L[i].safety == Safety: return True
       return False
    else: print "Supply list object as input"


if __name__ == "__main__":
        eval1 = CarEvaluation("Ford","High", 2)
        eval2 = CarEvaluation("GMC","Med", 4)
        eval3 = CarEvaluation("Toyota","Low", 3)

        print "Car Count = %d" % CarEvaluation.carCount

        eval1.showEvaluation()
        eval2.showEvaluation()
        eval3.showEvaluation()

        L = [eval1, eval2, eval3]

        print sortbyprice(L, "asc")
        print sortbyprice(L, "des")
        
        print searchforsafety(L, 2); 
        print searchforsafety(L, 1); 
