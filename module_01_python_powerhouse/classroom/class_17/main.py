"""
File Handling
"""

# file = open("../class_16/main.py", )
# file = open(r"C:\Users\aryan\Downloads\discord_backup_codes.txt")
# print(file.read())


# open("pull.txt","x")
# file = open("push.txt", "a")
# file.write("This is sample file created using python")
# file.close()

with open("../class_16/main.py", "r") as fs:
    print(fs.read())
