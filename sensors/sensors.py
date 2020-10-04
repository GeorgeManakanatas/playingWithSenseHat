from sense_hat import SenseHat
#from sense_emu import SenseHat
from configuration.ledImageArrays import black_screen
from configuration.ledImageArrays import alarm_attention
import time

sense = SenseHat()

def sense_orientation():
    # get accelerations
    acceleration = sense.get_accelerometer_raw()
    # get rounded values
    x=round(acceleration['x'], 0)
    y=round(acceleration['y'], 0)
    z=round(acceleration['z'], 0)
    # detect orientation and apply proper rotation of matrix
    if (x == 1):
        sense.set_rotation(270)
    elif (x == -1):
        sense.set_rotation(90)
    elif (y == 1):
        sense.set_rotation(0)
    elif (y == -1):
        sense.set_rotation(180)
    else:
        sense.set_rotation(0)

def sense_shaking():
    # get accelerations
    acceleration = sense.get_accelerometer_raw()
    # get absolute values
    x = abs(acceleration['x'])
    y = abs(acceleration['y'])
    z = abs(acceleration['z'])
    # if any are greater than gravity
    if x > 1.2 or y > 1.2 or z > 1.2:
        sense.set_pixels(configuration.ledImageArrays.alarm_attention)
        print("x={0} y={1} z={2}".format(x, y, z))
    else:
        sense.set_pixels(black_screen)

def display_time(color,speed,preference):
    # get local time
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min

    # convert to non military time
    # not clear right now how to display in a practical fashion as message

    # prepare minutes for display
    if ( minute < 10 ):
        minutes = "0"+str(minute)
    else:
        minutes = str(minute)
    # prepare hours for display
    if ( hour < 10 ):
        hours = "0"+str(hour)
    else:
        hours = str(hour)
    # build the display string
    displayMessage = hours+":"+minutes
    # display information
    sense.show_message(displayMessage, text_colour=color, scroll_speed=speed)

def display_temp(color,speed):
    # get temp reading
    temp = sense.get_temperature()
    # build display string
    displayMessage = str(int(temp))+"C"
    # display information
    sense.show_message(displayMessage, text_colour=color, scroll_speed=speed)

def display_humidity(color,speed):
    # get humidity reading
    humidity = sense.get_humidity()
    # build display string
    displayMessage = str(int(humidity))+"%"
    # display information
    sense.show_message(displayMessage, text_colour=color, scroll_speed=speed)
