import yaml
import subprocess

yaml_file = 'pkgs.yaml'

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GRAY = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

def ask_for_groups(group_list, aur=False):
    groups = []
    for group in group_list:
        if aur:
            print(f'Install {c.BOLD}{group}{c.ENDC} {c.GRAY}[AUR]{c.ENDC} packages? [Y/n]', end='')
        else:
            print(f'Install {c.BOLD}{group}{c.ENDC} packages? [Y/n]', end='')
        answer = input()
        if answer == 'y' or answer == '':
            groups.append(group)
    return groups

def print_group(group, aur=False):
    for pkg in group:
        if aur:
            print(f'    {c.ITALIC}{pkg}{c.ENDC} {c.GRAY}[AUR]{c.ENDC}')
        else:
            print(f'    {c.ITALIC}{pkg}{c.ENDC}')

def final_question(arch_groups, aur_groups):
    print(f'\n{c.BOLD}Install the following packages?{c.ENDC}')
    for group in arch_groups:
        print(f' {c.BOLD}{group}{c.ENDC}')
        print_group(arch[group])
        if aur_groups.__contains__(group):
            print_group(aur[group], True)
    for group in aur_groups:
        if not arch_groups.__contains__(group):
            print(f' {c.BOLD}{group}{c.ENDC}')
            print_group(aur[group], True)

    print('Procced? [Y/n]', end='')
    answer = input()
    if answer != 'y' and answer != '':
        print(f'{c.FAIL}Aborted{c.ENDC}')
        exit(1)


def install_arch_package(package_name, aur=False):
    try:
        # Run the pacman command to install the package
        if aur:
            subprocess.run(['yay', '-S', '--noconfirm', package_name], check=True)
        else:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', package_name], check=True)
        print(f"Package {package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing package {package_name}: {e}")
        return False
    return True

def install_packages(arch_groups, aur_groups):
    failed_pkgs = []
    for group in arch_groups:
        for pkg in arch[group]:
            print(f'Installing {c.BOLD}{pkg}{c.ENDC}')
            if install_arch_package(pkg):
                print(f'{c.OKGREEN}Done{c.ENDC}')
            else:
                failed_pkgs.append(pkg)
    for group in aur_groups:
        for pkg in aur[group]:
            print(f'Installing {c.BOLD}{pkg}{c.ENDC}')
            if install_arch_package(pkg, aur=True):
                print(f'{c.BOLD}{c.OKGREEN}Done{c.ENDC}')
            else:
                failed_pkgs.append(pkg)
    # Print failed packages
    if len(failed_pkgs) > 0:
        print(f'{c.FAIL}Failed to install the following packages:{c.ENDC}')
        for pkg in failed_pkgs:
            print(f'  {c.BOLD}{pkg}{c.ENDC}')
    else:
        print(f'{c.OKGREEN}All packages installed successfully{c.ENDC}')

# Read YAML file
with open(yaml_file, 'r') as yaml_file:
    pkgs = yaml.safe_load(yaml_file)

arch = pkgs['arch']
aur = pkgs['aur']

arch_groups = ask_for_groups(arch)
aur_groups = ask_for_groups(aur, aur=True)

final_question(arch_groups, aur_groups)

print(f'\n{c.BOLD}Installing packages...{c.ENDC}')

install_packages(arch_groups, aur_groups)
