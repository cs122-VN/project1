# ----------------------------------------------------------------
# CS 112 - Project
# Student: Vincent Nguyen
# Notes: Project was tested with Python 3.8 / IDE Spyder 4.1.4
# ----------------------------------------------------------------

# ---------------- Begin Project Code ----------------------------
# declare general variables
PI = 3.14159
to_square_meter = 0.00064516

# Greeting user and get input
print("Welcome to CS 112")
name = input("What's your name? ")
input_time = input("What is the time in seconds? ")
input_time = int(input_time)

# Calculate the hours / minutes /seconds
hours = input_time//3600
#seconds = input_time % 360
minutes = input_time // 60 - (hours * 60)

seconds = input_time - (hours * 3600 + minutes * 60)

# output time in hrs mins secs format
print('The time is ' +  str(hours)+'h',str(minutes)+'m',str(seconds)+'s')

# Calculate the angles of the hours / mins / seconds in degrees and convert to radians
# degrees
hand_hour = round(((input_time/3600)/12)*360,5)
hand_mins = round(((seconds/60)+minutes)*6,5)

#hand_secs = round(hand_mins * 6,5)
hand_secs = round(seconds * 6,5)
# radians conversion
radian_hour = round((hand_hour *(PI/180)),5)
radian_mins = round((hand_mins *(PI/180)),5)
radian_secs = round((hand_secs *(PI/180)),5)

# Output the angles of three hands
print('The angles of the three hands are ' + str(hand_hour) + ' ' + str(hand_mins) +  ' ' + str(hand_secs) + ' degrees ' + 'or ' + str(radian_hour) + ' ' + str(radian_mins) + ' ' + str(radian_secs) + ' radians')

# Calculate the angles between the hour hand and the minutes hand
hours_min_angle = round(abs(hand_mins - hand_hour),5)
radians_hours_mins_angle = round(hours_min_angle *(PI/180),5)

print('The angle between the hour hand and the minutes hand is ' + str(hours_min_angle) + ' degrees or ' + str(radians_hours_mins_angle) + ' radians')

diameter = input('What is the diameter of the clock in inches? ')

# Calculate the area of the slice between hour hand and minute hand and output result
radius = float(diameter)/2
square_inches = round( (hours_min_angle / 360) * PI * (radius **2),5)
square_meter = round(square_inches * to_square_meter,5)

print('The area of the slice between the hour hand and the minutes hand is ' + str(square_inches) + ' sq. inches or ' + str(square_meter) + ' sq. meters')

# get the new diameters in inches and recalculate new angle between the hour hand and minute hand
new_diameter = input('What is the new diameter of the clock in inches? ')
radius = float(new_diameter)/2
new_angle = round((square_inches * 360) / (PI * (radius ** 2)),5)
radian_new_angle = round(new_angle * (PI/180), 5)

print('The new angle between the hour hand and the minutes hand must be ' + str(new_angle) + ' degrees or ' + str(radian_new_angle) + ' radians')

#print('The new angle between the hour hand and the minutes hand must be {:.5f} {:.5f}'.format(new_angle, radian_new_angle) )

# output end greeting
print('Have a good day ' + name + '!')

# ---------------- End Project Code -----------------------------
