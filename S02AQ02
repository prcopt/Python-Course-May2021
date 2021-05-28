"""
EXERCISE SET S02AQ02
Re-write the earlier question of S02Q02 using functions :

- Using the starting and ending values of your car’s odometer, and the measure of fuel consumed, 
- calculate the number of stops one should make for refuelling while travelling from Bangalore to Goa, 
- a distance of 560 kms.


Inputs: Starting and Ending Values on odometer, both as positve integers (end value to be > start value)
        Total Fuel consumed , a positive number

"""
def mileage(start,end,fuel): #Computation of Mileage
    return (end-start)/fuel

def get_inputs():  # Collect inputs for mileage computation
    start = int(input("Key in Odometer Value at start:"))
    end   = int(input("Key in Odometer Value at End  :"))
    fuel_consumed = float(input("Key in amount of fuel consumed:"))
    return start,end,fuel_consumed

def get_tank_details(): # Collect Futel Tank Details
    capacity = int(input("Key-in Fuel Tank Capacity:"))
    fuel_left = float(input("Fuel left in tank at start of journey:"))
    return capacity,fuel_left

def no_of_stops(fuel_at_start,distance,fc,capacity): # Computation of Number of Stops
    fuel_required_for_trip = distance/fc
    if fuel_at_start < fuel_required_for_trip:
        no_of_stops_for_refils = int((fuel_required_for_trip - fuel_at_start)/capacity)
        if (fuel_required_for_trip - fuel_at_start)%capacity > 0 : 
            no_of_stops_for_refils += 1  
        return no_of_stops_for_refils

def print_results(fc,fr,tc,fs,stop,distance): # Printing Results
    print(" Fuel Consumption of Car  :",fc ,"Kms/Ltr\n",
          "Distance to Travel       :",distance,"Kms\n",
          "Fuel required for journey:",fr ,"Ltrs\n",
          "Tank Capacity            :",tc ,"Ltrs\n",
          "Fuel in tank at start    :",fs ,"Ltrs\n",
          "No of stops for refils    :",stop)
    return

def main():
    start,end,fuel = get_inputs()
    fc = mileage(start,end,fuel)
    capacity,fuel_left = get_tank_details()
    distance = 560
    stops = no_of_stops(fuel_left,distance,fc,capacity)
    print_results(fc,distance/fc,capacity,fuel_left,stops,distance) 

main()
          
