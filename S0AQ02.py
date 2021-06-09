"""S0AQ02
Like everyone I too enjoyed watching Taj Hotel from Mumbai’s Gateway of India. 
When I stood at the Gateway of India, I saw that the 
top of Taj Hotel’s tower was at an angle of elevation of 25 degrees.
I then walked to the security guard near the gate of Taj Hotel and 
noticed that the top of the tower was at an angle of elevation of 65 degrees. 
The security guard informed me that the Tower was about 100 yards from the gate.

Write a program to find the height of Taj Hotel’s tower and 
the distance between Gateway of India and Taj Hotel’s entrance.
.

"""

# Implement the helper functions here

import math

alpha = 65  # Angle of Elevation from Gate of Tajmahal 
beta  = 25    # Angle of Elevation from Gateway of India
dist_gate = 100 # Distance from Gate to Tower

height = dist_gate * math.tan(math.radians(alpha))
dist = (height/math.tan(math.radians(beta)) - dist_gate)
print( "Distance between Gateway of India and Taj Hotel's entrance:",round(dist,0),"Yards")
        
