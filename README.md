# Laveer-Enterprises
This project was developed to assist our robotics team in controlling our underwater robot. 

The program requires various libraries and hardware in order to run. Please verify that your unit is able to support and install these plugins and hardware.

Python Libraries needed: 
 - pygame
 - serial
 - math

Hardware Required:
 - Arduino Micro Controller
 - RS232 Serial to usb cable
 - PS3/PS4 controller with usb compatibility


 How it Works:

 Python Side:
 The python side is in charge of launching a user interface which displays all the information being sent from both the microcontroller and the usb controller. 
 Once it collects the values of the joystick positions, it then maps these to a specific number on a scale of 1 to 255 which is the values for the motor speed.
 This is then compiled into a string such as: ["255/", "128/", "1/", "255/", "40/"].

 Arduino Side:
 Once the Python Side compiles this string it is then sent over to the arduino side where the code will then break it back apart and associate the values with 
 whichever motor or sensor needs to be controlled. 
