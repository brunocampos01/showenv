import argparse
import os

from pyfiglet import Figlet


f = Figlet(font='slant')


def install_prereq():
    command = os.popen("cd easyenv/ && sudo make clean")
    print('-' * 50, end='\n')
    print('Cleansing all compiled Python files\n')
    command.read()

    command = os.popen("cd easyenv/ && sudo make prereq")
    print('-' * 50, end='\n')
    print(f'Installing Python Dependencies\n')
    command.read()

    command = os.popen("cd easyenv/ && sudo make list")
    print('-' * 50, end='\n')
    print('Applying lint (flake8)\n')
    command.read()

    command = os.popen("cd easyenv/ && sudo make test_env")
    print('-' * 50, end='\n')
    print('Testing python environment is setup correctly\n')
    print(command.read())

    command = os.popen("cd easyenv/ && make create_virtual_env")
    print('-' * 50, end='\n')
    print('Creating virtualenv\n')
    print(command.read())

    command = os.popen("cd easyenv/ && make show_tree")
    print('-' * 50, end='\n')
    print('Creating and show structure project\n')
    print(command.read())

    command = os.popen("cd easyenv/ &&  make show_config_env")
    print('-' * 50, end='\n')
    print('Creating file whats contains configuration environment\n')
    print(command.read())


def main():
    print(f.renderText('Easy Environment'))
    install_prereq()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='\nInstall Python Dependencies;'
                                                 '\nDelete all compiled Python files;'
                                                 '\nApply lint using flake8;'
                                                 '\nTest python environment is setup correctly;'
                                                 '\nCreating virtual environment;'
                                                 '\nCreating and show structure project')
    parser.add_argument('--create',
                        type=str,
                        required=False,
                        default='create',
                        help='Run inside your project directory. It is necessary to have a file of requirements.txt')

    args = parser.parse_args()  # <class 'argparse.ArgumentParser'>
    create = args.create

    main()
