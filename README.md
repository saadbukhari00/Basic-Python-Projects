# Python Practice Projects

Welcome to my collection of Python practice projects! This repository showcases a series of projects that I have worked on to improve my skills in Python programming, network security, and ethical hacking. Each project demonstrates different concepts and techniques that are essential for both beginners and those looking to enhance their knowledge in these areas.

## Table of Contents

- [Projects Overview](#projects-overview)
- [Libraries and Tools Used](#libraries-and-tools-used)
- [Learning Outcomes](#learning-outcomes)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

## Projects Overview

### 1. Basic Port Scanner

**Description**: A simple port scanner that checks a range of ports on a target IP address or hostname to determine if they are open or closed.

**Key Features**:
- Scans a range of ports to identify open and closed ports.
- Supports verbose mode to display closed ports.

**Usage**:
```bash
python3 scanner.py <ip> <start_port> <end_port> [-v]
```

**Libraries**:
- `socket`: For network operations.
- `sys`: For command-line arguments.
- `datetime`: For timestamping the start time of the scan.

**Example**:
```bash
python3 scanner.py example.com 20 80
python3 scanner.py example.com 20 80 -v
```

**[Detailed README for Basic Port Scanner](https://github.com/syedsaad2005/Basic-Python-Projects/blob/main/Basic%20Port%20Scanner/README.md)**

---

### 2. SHA-256 Cracker

**Description**: A brute-force script to crack SHA-256 hashes using a wordlist.

**Key Features**:
- Attempts to find the password that matches a given SHA-256 hash.
- Uses a wordlist to try different passwords.

**Usage**:
```bash
python3 sha256_cracker.py <hash> [--wordlist <path>]
```

**Libraries**:
- `argparse`: For command-line argument parsing.
- `pwnlib`: For SHA-256 hash computation and progress reporting.

**Example**:
```bash
python3 sha256_cracker.py <your-hash>
python3 sha256_cracker.py <your-hash> --wordlist /path/to/wordlist.txt
```

**[Detailed README for SHA-256 Cracker](https://github.com/syedsaad2005/Basic-Python-Projects/blob/main/SHA256%20Cracker/README.md)**

---

### 3. SSH Brute-force Script

**Description**: A brute-force attack script for SSH to find valid login credentials.

**Key Features**:
- Attempts to find a valid password for a given username via SSH.
- Uses a predefined wordlist of common passwords.

**Usage**:
```bash
python3 ssh_bruteforce.py <host> <username> [--port <port>]
```

**Libraries**:
- `argparse`: For command-line argument parsing.
- `pwnlib`: For handling SSH connections.
- `paramiko`: For SSH connections and handling exceptions.

**Example**:
```bash
python3 ssh_bruteforce.py example.com admin
python3 ssh_bruteforce.py example.com admin --port 2222
```

**[Detailed README for SSH Brute-force Script](https://github.com/syedsaad2005/Basic-Python-Projects/blob/main/SSH%20Login%20Brute%20Force/README.md)**

---

### 4. Web Brute-force Cracker

**Description**: A brute-force attack script to guess passwords for multiple usernames on a web login page.

**Key Features**:
- Attempts to find the correct password for multiple usernames by sending HTTP POST requests.
- Checks if a specific string is present in the response to determine a successful login.

**Usage**:
```bash
python3 web_bruteforce_cracker.py
```

**Libraries**:
- `requests`: For sending HTTP POST requests.
- `sys`: For displaying status updates in real-time.

**Example**:
```bash
python3 web_bruteforce_cracker.py
```

**[Detailed README for Web Brute-force Cracker](https://github.com/syedsaad2005/Basic-Python-Projects/tree/main/Web%20Login%20Form%20Brute%20Force)**

---

## Libraries and Tools Used

### Common Libraries

- **`requests`**: A popular HTTP library for sending HTTP requests and handling responses.
- **`argparse`**: A module for parsing command-line arguments.
- **`socket`**: A module for low-level network interactions and socket programming.
- **`paramiko`**: A library for SSH protocol implementation, used for remote server interactions.
- **`pwnlib`**: Part of the Pwntools library for exploit development and security research.

### Tools

- **`Wordlists`**: Various wordlists like `rockyou.txt` and `10-million-password-list-top-100.txt` are used for brute-force attacks.
- **`SecLists`**: A collection of security test data, including password lists.

## Learning Outcomes

Through these projects, I have gained hands-on experience with:

- **Network Security**: Understanding basic network security concepts like port scanning and brute-force attacks.
- **Python Programming**: Writing Python scripts for practical cybersecurity tasks.
- **Command-Line Interfaces**: Utilizing command-line arguments for script configurations.
- **Web and Network Protocols**: Learning about HTTP requests, SSH connections, and network communications.
- **Ethical Hacking**: Developing skills for ethical hacking and security testing practices.

## Disclaimer

**Use these scripts only on authorized systems and networks. Unauthorized access to systems, networks, or data is illegal and unethical. These projects are intended for educational purposes and should be used to enhance your skills in a responsible manner.**

## Contact

For any questions or feedback, you can reach me at **syed4000saad@gmail.com**.

## Acknowledgments

- Special thanks to the creators of the libraries and tools used in these projects.

---

Feel free to explore each project, learn from the code, and contribute to the repository. Happy coding!
