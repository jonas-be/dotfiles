import yaml
import subprocess

yaml_file = "pkgs.yaml"


class c:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    GRAY = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"

def get(x, key):
    if key in x:
        return x[key]
    return []

def ask_for_groups(group_list):
    groups = []
    for group in group_list:
        print(f"Install {c.BOLD}{group}{c.ENDC} packages? [Y/n]", end="")
        answer = input()
        if answer.lower() == "y" or answer == "":
            groups.append(group)
    return groups


def print_group(group):
    print(f"  {c.GRAY}pkgs:{c.ENDC}")
    for pkg in get(group, "pkgs"):
        print(f"    {c.ITALIC}{pkg}{c.ENDC}")
    for pkg in get(group, "aurs"):
        print(f"    {c.ITALIC}{pkg}{c.ENDC} {c.GRAY}[AUR]{c.ENDC}")

    print(f"  {c.GRAY}scripts:{c.ENDC}")
    for script in get(group, "scripts"):
        print(f"    {c.ITALIC}{script}{c.ENDC}")

    print(f"  {c.GRAY}dotfiles:{c.ENDC}")
    for dotfile in get(group, "dotfiles"):
        print(f"    {c.ITALIC}{dotfile}{c.ENDC}")


def final_question(groups):
    print(f"\n{c.BOLD}Install the following packages?{c.ENDC}")
    for group in groups:
        print(f" {c.BOLD}{group}{c.ENDC}")
        print_group(config[group])

    print("Procced? [Y/n]", end="")
    answer = input()
    if answer.lower() != "y" and answer != "":
        print(f"{c.FAIL}Aborted{c.ENDC}")
        exit(1)


def install_package(package_name, aur=False):
    try:
        if aur:
            subprocess.run(["yay", "-S", "--noconfirm", "--needed", package_name], check=True)
        else:
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", package_name], check=True)
        print(f"{c.BOLD}{c.OKGREEN}Package {package_name} installed successfully.{c.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{c.FAIL}Error installing package {package_name}: {e}{c.ENDC}")
        return False
    return True


def install_packages(groups):
    failed_pkgs = []
    for group_key in groups:
        group = config[group_key]
        for pkg in get(group, 'pkgs'):
            print(f"{c.HEADER}Installing {c.BOLD}{pkg}{c.ENDC}")
            if not install_package(pkg):
                failed_pkgs.append(pkg)

        for pkg in get(group, 'aurs'):
            print(f"{c.HEADER}Installing {c.BOLD}{pkg}{c.ENDC}")
            if not install_package(pkg, aur=True):
                failed_pkgs.append(pkg)

    # Print failed packages
    if len(failed_pkgs) > 0:
        print(f"{c.FAIL}Failed to install the following packages:{c.ENDC}")
        for pkg in failed_pkgs:
            print(f"  {c.BOLD}{pkg}{c.ENDC}")
    else:
        print(f"{c.OKGREEN}All packages installed successfully{c.ENDC}")


def copy_dotfiles_entry(dotfiles_entry):
    try:
        subprocess.run(["python", "dotcopy.py", "put", dotfiles_entry], check=True)
        print(f"{c.BOLD}{c.OKGREEN}Dotfiles {dotfiles_entry} copied successfully.{c.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{c.FAIL}Error copying dotfiles {dotfiles_entry}: {e}{c.ENDC}")
        return False
    return True


def copy_dotfiles(groups):
    failed_dotfiles = []
    for group_key in groups:
        group = config[group_key]
        for dotfiles_entry in get(group, 'dotfiles'):
            print(f"{c.HEADER}Copy {c.BOLD}{dotfiles_entry}{c.ENDC}")
            if not copy_dotfiles_entry(dotfiles_entry):
                failed_dotfiles.append(dotfiles_entry)

    # Print failed dotfiles_entries
    if len(failed_dotfiles) > 0:
        print(f"{c.FAIL}Failed to copy the following dotfiles:{c.ENDC}")
        for pkg in failed_dotfiles:
            print(f"  {c.BOLD}{pkg}{c.ENDC}")
    else:
        print(f"{c.OKGREEN}All dotfiles copied successfully{c.ENDC}")


# Read YAML file
with open(yaml_file, "r") as yaml_file:
    config = yaml.safe_load(yaml_file)

groups = ask_for_groups(config)

final_question(groups)

print(f"\n{c.BOLD}Installing packages...{c.ENDC}")
install_packages(groups)

print(f"\n{c.BOLD}Copy dotfiles...{c.ENDC}")
copy_dotfiles(groups)
