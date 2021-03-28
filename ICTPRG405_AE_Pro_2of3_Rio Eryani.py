
"""
Check for server connection. If no connection to server, show error prompt. Otherwise, continue to import csv file.
"""
# Import modules required for program to run.
import os.path
import urllib.request
import sys

# Step One: Check for main server connection. Loop until server is connected.

try:
    if urllib.requests.get('http://10.12.15.56').ok:
        print("Main server is connected")
except:
    print("Main server is NOT connected!")


# Step Two: Check for file server connection. Loop until server is connected.
try:
    if urllib.requests.get('http://10.12.15.58').ok:
        print("File server is connected")
except:
    print("File server is NOT connected!")
    sys.exit()

# Step Three: Check if txt file exist in file server.

path = "/Users/Administration/New_Customers" # given file path
if os.path.isfile('filename.txt'):
    f = open("filename.txt", 'r') # open file to read.
    content = f.read()  # Display content of file.
    print(content)
    f.close()   # Close file after read.
else:
    print ("Missing customer name file! Please input text file to read.")   # Display warning if no file exist.

# Create new file directory from imported txt file.

with open('filename.txt') as file_name:
    for line in file_name:
        print(line)
        line = line.strip() #to remove question mark at the end of name from appearing.
        os.mkdir(os.path.join(path, line))


# How do I display the file exist error here??
