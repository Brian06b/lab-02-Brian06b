# Brian Barrios Montiel
# UWYO COSC 1010
# Novemeber 5, 2024
# HW 04
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here
# Homework Question: 
#Your code should accept input from the command line. Dates in the form of MM/DD/YYYY will be inputted.

#You will be reading from and writing to a file.
#prompt (2).txt
#You will write to a file called "out.txt".

#Look at prompt.txt to understand its structure.

#It contains key-value pairs on each line of the file.
#The keys are 'w' and '*'.
#'w' stands for white space, and '*' is an asterisk (*).
#The numeric value shows how many of each of those characters there are for each line in your output file.
#Each line in prompt.txt corresponds to one line in out.txt.

#For example, the line:
#"w:101    *:020    w:026    *:004    w:017    *:030"
#You will output a line with 101 white spaces, 20 asterisks, 26 white spaces, 4 asterisks, 17 white spaces, and 30 asterisks.
#All of that will be on ONE line of your output file.
#
#Each of the key-value pairs is separated by a tab '\t' character.
#The key values are separated by a ':' character.

#You can use the .split() function on strings to create a list. For example, pairs = line.split("\t") will give you a list of all the pairs in a line.

#You can multiply strings by an integer, x, to create a string repeated x times. So, string_val = "*" * 10 would create a string with 10 asterisks: "**********".

#You will be outputting a VERY recognizable ASCII art with this. If you are looking at the output file and you aren't sure what it is, you are likely doing it incorrectly. It can help if you zoom out on your output file.


with open("prompt.txt", "r") as input, open("out.txt", "w") as output:
    for line in input:
        pairs = line.strip().split("\t")
        output_line = ""    
        for pair in pairs:      
            key, value = pair.split(":")
            compute = int(value.strip())   
            if key == 'w':
                output_line += " " * compute  
            elif key == '*':
                output_line += "*" * compute 
        output.write(output_line + "\n")

