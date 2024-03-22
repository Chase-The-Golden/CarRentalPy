from datetime import datetime

class Rent:
    def __init__(self):
        self.__available = 15
        pass

    def displayAvailable(self):
        return self.__available

    def rentAvailable(self):
        cars_to_rent = -1
        while cars_to_rent < 0 or cars_to_rent > self.__available:
            print("How many cars would you like to rent? Type 0 to cancel.\nCars availble: ", self.__available)
            cars_to_rent = int(input())
            if cars_to_rent < 0 or cars_to_rent > self.__available:
                print("INVALID INPUT")
            elif cars_to_rent == 0:
                print("Cancelled renting.")
                break
        self.__available -= cars_to_rent
        self.__renttime = datetime.now().strftime("%b %d, %Y\t%I:%M:%S %p")
        
    def bill(self, timeframe):
        print(self.__renttime)

class Customers():
    def __init__(self):
        pass

    def requestCars():
        pass

    def returnCars():
        pass

test = Rent()
test.rentAvailable()