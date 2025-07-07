# Import the 'socket' library, which is Python's built-in library for networking.
import socket
import sys
from datetime import datetime

# --- Functions ---

def get_target_host():
    """Gets the target host from the user."""
    return input("Enter the target IP address or hostname to scan: ")

def get_port_range():
    """Gets the port range from the user."""
    while True:
        try:
            start_port = int(input("Enter the starting port number: "))
            end_port = int(input("Enter the ending port number: "))
            if 0 < start_port <= end_port <= 65535:
                return start_port, end_port
            else:
                print("Invalid port range. Please enter numbers between 1 and 65535.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def scan_ports(target, start_port, end_port):
    """Scans the specified ports on the target host."""
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    try:
        # Loop through the port range provided by the user.
        for port in range(start_port, end_port + 1):
            # Create a new socket object for each connection attempt.
            # AF_INET specifies that we're using IPv4.
            # SOCK_STREAM specifies that this is a TCP socket.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout for the connection attempt. If a port is not open,
            # we don't want to wait forever. 0.5 seconds is a reasonable timeout.
            socket.setdefaulttimeout(0.5)

            # Try to connect to the target on the current port.
            # The connect_ex() method returns 0 if the connection is successful (port is open).
            # It returns an error code if the connection fails (port is closed or filtered).
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}:    OPEN")
                open_ports.append(port)
            else:
                # You can uncomment the line below if you want to see closed ports too.
                # print(f"Port {port}:    Closed")
                pass

            # Close the socket to free up resources.
            s.close()

    except socket.gaierror:
        print("\nError: Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nError: Could not connect to server.")
        sys.exit()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    return open_ports

def print_summary(open_ports):
    """Prints a summary of the scan results."""
    print("-" * 50)
    if open_ports:
        print("Scan complete. Open ports found:")
        print(open_ports)
    else:
        print("Scan complete. No open ports were found in the specified range.")
    print("-" * 50)


# --- Main Program Execution ---

if __name__ == "__main__":
    target_host = get_target_host()
    start, end = get_port_range()
    found_ports = scan_ports(target_host, start, end)
    print_summary(found_ports)
