"""
Create a script that:
- Reads from an input file (input.txt) containing multiple lines.
- Writes the reversed lines to an output file (output.txt).
"""

#Read content from input file
with open("input.txt", "r") as inputFile:
    content = inputFile.readlines() #This is a global variable

with open("output.txt", "w") as outputFile:
    for line in content:
        outputFile.write(line.strip()[::-1]+"\n") #strip() removes any trailing new line