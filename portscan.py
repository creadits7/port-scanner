#!/usr/bin/env python
import socket
import sys
from datetime import datetime


# Ask for input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
portStart = int(raw_input("Start of port range: "))
portEnd = int(raw_input("End of port range: "))

# Ensure that the user doesn't enter a start port of 50 and an end of 15 for example...
if portEnd < portStart:
	print "You cannot have a negative range."
	sys.exit()


# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()


# Changes the timeout period for a failed connection (default was originally 30 seconds)
socket.setdefaulttimeout(0.07)

# Error handling for catching errors

try:
	count = 0
	openPorts = []
	for port in range(portStart, portEnd + 1):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "Port {}: 	 Open".format(port)
			count += 1
			openPorts.append(port)
		else:
			print "Port {}:		 Closed".format(port)
		sock.close()
	

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
print "\nPortscan found %s open ports between %s and %s" % (count, portStart, portEnd)
if count != 0:
	print "\nOpen ports:\n "
	for word in openPorts:
		print word
	