
import sys
import os
import shutil
import configparser


def copy_files(source, destination, is_file=False):
    source_path = os.path.expanduser(source)
    destination_path = os.path.expanduser(destination)

    try:
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        if is_file:
            shutil.copy2(source_path, destination_path)
        else:
            shutil.copytree(source_path, destination_path)
        print("Files copied successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python x.py [put|get] [entry_name]")
        return

    action = sys.argv[1]
    entry_name = sys.argv[2]

    config = configparser.ConfigParser()
    config.read("config.ini")

    if entry_name not in config.sections():
        print(f"No entry found with name '{entry_name}'")
        return

    entry = config[entry_name]
    source_path = entry["source"]
    destination_path = entry["destination"]

    if "file" in entry:
        is_file = entry.getboolean("file")
    else:
        is_file = False

    if action == "put":
        copy_files(source_path, destination_path, is_file)
    elif action == "get":
        copy_files(destination_path, source_path, is_file)
    else:
        print("Invalid action. Use 'put' or 'get'.")


if __name__ == "__main__":
    main()

