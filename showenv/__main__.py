from showenv.showenv import install_prereq
from pyfiglet import Figlet


f = Figlet(font='slant')


def main():
    print(f.renderText('showenv'))
    print('Show informations about project, python version, pip, libraries and OS')
    install_prereq()


if __name__ == '__main__':
    main()
