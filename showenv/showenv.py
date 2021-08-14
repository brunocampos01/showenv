import subprocess
import time
import os 


HERE = os.path.abspath(os.path.dirname(__file__))
cwd = os.getcwd()


def install_prereq():
    print('-' * 79, end='\n')
    print('It`s necessary install: tree\n')
    print('Installing Dependencies\n')
    subprocess.call('sudo apt install tree', shell=True)

    print('-' * 79, end='\n')
    print('Testing python environment is setup correctly\n')
    subprocess.call(f'python {HERE}/scripts/test_env.py', shell=True)

    print('-' * 79, end='\n')
    print('Creating and show structure this project\n')
    subprocess.call('touch structure_project.txt', shell=True)
    subprocess.call(f'bash {HERE}/scripts/show_structure_project.sh', shell=True)
    subprocess.call(f'mv {HERE}/scripts/structure_project.txt {cwd}', shell=True)

    print('-' * 79, end='\n')
    print('Creating file whats contains configuration environment\n')
    subprocess.call(f'bash {HERE}/scripts/show_config_env.sh', shell=True)
    subprocess.call('touch config_env.txt', shell=True)
    subprocess.call(f'mv {HERE}/scripts/config_env.txt {cwd}', shell=True)
    print('-' * 79, end='\n\n')
    
