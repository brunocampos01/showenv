import argparse
from .easyenv import install_prereq
from pyfiglet import Figlet


f = Figlet(font='slant')


def main(dir_project=dir_project):
    print(f.renderText('Easy Environment'))
    install_prereq(dir_project=dir_project)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='\nInstall Python Dependencies;'
                                                 '\nDelete all compiled Python files;'
                                                 '\nApply lint using flake8;'
                                                 '\nTest python environment is setup correctly;'
                                                 '\nCreating virtual environment;'
                                                 '\nCreating and show structure project')
    parser.add_argument('--dir_project',
                        type=str,
                        required=False,
                        default='.',
                        help='Run inside your project directory. It is necessary to have a file of requirements.txt')

    args = parser.parse_args()  # <class 'argparse.ArgumentParser'>
    dir_project = args.dir_project

    main(dir_project=dir_project)
