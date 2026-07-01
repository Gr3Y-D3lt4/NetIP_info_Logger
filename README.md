# NetIP_info_Logger
A Python utility that periodically collects and logs system network information—including IPv4 address, IPv6 address, MAC address, and timestamps—into a text file for monitoring, troubleshooting, and educational purposes.

## Features

- 🌐 Retrieves the system's IPv4 address
- 🌍 Retrieves the system's IPv6 address (when available)
- 🖥 Obtains the system's MAC address
- 📝 Appends network information to a log file
- ⏰ Automatically records timestamps for each entry
- 🔄 Periodically updates the log every 10 seconds
- 🐍 Simple and lightweight Python implementation

## Technologies Used

- Python 3
- socket
- uuid
- time

## Project Structure

```
NetIP_info_Logger/
│
├── network_logger.py
├── network_details.txt
├── README.md
├── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/NetInfo-Logger.git
```

Move into the project directory:

```bash
cd NetInfo-Logger
```

Run the application:

```bash
python network_logger.py
```

## Sample Output

```
==================================================
System IPv4 Address: 192.168.1.10
System IPv6 Address: fe80::abcd:1234:5678:90ef
MAC Address: 00:1A:2B:3C:4D:5E
Last Updated: 2026-07-01 14:30:45
```

## Applications

- Network troubleshooting
- Learning Python networking concepts
- Recording system network information
- Device identification within a local network
- Educational and laboratory projects

## Future Enhancements

- Export logs to CSV or JSON
- Display network details in a GUI
- Detect IP address changes
- Monitor multiple network interfaces
- Automatic log rotation
- Email notifications when network information changes

## License

This project is licensed under the MIT License.
