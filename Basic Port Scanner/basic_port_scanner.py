#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 4 or (len(sys.argv) == 5 and sys.argv[4] == '-v'):
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
    verbose = len(sys.argv) == 5 and sys.argv[4] == '-v'
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip> <start_port> <end_port> [-v]")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

# Used typecasting to omit any error
start_port = int(sys.argv[2])  # Argument from user for start port
end_port = int(sys.argv[3])    # Argument from user for end port

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # Returns an error indicator - if port is open it throws a 0, otherwise 1
        if result == 0:
            print("Port {} is open".format(port))
        elif verbose:
            print("Port {} is closed".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()
