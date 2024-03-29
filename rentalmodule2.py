from datetime import datetime as dt

class Rental:
    # Constructor
    def __init__(i):
        i.__available = 15  # Available cars
        i.__rented = 0      # Rented amount
        i.__total = 0       # Total price
        i.__HR = 7.99       # Hourly
        i.__DL = 129.99     # Daily
        i.__WK = 549.99     # Weekly

    # NOTE: s = self
    # Display available cars for rent
    def dispAvailable(s):
        return s.__available
    
    # Rent the cars & log time and inventory
    def rentAvailable(s, numcars):
        s.__rented = numcars
        s.__available -= s.__rented
    
    # Choose rental mode between hourly, daily, and monthly
    def rentMode(s, numcars, mode, renttime):
        s.__timediff = dt.now() - renttime
        s.__timespan = s.__timediff.total_seconds()
        s.__strtime = renttime.strftime("%b %d, %Y\t%I:%M:%S %p")
        s.__rate = 0

        # Charge rate based on mode
        if mode == 1:
            s.__timespan //= 3600   # Hourly
            s.__rate = s.__HR
        elif mode == 2:
            s.__timespan //= 86400  # Daily
            s.__rate = s.__DL
        elif mode == 3:
            s.__timespan //= 604800 # Weekly
            s.__rate = s.__WK
        
        # Base charge if rented for less than 1 span of chosen time
        s.__base = 0 if s.__timespan > 0 else 1

        s.__total = numcars * s.__rate * (s.__timespan + s.__base)  # Calculate the total price
    
    # Update inventory & generate bill
    def rentReturn(s, numcars):
        # Add cars back to inventory
        s.__available += numcars
        # Receipt
        print("RETURNED. THANK YOU FOR USING X RENTALS!")
        print("========================================")
        print("--------     Rental Receipt     --------")
        print("Rent Time\t\t", s.__strtime)
        print("Rented For\t\t", s.__timediff)
        print("Total\t\t\t", s.__total)

class Customer:
    # Constructor
    def __init__(i, id, numcars, rate, obj):
        i.__id = id
        i.__rented = numcars
        i.__rate = rate
        i.__rentobj = obj
        i.__rentdt = dt.now()

    # Customer request cars
    def custReq(s):
        s.__rentobj.rentAvailable(s.__rented)
        print("REQUEST MADE. YOUR ID IS #: ", s.__id)
    
    # Customer returns cars
    def custRet(s):
        s.__rentobj.rentMode(s.__rented, s.__rate, s.__rentdt)
        s.__rentobj.rentReturn(s.__rented)