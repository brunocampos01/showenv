# Show Env
Report of Project Environment

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
- Disk usage

## Requirements
This project is tested with:

| Requisite      | Version             |
|----------------|---------------------|
| Python         | 3.9.1               |
| Pip            | 21.2.4              |
| Debian distros | Ubuntu/Linux Mint   |

## Install
```shell script
pip install showenv
```

## Usage
```shell script
cd <REPOSITORY_TO_ANALYSE>
showenv
```


## Output: Report of Project Environment
2 files generated in current project.

- config_env.txt
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
        ├── config_env.txt
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
        ├── show_config_env.sh
        ├── show_struture_project.sh
        ├── struture_project.txt
        ├── test_environment.py
        ├── venv
        └── virtualenv_requirements.txt

8 directories, 24 files
```

---

<p  align="left">
	<a href="mailto:brunocampos01@gmail.com" target="_blank"><img src="https://github.com/brunocampos01/brunocampos01/blob/main/images/email.png" width="30">
	</a>
	<a href="https://stackoverflow.com/users/8329698/bruno-campos" target="_blank"><img src="https://github.com/brunocampos01/brunocampos01/blob/main/images/stackoverflow.png" width="30">
	</a>
	<a href="https://www.linkedin.com/in/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/brunocampos01/blob/main/images/linkedin.png" width="30">
	</a>
	<a href="https://github.com/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/brunocampos01/blob/main/images/github.png" width="30"></a>
	<a href="https://medium.com/@brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/brunocampos01/blob/main/images/medium.png" width="30">
	</a>
    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png",  align="right" />
    </a>
    <br/>
</p>
