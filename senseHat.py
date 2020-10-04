#!/usr/bin/python
#
#from sense_hat import SenseHat
from sense_emu import SenseHat
from configuration.colorDefinitions import green
from configuration.colorDefinitions import cyan
from configuration.colorDefinitions import red
from configuration.ledImageArrays import alarm_attention
from configuration.ledImageArrays import gr_flag
from sensors import sensors
from system import system_info
from time import sleep

sense = SenseHat()

###########
#
# Configuration
#
###########

# settings for the display functions
timeColor = green
humidityColor = cyan
tempColor = red
infoColor = white
speed = 0.1

'''
Functions
'''
def joystic_event(event):
    #print(event)
    if (event.action) == 'pressed':
        # trigger when pressed
        if (event.direction == 'middle'):
            # pressing will show 2 exclamation marks
            sense.set_pixels(alarm_attention)
        elif (event.direction == 'up'):
            # up and down will trigger the temperature
            sensors.display_temp(tempColor,speed)
        elif (event.direction == 'down'):
            # up and down will trigger the temperature
            system_info.display_system_info(infoColor,speed)
        elif (event.direction == 'right'):
            # left and right will trigger the humidity
            sensors.display_humidity(humidityColor,speed)
        elif (event.direction == 'left'):
            # left and right will trigger the humidity
            sensors.display_humidity(humidityColor,speed)
        # just for some seperation
        sleep(1)
    elif (event.action) == 'held':
        # something as a placeholder for held
        sense.set_pixels(gr_flag)
        sleep(2)
    elif (event.action) == 'released':
        sense.clear()
    else:
        print('error, no action in event ?')


'''
Main run loop
'''
while True:
    # orientation and motion detection
    sensors.sense_orientation()
    sensors.sense_shaking()
    # checking for joystic inputs
    for event in sense.stick.get_events():
        joystic_event(event)
    else:
        sensors.display_time(timeColor,speed,"military")

# Originally used for event detection, gave trouble when mixed with While True
#sense.stick.direction_any = joystic_event
