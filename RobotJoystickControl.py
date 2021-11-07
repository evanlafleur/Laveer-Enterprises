import pygame
import serial
import io
import time
import easygui

# Define some colors
BLACK	= (   0,   0,   0)
WHITE	= ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
PURPLE = (130, 0, 130)

# Pulse Width Modulation & Debugger Mode  default = off
programMode = 0

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
	def __init__(self):
		self.reset()
		self.font = pygame.font.Font(None, 20)

	def printline(self, screen, textString):
		textBitmap = self.font.render(textString, True, BLACK)
		screen.blit(textBitmap, [self.x, self.y])
		self.y += self.line_height
		
	def reset(self):
		self.x = 10
		self.y = 10
		self.line_height = 15
		
	def indent(self):
		self.x += 10
		
	def unindent(self):
		self.x -= 10
	
	
pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("RobotJoystickControl")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# Pyserial stuff for Arduino
#"""
portNum = 256
portList = []
for i in range(portNum):
	try:
		ser = serial.Serial(i, 9600)
		portList.append(ser.portstr)
		ser.close()
	except:
		pass
portList.append("None")
comPort= easygui.choicebox("Choose Port:", "Ports", portList)
serialConnected = False
try:
	serial = serial.Serial(comPort, 9600)
	time.sleep(0.5)
	print (serial.name)
	serialConnected = True
	time.sleep(1)
except:
	print ("Serial error...")
	
pulseWidthModulation = easygui.choicebox("Choose Program Mode:", "Program Mode Select Menu", ("Pulse On", "Pulse Off"))
programMode = easygui.indexbox(msg="Choose Program Mode:", title="Program Mode Select Menu", choices=('Pulse Width OFF', 'Pulse Width ON', 'Debugger Mode'), image="bla")
print (pulseWidthModulation)
if (pulseWidthModulation == 1):
	print ("pulseWidth ON")
elif (pulseWidthModulation == 0):
	print ("pulseWidth OFF")
elif (pulseWidthModulation == 2):
	print ("Starting Debugger Mode...")
else:
	print ("Error... pulseWidth OFF")
if (serialConnected == True and serial.isOpen()):
	serial.write(chr(pulseWidthModulation).encode('latin-1'))

wait = True
if (serialConnected == True and serial.isOpen()):
	while(wait):
		time.sleep(.5)
		print(serial.inWaiting())
		while(serial.inWaiting() > 0):
			arduinoString = serial.readline()
			try:
				print (arduinoString.decode())
			except:
				print ("Error decoding string")
			#arduinoCharacters = serial.read(serial.inWaiting())
			#print (arduinoCharacters.decode())
		time.sleep(.5)
		if (serial.inWaiting() == 0):
			wait = False
			print ("python flushing...")
			serial.flush()
			serial.flushOutput()
			serial.flushInput()
