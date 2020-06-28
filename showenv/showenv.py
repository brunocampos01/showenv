import subprocess
import time
import os 


HERE = os.path.abspath(os.path.dirname(__file__))
cwd = os.getcwd()


def install_prereq():
    print('-' * 50, end='\n\n')
    print('Installing Dependencies\n')
    subprocess.call('sudo apt install tree', shell=True)

    print('-' * 50, end='\n\n')
    print('Testing python environment is setup correctly\n')
    subprocess.call(f'python {HERE}/scripts/test_env.py', shell=True)

    print('-' * 50, end='\n\n')
    print('Creating and show structure this project\n')
    subprocess.call('touch struture_project.txt', shell=True)
    subprocess.call(f'bash {HERE}/scripts/show_structure_project.sh', shell=True)
    subprocess.call(f'mv {HERE}/scripts/struture_project.txt {cwd}', shell=True)

    print('-' * 50, end='\n\n')
    print('Creating file whats contains configuration environment\n')
    subprocess.call(f'bash {HERE}/scripts/show_config_environment.sh', shell=True)
    subprocess.call('touch config_environment.txt', shell=True)
    subprocess.call(f'mv {HERE}/scripts/config_environment.txt {cwd}', shell=True)
    print('-' * 50, end='\n\n')
