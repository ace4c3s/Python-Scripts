import socket, sys

# the gethostbyname gets the hostname from the terminal as provided.
# sys.argv enables reads the input from the command-line 
host = socket.gethostbyname(sys.argv[1])
# Specifies that ports to be scanned are 1-99
ports = range(1,5000)

# This function looks for open ports and returns them
def probe_ports(host,ports):
    # Initializes an empty list where the open ports will be appended.
    open_ports = []
    # We try the following first
    try:
        # This loops over all the ports as specified in the range
        for port in ports:
            # using width to create a socket closes the socket automatically without the socket.close()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # The port is probed for 2 seconds after which it's rendered to a particular state
                s.settimeout(2)
                # s.connect_ex connects to the port in the host provided and returns an integer. 0 if the connection is successful and 1 if an error is encountered.
                # This variable is assigned to variable result
                result = s.connect_ex((host,port))
                # If the connection is successful...
                if result == 0:
                    # Append the ports to the open_ports list
                    open_ports.append(port)
    # Throws this error the hostname provided was unresolved
    except socket.gaierror:
        print("Unable to resolve hostname")
    # Throws this error due to network and other socket related errors
    except socket.error:
        print("There was a problem with your connection")
    # Throws this error where there is interrupt to the keyboard
    except KeyboardInterrupt:
        print("The scan was stopped unexpectedly")
        # Exits the try-except block gracefully
        sys.exit(0)
    # This fuction returns the open ports
    return open_ports

# the probe_ports is called and assigned to open_ports
open_ports = probe_ports(host,ports)

# Checks if the open_ports is empty, if not empty print the open ports
if open_ports:
    print(f"The following ports are open {open_ports}")
else:
    print("Seems no ports are open")



