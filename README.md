HueSunriseLamp
==============

Philips Hue lamp controlled by python script to simulate a sunrise. 


Overview of the Philips Hue Sunrise Lamp: 
A python script (using a phue library) turns on the lamp and gradually increases the brightness and changes the color to mimic a sunrise lamp. There are five total colors, each lasts three minutes for a total of fifteen minutes from start to finish. 

The python code will turn itself off after one hour (45 minutes after the maximum brightness). 

The colors the lamp uses are:
- orange
- yellow-orange
- yellow
- light yellow
- white


Additional information and photos can be found here: FORTHCOMING

Requirements: 
- Hue Lamps: http://www.meethue.com/en-US
- python (this program is written in 2.7): http://www.python.org/download/
- Philips Hue python library: https://github.com/studioimaginaire/phue
- computer capable of running cron or similar job scheduling function (ex. schtasks in Windows) 

Contents: 
- HueSunriseLamp.py - python script for the sunrise lamp
- HueSunriseLamp.sh - shell script to execute python script (only needed if there are issues with getting cron to execute the python script)
- SunriseCron - cron job example

Installation: 
A more detailed description of this project can be found here: FORTHCOMING

Distribution: 
feel free to copy/modify/change/distribute at will! 

Note: the last color (whiteC in the python code) has a greenish-tint to it at the beginning of the transition. This is something I plan to tweak when I get more time. 