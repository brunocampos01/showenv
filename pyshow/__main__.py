from pyshow.pyshow import install_prereq
from pyfiglet import Figlet


f = Figlet(font='slant')


def main():
    print(f.renderText('pyshow'))
    print('Show informations about project, python, pip, libraries and OS \n ----- \n')
    install_prereq()


if __name__ == '__main__':
    main()