#"""
# -------- Main Program Loop -----------
while done==False:
	# EVENT PROCESSING STEP
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
		
		# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		if event.type == pygame.JOYBUTTONDOWN:
			print("Joystick button pressed.")
		#if event.type == pygame.JOYBUTTONUP:
			#print("Joystick button released.")
		
		
	# DRAWING STEP
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(WHITE)
	textPrint.reset()

	# Get count of joysticks
	joystick_count = pygame.joystick.get_count()
	
	textPrint.printline(screen, "Number of joysticks: {}".format(joystick_count) )
	textPrint.indent()
	
	
	# For each joystick:
	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()
	
		textPrint.printline(screen, "Joystick {}".format(i) )
		textPrint.indent()
	
		# Get the name from the OS for the controller/joystick
		name = joystick.get_name()
		textPrint.printline(screen, "Joystick name: {}".format(name) )
		
		# Usually axis run in pairs, up/down for one, and left/right for
		# the other.
		axes = joystick.get_numaxes()
		textPrint.printline(screen, "Number of axes: {}".format(axes) )
		textPrint.indent()
		
		for i in range( axes ):
			axis = (joystick.get_axis( i ) * -60) + 90
			textPrint.printline(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
		textPrint.unindent()
			
		buttons = joystick.get_numbuttons()
		textPrint.printline(screen, "Number of buttons: {}".format(buttons) )
		textPrint.indent()
		almostExplode1 = False
		almostExplode2 = False
		for i in range( buttons ):
			button = joystick.get_button( i )
			textPrint.printline(screen, "Button {:>2} value: {}".format(i,button) )
			if (i == 0 and button == 1):
				almostExplode1 = True
			if (i == 1 and button == 1):
				almostExplode2 = True
			if (almostExplode1 == True and almostExplode2 == True):
				print ("OH NOOOOOO!!! Joystick EXPLODED!!!!\n\n" * 3)
				done = True
				break
		textPrint.unindent()
			
		# Hat switch. All or nothing for direction, not like joysticks.
		# Value comes back in an array.
		hats = joystick.get_numhats()
		textPrint.printline(screen, "Number of hats: {}".format(hats) )
		textPrint.indent()

		for i in range( hats ):
			hat = joystick.get_hat( i )
			textPrint.printline(screen, "Hat {} value: {}".format(i, str(hat)) )
		textPrint.unindent()
		
		textPrint.unindent()
		
		#Code to Find the Axes......
		numOfAxes = axes
		directionByte = 0
		# Axes used for driving, drawing, and direction byte.
		yAxis = int(joystick.get_axis(1) * -60 + 90)
		xAxis = int(joystick.get_axis(0) * -60 + 90)
		zAxis = int(joystick.get_axis(2) * -60 + 90)
		wAxis = int(joystick.get_axis(3) * -60 + 90)
		if (yAxis > 110):
			directionByte = 1
		elif (yAxis < 70):
			directionByte = 2
		elif (xAxis > 110):
			directionByte = 3
		elif (xAxis < 70):
			directionByte = 4
		elif (wAxis > 110):
			directionByte = 5
		elif (wAxis < 70):
			directionByte = 6
		else:
			directionByte = 0
		yAxisDot = int(joystick.get_axis(1) * 250 + 250)
		xAxisDot = int(joystick.get_axis(0) * 250 + 250)
		zAxisDot = int(joystick.get_axis(2) * 250 + 250)
		wAxisDot = int(joystick.get_axis(3) * 250 + 250)
		
		# Pulse stuff... Speed and axis.
		if (pulseWidthModulation == 1):
			pulseWidth = 0
			pulseWidthAxis = 1
			if (directionByte == 1 or directionByte == 2):
				pulseWidthAxis = 1
			elif (directionByte == 3 or directionByte == 4):
				pulseWidthAxis = 0
			elif (directionByte == 5 or directionByte == 6):
				pulseWidthAxis = 3
			pulseWidth = int(joystick.get_axis(pulseWidthAxis) * 255)
			textPrint.printline(screen, "pulseWidth = " + str(pulseWidth) + " pulseWidthAxis = " + str(pulseWidthAxis))
			if (pulseWidth < 0):
				pulseWidth = pulseWidth * -1
			if (pulseWidth > 255):
				pulseWidth = 0
				
		#textPrint.printline(screen, "Number of Axes: %f" %numOfAxes)
		#textPrint.printline(screen, "xAxis: %f\nyAxis: %f\nzAxis: %f\nwAxis: %f" %(xAxis,yAxis,zAxis,wAxis))
		pygame.draw.circle(screen, BLUE, [xAxisDot, 250], 15, 0)
		pygame.draw.circle(screen, RED, [250, yAxisDot], 15, 0)
		pygame.draw.circle(screen, GREEN, [zAxisDot, 200], 5, 0)
		pygame.draw.circle(screen, BLACK, [500, wAxisDot], 15, 0)
		if (pulseWidthModulation == 1):
			pulseDot = int(250 - pulseWidth)
			pygame.draw.circle(screen, PINK, [100, pulseDot], 20, 0)
		#"""
		if (serialConnected == True and serial.isOpen()):
			#time.sleep(0.1)
			serial.write(chr(255).encode('latin-1'))
			"""
			#serial.write(b'101')
			#print (chr(126).encode())
			#num = chr(255)
			#print (num)
			#serial.write(bytes(num, 'latin-1'))
			#serial.write(chr(101).encode())
			#print (b'255')
			#print (bytearray(b'255'))
			#print (bytes("255", 'utf-8'))
			#print (bytes("255", 'ascii'))
			#serial.write(chr(yAxis).encode())
			#serial.write(chr(xAxis).encode())
			#serial.write(chr(zAxis).encode())
			#serial.write(chr(wAxis).encode())
			"""
			serial.write(chr(directionByte).encode('latin-1'))
			serial.write(chr(zAxis).encode('latin-1'))
			if (pulseWidthModulation == 1):
				serial.write(chr(pulseWidth).encode('latin-1'))
			while(serial.inWaiting() > 0):
				if (serial.inWaiting() > 100):
					print ("python flushing...")
					serial.flush()
					serial.flushOutput()
					serial.flushInput()
				arduinoString = serial.readline()
				try:
					print (arduinoString.decode())
				except:
					print ("Error decoding string")
					break;
			#time.sleep(0.05)
		#"""
		
	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	
	# Limit to 25 frames per second.
	# Equals 40 milliseconds per frame.
	clock.tick(25)
	
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
#"""
if (serialConnected == True and serial.isOpen()):
	serial.close()
	print ("Serial closed...Exiting...")
#"""
pygame.quit ()