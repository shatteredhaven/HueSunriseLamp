#!/usr/bin/python2

#-------------------------------------------------------------------------------
# Name:         Hue Weather Lamp
#
# Details &
# instructions: forthcoming
#
# Author:       shatteredhaven
# 
# Created:      April 2013
# 
#-------------------------------------------------------------------------------

import sys; sys.path.append("/home/pi/phue-master")

import urllib2
from xml.dom import minidom
import time

from phue import Bridge

# change to your IP address
b = Bridge('192.168.x.x')

# turn the lamp on and make it as dim as possible
b.set_light(1,'on', True)
b.set_light(1, 'bri', 1)
b.set_light(1, 'hue', 9977)

# define the 5 different color transitions. Each variable runs for three minutes.
orangeC =  {'transitiontime' : 1800, 'on' : True, 'bri' : 50, 'hue' : 9977}
orangeyellowC =  {'transitiontime' : 1800, 'on' : True, 'bri' : 100, 'hue' : 9980}
yellowC =  {'transitiontime' : 1800, 'on' : True, 'bri' : 150, 'hue' : 13390}
yellowwhiteC =  {'transitiontime' : 1800, 'on' : True, 'bri' : 200, 'hue' : 15191}
whiteC =  {'transitiontime' : 1800, 'on' : True, 'bri' : 254, 'hue' : 38375} 

# begin sunrinse lamp. This will last 
b.set_light(1, orangeC)
print 'orange'
time.sleep(180)
b.set_light(1, orangeyellowC)
print 'orange yellow'
time.sleep(180)
b.set_light(1, yellowC)
print 'yellow'
time.sleep(180)
b.set_light(1, yellowwhiteC)
print 'yellow white'
time.sleep(180)
b.set_light(1, whiteC)
time.sleep(180)
print 'white'

#delay for 1 hour then turn lamp off
time.sleep(3600)
b.set_light(1,'on', False)
