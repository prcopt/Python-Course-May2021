""" S04Q01
Simulation of Ethanol tank level based action required.
- When the tank is more than 80% full, it should raise an alarm to close the valve.
- When the tank is less than 20% full, it should send an SMS to buy more liquid.
- The total tank capacity is 900 litres.

"""

def do_action(present, redmark, bluemark):
    # Compare present with redmark and bluemark
    # to decide the appropriate action
    if present > redmark :
        print("Alarm to Close Valve")
    else:
        if present < bluemark :
            print("Send SMS to order Ethanol")
        else:
            print("All going fine")
    return

def get_current_level():
    integer = int(input("Current level of Ethanol:")) # Get value from user
    return integer

# Main starts from here
capacity = 900
high = 0.8*capacity # calculate using "capacity" variable
low  = 0.2*capacity # calculate using "capacity" variable
level = get_current_level()
do_action(level, high, low)
