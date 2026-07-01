import socket
import uuid
import time

def get_network_details():
    try:
        hostname = socket.gethostname()  # Get the hostname
        ipv4 = socket.gethostbyname(hostname)  # Get IPv4 address
        
        # Get IPv6 address
        ipv6 = None
        for info in socket.getaddrinfo(hostname, None, socket.AF_INET6):
            ipv6 = info[4][0]
            break
        
        # Get MAC address
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)][::-1])
        
        return ipv4, ipv6, mac_address
    except socket.error as e:
        return f"Error retrieving network details: {e}", None, None

#def store_network_details(filename="network_details.txt"):
   # while True:
        #ipv4, ipv6, mac_address = get_network_details()
        #with open(filename, "w") as file:
           # file.write(f"System IPv4 Address: {ipv4}\n")
          #  file.write(f"System IPv6 Address: {ipv6}\n")
         #   file.write(f"MAC Address: {mac_address}\n")
        #    file.write(f"Last Updated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
       # print(f"Network details updated in {filename} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
       # time.sleep(10)  # Wait for 1 minutes
def store_network_details(filename="network_details.txt"):
    while True:
        ipv4, ipv6, mac_address = get_network_details()

        with open(filename, "a") as file:   # Append mode
            file.write("=" * 50 + "\n")
            file.write(f"System IPv4 Address: {ipv4}\n")
            file.write(f"System IPv6 Address: {ipv6}\n")
            file.write(f"MAC Address: {mac_address}\n")
            file.write(f"Last Updated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        print(f"Network details appended to {filename} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(10)

if __name__ == "__main__":
    store_network_details()
