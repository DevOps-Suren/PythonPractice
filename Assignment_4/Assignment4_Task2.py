try:
    WriteFile = open("Output.txt","xt")
    UserInput = str(input("Enter your file contents : "))
    WriteFile.write(UserInput + "\n")
    print("File written Successfully")
    WriteFile.close()

    appendFile = open("Output.txt","at")
    appendInput = str(input("Enter your append file contents : "))
    appendFile.write(appendInput + "\n")
    print("Append contents written successfully")
    appendFile.close()

except IOError:
    print("ERROR: File Not Found")

with open("Output.txt","rt") as file:
    content = file.read()
    print(content)