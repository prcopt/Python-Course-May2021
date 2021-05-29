"""
EXERCISE SET S02Q02
     - Using the starting and ending values of your car’s odometer, 
            and the measure of fuel consumed, 
            calculate the number of stops one should make for refuelling 
            while travelling from Bangalore to Goa, 
            a distance of 560 kms.

2 methods are provided: calculation using math library and the other using basic operators.

"""
##### function to calculate mileage

def mileage(start,end,fuel):
    return (end-start)/fuel

##### Function to calculate fuel consumption (Mileage) km/ltr for car
def get_fuel_consumption():
    input_data = input("Key in Start and End values of Odometer Readings with comma separating the numbers:")
    (x,y)=input_data.split(",")
    start_value = int(x)
    end_value = int(y)
    if start_value >= 0 and end_value >= 0 and start_value < end_value:
        fuel_consumed_in_ltr = float(input("Enter Fuel consumed in Liters:"))
        if fuel_consumed_in_ltr > 0:
         return mileage(start_value,end_value,fuel_consumed_in_ltr)
        else:  
            print("There was no fuel to consume or quantity cannot be negetive!!")
    else:
        print("Give meaningful odometer readings seperated by comma!!")

##### Function to print results - Dash board
def result_board(fc,fr,tc,fs,stop):
    print(" Fuel Consumption of Car  :",fc ,"Kms/Ltr\n",
          "Fuel required for journey:",fr ,"Ltrs\n",
          "Tank Capacity            :",tc ,"Ltrs\n",
          "Fuel in tank at start    :",fs ,"Ltrs\n",
          "No of stops for refil    :",stop)
    return
                 
                 
        
###### Calculating fuel required for journey

fc = get_fuel_consumption()
dist_to_goa = 560
fuel_required_for_goa = dist_to_goa/ fc
tank_capacity = int(input("Enter the Fuel Tank Capacity in Liters as integer:"))
fuel_at_start = float(input("Enter Fuel in Tank in Liters at Start: "))


# calculation by using  math function
print("\nMETHOD-1: BY USE OF MATH LIBRARY\n")
import math
no_of_stops_for_refils = math.ceil((fuel_required_for_goa - fuel_at_start)/tank_capacity)
result_board(fc,fuel_required_for_goa,tank_capacity,fuel_at_start,no_of_stops_for_refils)

# calculation by using remainder operator
print("\nMETHOD-2: BY USE OF REMAINDER OPERATOR\n")
if fuel_at_start < fuel_required_for_goa:
    no_of_stops_for_refils = int((fuel_required_for_goa - fuel_at_start)/tank_capacity)
    if (fuel_required_for_goa - fuel_at_start)%tank_capacity > 0 : 
        no_of_stops_for_refils += 1
result_board(fc,fuel_required_for_goa,tank_capacity,fuel_at_start,no_of_stops_for_refils)
    
