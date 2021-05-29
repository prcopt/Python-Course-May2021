"""
EXERCISE SET S02Q01
Using the starting and ending values of your car’s odometer,calculate its mileage

Inputs: Starting and Ending Values on odometer, both as positve integers separated by ','
        Total Fuel consumed , a positive number

"""
def mileage(start,end,fuel):
    return (end-start)/fuel


input_data = input("Key in Start and End values of Odometer Readings with comma separating the numbers:")
(x,y)=input_data.split(",")
start_value = int(x)
end_value = int(y)
if start_value >= 0 and end_value >= 0 and start_value < end_value:
    fuel_consumed_in_ltr = float(input("Enter Fuel consumed in Liters:"))
    if fuel_consumed_in_ltr > 0:
        print("Mileage given by car: ",mileage(start_value,end_value,fuel_consumed_in_ltr),"Miles/litre")
    else:  
        print("There was no fuel to consume or quantity cannot be negetive!!")
else:
    print("Give meaningful odometer readings seperated by comma!!")
