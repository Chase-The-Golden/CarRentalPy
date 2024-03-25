from datetime import datetime

# Class for renting cars
class Rent:
    # Constructor
    def __init__(self):
        self.__available = 15
        self.__rentamt = 0
        self.__total = 0
        self.__HOURLYRATE = 7.99
        self.__DAILYRATE = 129.99
        self.__WEEKLYRATE = 549.99

    # Instructions specificaly stated to create a method of displaying available cars
    def displayAvailable(self):
        return self.__available

    # Storing rent time in variable (and subtracting cars)
    def rentAvailable(self, cars_to_rent):
        self.__rentamt = cars_to_rent
        self.__available -= self.__rentamt
        self.__renttime = datetime.now()
        self.__rentstrtime = datetime.now().strftime("%b %d, %Y\t%I:%M:%S %p")

    # Typically, I would calculate this in only one method but the instructions insists on creating multiple methodS
    def rentHourly(self, cars_rented):
        # Testing calculating prices as of 1:42 3/23/2024
        '''
        __testdelta = datetime(2024, 3, 23, 2, 28)
        __testdate = __testdelta - self.__renttime
        __testhours = __testdate.total_seconds() // 3600
        '''
        self.__timediff = datetime.now() - self.__renttime
        self.__diffhours = self.__timediff.total_seconds() // 3600      # 3600s = 1h
        self.__hours = 0 if self.__diffhours > 0 else 1                 # Base charge of 1 hour for any returns after less than 1 hour
        self.__total = cars_rented * self.__HOURLYRATE * (self.__diffhours + self.__hours)

    def rentDaily(self, cars_rented):
        self.__timediff = datetime.now() - self.__renttime
        self.__diffdays = self.__timediff.total_seconds() // 86400     # 86400s = 1d
        self.__days = 0 if self.__diffdays > 0 else 1                 # Base charge of 1 hour for any returns after less than 1 day
        self.__total = cars_rented * self.__DAILYRATE * (self.__diffdays + self.__days)
    
    def rentWeekly(self, cars_rented):
        self.__timediff = datetime.now() - self.__renttime
        self.__diffweeks = self.__timediff.total_seconds() // 604800    # 604800s = 1w
        self.__weeks = 0 if self.__diffweeks > 0 else 1                 # Base charge of 1 hour for any returns after less than 1 week
        self.__total = cars_rented * self.__WEEKLYRATE * (self.__diffweeks + self.__weeks)
        
    # Update inventory on return and generate final bill
    def rentReturn(self, amount):
        self.__available += amount
        # Rent Receipt
        print("THANK YOU FOR USING X CAR RENTAL!")
        print("Final Bill")
        print("Rented At\t\t\t\tRental Period\t\t\tTotal")
        print(self.__rentstrtime,"\t\t",self.__timediff,"\t\t",self.__total)

# Customer class
class Customer:
    # Constructor
    def __init__(self, id, rentrate, rentobject):
        self.__id = id
        self.__carsrented = 0
        self.__rentrate = rentrate
        self.__rentobj = rentobject

    # Make rent request
    def custRequest(self):
        cars_to_rent = -1
        cars_left = self.__rentobj.displayAvailable()   # Update cars left
        while cars_to_rent < 0 or cars_to_rent > cars_left:
            print("Cars availble: ", cars_left)
            try:
                cars_to_rent = int(input("How many cars would you like to rent? Type 0 to go back: "))
            except:
                cars_to_rent = -1
            ################ DEMO PURPOSES TO EXPLICITLY SHOW IN PDF - COMMENT OUT IN FINAL BUILD
            # print("How many cars would you like to rent? Type 0 to go back: ", cars_to_rent)
            ################
            if cars_to_rent < 0 or cars_to_rent > cars_left or cars_left == None:
                print("INVALID INPUT")
            # Go Back / Cancel
            elif cars_to_rent == 0:
                return True
            
        self.__carsrented = cars_to_rent
        self.__rentobj.rentAvailable(self.__carsrented)
        print("RENT MADE. YOUR ID IS: ", self.__id)
        return False

    # Return car method
    def custReturn(self):
        # Calculate rent depending on rental mode
        if self.__rentrate == 1:
            self.__rentobj.rentHourly(self.__carsrented)
        elif self.__rentrate == 2:
            self.__rentobj.rentDaily(self.__carsrented)
        elif self.__rentrate == 3:
            self.__rentobj.rentWeekly(self.__carsrented)
        
        self.__rentobj.rentReturn(self.__carsrented)