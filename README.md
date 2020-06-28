# Show Env

```shell script
         __                                 
   _____/ /_  ____ _      _____  ____ _   __
  / ___/ __ \/ __ \ | /| / / _ \/ __ \ | / /
 (__  ) / / / /_/ / |/ |/ /  __/ / / / |/ / 
/____/_/ /_/\____/|__/|__/\___/_/ /_/|___/  
                                            

```

It is a tool to show detailed information of:
- Python
- Pip
- Libraries
- OS
- Disck usage

by project.

## Requirement
- Python 3.7 or more<br/>
- pip
- Python Virtual Environment (recomended)

## Install
```shell script
pip3 install showenv
```

## Running
```shell script
cd <REPOSITORY_TO_ANALYSE>
showenv
```


## Output
2 files generated in current project.


- config_environment.txt
```
OS:
Linux
Distributor ID:	Ubuntu
Description:	Ubuntu 19.04
Release:	19.04
Codename:	disco

Python Version:
Python 3.7.3

Pip Version:
pip 19.1.1 from $HOME/projetos/challenges/kaggle/porto-seguro-safe-driver-prediction/src/environment/venv/lib/python3.7/site-packages/pip (python 3.7)

Jupyter Version:
4.4.0

--------------------------------------------------

Disk Usage:

data:
383M	data/

virtual env:
736M	src/environment/venv/

all:
1,3G	.
```

- struture_project.txt
```
.
├── data
│   ├── kaggle_submission.csv
│   └── raw
│       ├── datasets.zip
│       ├── sample_submission.csv
│       ├── test.csv
│       └── train.csv
├── LICENSE
├── notebooks
│   └── porto_seguro_safe_driver.ipynb
├── README.md
├── references
│   └── porto-seguro-vector-logo.png
└── src
    └── environment
        ├── config_environment.txt
        ├── container
        │   └── Dockerfile
        ├── create_requirements.sh
        ├── create_virtual_env.sh
        ├── __init__.py
        ├── jupyter_notebook_config.py
        ├── makefile
        ├── prepare_env.py
        ├── README.md
        ├── requirements.txt
        ├── show_config_environment.sh
        ├── show_struture_project.sh
        ├── struture_project.txt
        ├── test_environment.py
        ├── venv
        └── virtualenv_requirements.txt

8 directories, 24 files
```

---

#### Author
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img class="" src="https://github.com/brunocampos01/devops/blob/master/images/gmail.png" width="28"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img class="ai-subscribed-social-icon" src="https://github.com/brunocampos01/devops/blob/master/images/github.png" width="30"></a>
<a href="https://www.linkedin.com/in/brunocampos01/" target="_blank"><img class="ai-subscribed-social-icon" src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" width="30"></a>
Bruno Aurélio Rôzza de Moura Campos 

---

#### Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br/>
