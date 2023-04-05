
#1Create a program to read and write into a txt file.
#2..The program should prompt the user to enter the name of a file. 
#3..if the file exists, it should let the user know and allow the user name changes into the file by adding
# content or changing words in the file.
#4.. if the file doesnt exist, it should create the file and allow the user .

filename = input("enter file name: ")
try:
    file = open(filename)
    if file:
        print(f"file exist")
        file = open(filename, "a")
        while True:
            line = input("Add the content: ")
            if line == "done":
                break
            else:
                file.write(line+"\n")
except FileNotFoundError as e:
    print("File not Found")
    cmd = input("create file y/n")
    if cmd == "y":
        file = open(filename, "w")
        choice = input("write to filr y/n: ")
        if choice == "y":
            while True:
                line = input("Type here: ")
                if line == "done":
                    break
                else:
                    file.write(line+"\n")

