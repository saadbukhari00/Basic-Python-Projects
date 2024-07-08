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

<ip>: The target IP address or hostname you want to scan.
<start_port>: The starting port number of the range to scan.
<end_port>: The ending port number of the range to scan.
-v (Optional): Add this flag for verbose mode to display closed ports.
