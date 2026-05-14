try:
    with open("Simple.txt","r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("ERROR: The file Simple.txt is not found")