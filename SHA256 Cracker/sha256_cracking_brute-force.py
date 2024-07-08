import argparse
from pwn import *

# Set up argument parsing
parser = argparse.ArgumentParser(description="SHA-256 Brute-force script")
parser.add_argument("hash", type=str, help="The SHA-256 hash to crack")
parser.add_argument("--wordlist", type=str, default="/usr/share/wordlists/rockyou.txt", 
                    help="The wordlist to use (default: /usr/share/wordlists/rockyou.txt)")
args = parser.parse_args()

# Retrieve the arguments
wanted_hash = args.hash
wordlist = args.wordlist
attempts = 0

# Print information about the wordlist being used
print("The file being used for passwords is: {}".format(wordlist))
if wordlist == "/usr/share/wordlists/rockyou.txt":
    print("You provided no wordlist, so using the default: rockyou.txt")

# Start the brute-force attempt
with log.progress("Attempting to crack hash: {}!\n".format(wanted_hash)) as p:
    try:
        # Open the wordlist file
        with open(wordlist, "r", encoding='latin-1') as password_list:
            for password in password_list:
                password = password.strip("\n").encode('latin-1')  # Read and encode each password
                password_hash = sha256sumhex(password)  # Compute the SHA-256 hash of the password
                p.status("[{}] {} == {} ".format(attempts, password.decode('latin-1'), password_hash))
                
                # Check if the computed hash matches the wanted hash
                if password_hash == wanted_hash:
                    p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
                    exit()
                
                attempts += 1  # Increment the attempt counter

        # If the password is not found in the list
        p.failure("Password hash not found")

    except FileNotFoundError:
        p.failure(f"Password list file not found: {wordlist}")
    except Exception as e:
        p.failure(f"An error occurred: {str(e)}")
