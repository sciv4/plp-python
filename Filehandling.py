file = open("newfile.pdf", "w")
file.write("This is my new file and I will now manipulate it.\n")

# Reading the file
file = open("newfile.pdf", "r")
content = file.read()
print(content)

# adding content to the file
file = open("newfile.pdf", "a")
file.write("This is fuuunnnn!")

#Modified file content
modified_content = (content.upper())
print(modified_content)



# Exception handling sample with no error
try:
    file = open("newfile.pdf", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file was not found.")
finally:
    file.close()
    


