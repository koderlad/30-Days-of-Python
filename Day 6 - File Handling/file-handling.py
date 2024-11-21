"""
File Modes:
r: Read. Opens the files for reading.
w: Write. Creates a new file or overwrites an existing file.
a: Append. Adds data to the end of the file.
r+: Read and Write. Does not create a new file but modifies the content based on its file pointer.
"""

# Reading a file
file = open("example.txt", "r") #Opens the file in read mode.
content = file.read() #The file needs to be passed through the read() function to grab the content.
file.close() #This is an important step to free out the memory and prevent any future overwriting of the file.

"""
Other Reading Methods: 
read(size): Reads size(integer) characters
readline(): Reads one line at a time.
readlines(): Reads all lines as a list.
"""

# Writing a file
file = open("example.txt", "w") #Opens the file in write mode.
file.write("Hello World!\n") #Writes to the file.
file.write("Welcome to file handling in Python")
file.close()

# Appending a file
# Writing a file
file = open("example.txt", "a") #Opens the file in append mode.
file.write("\nApending a new line to the file.")
file.close()

#Using 'with' for File Handling
"""The 'with' statement ensures proper resource management by automatically closing the file."""
with open("example.txt", 'r') as file:
    content = file.read()
    print(content)
    #No need to call file.close()