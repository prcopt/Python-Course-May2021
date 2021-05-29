"""
EXERCISE SET S02AQ01
Using the starting and ending values of your car’s odometer,calculate its mileage - as a function

Inputs: Starting and Ending Values on odometer, both as positve integers (end value to be > start value)
        Total Fuel consumed , a positive number

"""
def mileage(start,end,fuel):
    return (end-start)/fuel

def get_inputs():
    start = int(input("Key in Odometer Value at start:"))
    end   = int(input("Key in Odometer Value at End  :"))
    fuel_consumed = float(input("Key in amount of fuel consumed:"))                   
    return start,end,fuel_consumed


def main():
    start,end,fuel = get_inputs()
    fc = mileage(start,end,fuel)
    print("Odometer Start Value:",start,
          "\nOdometer End Value  :",end,
          "\nFuel Consumed :",fuel,
          "\nMileage :",fc)

main()
