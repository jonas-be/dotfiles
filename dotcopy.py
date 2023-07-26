import sys
import os
import shutil
import configparser


def copy_files(source, destination, is_file=False):
    source_path = os.path.expanduser(source)
    destination_path = os.path.expanduser(destination)

    try:
        if not is_file and os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        if is_file:
            shutil.copy2(source_path, destination_path)
        else:
            shutil.copytree(source_path, destination_path)
        print("Files copied successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def copy_entry(entry_name, action, config):
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
        print(f"Invalid action for entry '{entry_name}'. Use 'put' or 'get'.")


def main():
    if len(sys.argv) < 3:
        print("Usage: python x.py [put|get|all] [entry_name]")
        return

    action = sys.argv[1]
    entry_name = sys.argv[2]

    config = configparser.ConfigParser()
    config.read("config.ini")

    if entry_name == "all":
        for entry_name in config.sections():
            copy_entry(entry_name, action, config)
    else:
        copy_entry(entry_name, action, config)


if __name__ == "__main__":
    main()

