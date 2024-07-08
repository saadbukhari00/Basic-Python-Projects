# Basic Port Scanner

## Introduction

This is a simple port scanner written in Python. The tool allows you to scan a range of ports on a specified IP address or hostname to determine which ports are open and which are closed. It's a basic example of network scanning and can be useful for learning about socket programming and network security concepts.

## Features

- **Scan a range of ports**: Check if ports within a specified range are open or closed.
- **Verbose Mode**: Display information about closed ports when running in verbose mode (`-v` flag).

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of networking concepts and command-line operations.

## Usage

To run the port scanner, use the following command:

```bash
python3 scanner.py <ip> <start_port> <end_port> [-v]
```

- ip: The target IP address or hostname you want to scan.
- start_port: The starting port number of the range to scan.
- end_port: The ending port number of the range to scan.
- -v (Optional): Add this flag for verbose mode to display closed ports.

## How It Works
1. The script translates the provided hostname to an IP address.
2. It scans each port in the specified range using TCP connection attempts.
3. If the connection is successful, it reports the port as open; otherwise, it reports the port as closed if the verbose flag is set.
4. Handles common exceptions such as invalid hostname or connection errors.


## Potential Improvements
- Add features like saving results to a file.
- Implement additional scan types (e.g., UDP scans).
- Enhance error handling and reporting.

## Contributing
Feel free to submit issues or pull requests for improvements.

## Contact
For any questions or feedback, you can reach me at **syed4000saad@gmail.com**
