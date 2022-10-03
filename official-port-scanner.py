# pip install pyfiglet
import pyfiglet
import socket
import subprocess

# clear the shell
subprocess.call('clear', shell=True)

# print banner
ascii_banner = pyfiglet.figlet_format("Icky Scanner")
print(ascii_banner,)
print("by cIpHeR_sHaDoW")
# Print a nice banner with information on which host we are about to scan
print("_" * 60)
print(" " * 60)

host = input("Host: ")
port = int(input("Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)
result = s.connect_ex((host, port))


print(" " * 60)
print("Please Wait, Scanning Remote Host: ", host)
print("_" * 60)

if result == 0:
    print(" " * 60)
    print('>>Port', port, 'is open!')
    print(" " * 60)
else:
    print(" " * 60)
    print('>>Port', port, 'is closed!')
    print(" " * 60)
