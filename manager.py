# key = input("The key you will be using is: ")
fileRead = open("passwords.txt")
action = input("What will you do? (view to view passwords/add to add a new password): ")

if action == "view":
    print(fileRead.read())
elif action == "add":
    title = input("Write a title for the new entry: ")
    usr = input("Now, write a username/email: ")
    pwd = input("And last but not least a password: ")
    fileAdd = open("passwords.txt", "a")
    fileAdd.write(title + "\n")
    fileAdd.write(usr + "\n")
    fileAdd.write(pwd + "\n")
else:
    print("Instruction unclear. Start the program again.")