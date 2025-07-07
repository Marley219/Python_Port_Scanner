Simple Python Port Scanner
This is a beginner-friendly port scanner written in Python. It's a great project for learning the basics of network programming with Python's built-in socket library.

Description
The script allows a user to specify a target host (either an IP address like 8.8.8.8 or a hostname like google.com) and a range of ports to scan. It then attempts to connect to each port in the specified range and reports which ports are open.

Features
Scans a user-defined range of TCP ports.

Works with both IP addresses and hostnames.

Reports open ports.

Simple, easy-to-read, and commented code.

How to Use
Make sure you have Python 3 installed on your system.

Save the code as port_scanner.py.

Run the script from your terminal:

python port_scanner.py

The script will prompt you to enter the target host and the port range you wish to scan.

Example
Enter the target IP address or hostname to scan: scanme.nmap.org
Enter the starting port number: 20
Enter the ending port number: 80
--------------------------------------------------
Scanning target: scanme.nmap.org
Time started: 2025-07-07 11:21:00.123456
--------------------------------------------------
Port 22:    OPEN
Port 80:    OPEN
--------------------------------------------------
Scan complete. Open ports found:
[22, 80]
--------------------------------------------------

Disclaimer
This tool is for educational purposes only. Only use it to scan networks and hosts that you have explicit permission to test. Unauthorized port scanning can be considered a hostile activity.
