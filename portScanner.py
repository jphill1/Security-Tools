import socket
import subprocess
import sys
from datetime import datetime

############################################################################################
#This script serves as a port scanner.

#A port scanner is a method that is used to determine which ports within a specific network
#are open and could be receiving or sending data. It is also used for sending packets to
#specific ports on a host, thus analyzing responses to identify vulnerabilities.
############################################################################################

#Blank your screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are about to scan
print " " * 60
print "PLease wait, scanning remote host", remoteServerIP
print "_" * 60

#Check the date and time the scan was started
t1 = datetime.now()

#Using the range function, specify ports.
#Also, we will perform error handling

try:
    for port in range (1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:     Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print "Hostname could not be resolved. Exiting"
    sys.exit()

except socket.error:
    print "Could not connect to server"
    sys.exit()

#Checking time again
t2 = datetime.now()

#Calculate the difference in time to know how long the scan took
total = t2 - t1

#Print the information on the screen
print 'Scanning Completed in: ', total
