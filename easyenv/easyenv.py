import subprocess
import time


def install_prereq(dir_project: str):
    print('-' * 50, end='\n')
    print('Cleansing all compiled Python files\n')
    p = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    print('-' * 50, end='\n')
    print(f'Installing Python Dependencies\n')
    p = subprocess.Popen(['sudo', 'make', 'prereq'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    print('-' * 50, end='\n')
    print('Applying lint (flake8)\n')
    p = subprocess.Popen(['make', 'lint'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    print('-' * 50, end='\n')
    print('Testing python environment is setup correctly\n')
    p = subprocess.Popen(['make', 'test_env'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    print('-' * 50, end='\n')
    print('Creating virtualenv\n')
    p = subprocess.Popen(['make', 'create_virtual_env'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    print('-' * 50, end='\n')
    print('Creating and show structure this project\n')
    p = subprocess.Popen(['make', 'show_tree'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    print('-' * 50, end='\n')
    print('Creating file whats contains configuration environment\n')
    p = subprocess.Popen(['make', 'show_config_env'], stdout=subprocess.PIPE, cwd='easyenv/')
    p.wait()
    p.stdout.close()
    time.sleep(1.0)

    p.kill()
