# Basic SHA-256 Cracker

## Introduction

This is a basic SHA-256 brute-force cracker written in Python. The tool attempts to find the original plaintext password corresponding to a given SHA-256 hash using a wordlist. This project is a practical example of hash cracking and can help you understand how brute-force attacks work and how hashing functions operate in security contexts.

## Features

- **SHA-256 Hash Cracking**: Attempts to find the plaintext password that matches the given SHA-256 hash.
- **Wordlist Support**: Uses a wordlist of possible passwords to attempt cracking.
- **Progress Reporting**: Displays the progress of the brute-force attack and indicates whether the password was found or not.

## Prerequisites

- Python 3.x installed on your system.
- The `pwn` library for hashing and progress reporting. You can install it using `pip`:
    ```bash
    pip install pwntools
    ```
- Basic understanding of hashing algorithms, specifically SHA-256.

## Usage

To run the SHA-256 cracker, use the following command:

```bash
python3 sha256_cracker.py hash [--wordlist <wordlist>]
```
- hash: The SHA-256 hash you want to crack.
- --wordlist <wordlist> (Optional): The path to the wordlist file to use for the brute-force attack. If not specified, it defaults to /usr/share/wordlists/rockyou.txt.

## How It Works
1. **Argument Parsing:** 
  - The script uses argparse to handle command-line arguments. It takes the SHA-256 hash to crack and optionally a wordlist file path.
  - The default wordlist is `/usr/share/wordlists/rockyou.txt`
```python
parser = argparse.ArgumentParser(description="SHA-256 Brute-force script")
parser.add_argument("hash", type=str, help="The SHA-256 hash to crack")
parser.add_argument("--wordlist", type=str, default="/usr/share/wordlists/rockyou.txt", 
                    help="The wordlist to use (default: /usr/share/wordlists/rockyou.txt)")
args = parser.parse_args()
```
2. **Retrieve Arguments:**
  - Extracts the hash and wordlist from the command-line arguments.
  ```python
  wanted_hash = args.hash
  wordlist = args.wordlist
  ```

3. **Start Brute-force Attempt:**
  - Opens the wordlist file and reads it line by line. For each password, it computes the SHA-256 hash and checks if it matches the target hash.
  - Displays progress and results using `pwn`'s `log.progress` for real-time feedback.
  ```python
  with log.progress("Attempting to crack hash: {}!\n".format(wanted_hash)) as p:
    with open(wordlist, "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)
            p.status("[{}] {} == {} ".format(attempts, password.decode('latin-1'), password_hash))
            if password_hash == wanted_hash:
                p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1
    p.failure("Password hash not found")
  ```
4. **Exception Handling:**
   - Handles errors such as missing wordlist files and other exceptions.
   ```python
   except FileNotFoundError:
    p.failure(f"Password list file not found: {wordlist}")
   except Exception as e:
    p.failure(f"An error occurred: {str(e)}")

   ```

### Example
- Cracking Hash With Our Script <br>
![cracker](https://github.com/syedsaad2005/Basic-Python-Projects/assets/142715489/11143172-dc89-4836-8254-f38d0e09d30a)






## Potential Improvements
- Extend the script to support additional hash algorithms like MD5 or SHA-1.
- Implement more efficient techniques or parallel processing to speed up the brute-force attack.
- Include features like progress bars, estimated time, or interactive command-line options.

## Contributing
Feel free to submit issues or pull requests for improvements.

## Contact
For any questions or feedback, you can reach me at **syed4000saad@gmail.com**
  
