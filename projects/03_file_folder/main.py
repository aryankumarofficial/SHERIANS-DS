import os
from pathlib import Path
import shutil


def display_options():
    print("""
    Options:
        0. Exit File Manager
        1. Create a folder
        2. Read files and folders
        3. Update the folder
        4. Delete the folder
        5. Create a file
        6. Read a file
        7. Update a file
        8. Delete a file
    """)


def create_folder():
    try:
        name = input("Folder name:\x20")
        folder_path = Path(name)
        folder_path.mkdir()
    except Exception as err:
        print(f"An Error occurred creating folder as {err}")
    else:
        print("Folder created successfully!")


def read_file_folder():
    pwd = Path("")
    dir_and_files = list(pwd.rglob("*"))
    for item, value in enumerate(dir_and_files):
        print(f"{item + 1} : {value}")


def update_folder():
    try:
        read_file_folder()
        old_folder = input("which folder you want to modify:\x20")
        old_folder_path = Path(old_folder)
        if old_folder_path.exists() and old_folder_path.is_dir():
            new_name = input(f"Enter new name for {old_folder}:\x20")
            new_path = Path(new_name)
            old_folder_path.rename(new_path)
        else:
            print(f"No such folder exist")
    except Exception as err:
        print(f"Failed to rename folder as {err}")
    else:
        print("Your folder name is updated successfully!")


def delete_folder():
    try:
        read_file_folder()
        folder = input("Which folder you want to delete:\x20")
        folder_path = Path(folder)
        if folder_path.exists() and folder_path.is_dir():
            shutil.rmtree(folder_path)
        else:
            raise Exception("Folder Not Found")
    except Exception as err:
        print(f"Failed to Delete folder as {err}")
    else:
        print("Folder Deleted successfully!")


def create_file():
    try:
        read_file_folder()
        name = input("Your new file name/path:\x20")
        file_path = Path(name)
        if not file_path.exists():
            with open(file_path, "w") as fs:
                data = input("write what you want in this file:\x20")
                fs.write(data)
        else:
            raise Exception("File Already Exists")
    except Exception as err:
        print(f"Failed to create file as {err}")
    else:
        print("File Created successfully!")


def read_file():
    try:
        read_file_folder()
        name = input("which file you want to read:\x20")
        file_path = Path(name)
        if file_path.exists() and file_path.is_file():
            with open(file_path, "r") as fs:
                print(fs.read())
        elif not file_path.is_file():
            raise Exception("Not a valid file")
        elif not file_path.exists():
            raise Exception("File Doesn't exists")

    except Exception as err:
        print(f"Failed to read file as {err}")


def update_file():
    try:
        read_file_folder()
        file = input("which file you want to update:\x20")
        file_path = Path(file)

        if file_path.exists() and file_path.is_file():
            with open(file_path, "a") as fs:
                data = input("what you want to add to the file:\x20")
                fs.write(f"\n{data}")
        elif not file_path.is_file():
            raise Exception("Invalid file")
        elif not file_path.exists():
            raise Exception("File Doesn't exists")
    except Exception as err:
        print(f"Failed to update the file as {err}")


def delete_file():
    try:
        read_file_folder()
        name = input("which file you want to delete:\x20")
        file_path = Path(name)
        if file_path.exists() and file_path.is_file():
            confirm = input("Are you sure to delete file:(y/n):\x20")
            if confirm.lower() in ("y", "yes"):
                os.remove(file_path)
            else:
                print("Aborting file Deletion")
                return
        elif not file_path.is_file():
            raise Exception("Invalid file")
        elif not file_path.exists():
            raise Exception("File doesn't exists")
    except Exception as err:
        print(f"Failed to delete file as {err}")
    else:
        print("File Deleted successfully!")


def main():
    while True:
        display_options()
        try:
            choice = int(input("Please choose your options(0-8):\x20"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                create_folder()
            case 2:
                read_file_folder()
            case 3:
                update_folder()
            case 4:
                delete_folder()
            case 5:
                create_file()
            case 6:
                read_file()
            case 7:
                update_file()
            case 8:
                delete_file()
            case 0:
                print("Closing File Manager...")
                break
            case _:
                print("Invalid option. Pleas Try Again")


if __name__ == "__main__":
    main()
