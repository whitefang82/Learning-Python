# READING FILE

from sys import argv

script, filename = argv

txt = open(filename)        #open file

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) #will look for the name of text in th folder

print(txt_again.read())
