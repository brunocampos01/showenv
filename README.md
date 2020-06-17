# Easy env

```shell script
    ______                
   / ____/___ ________  __
  / __/ / __ `/ ___/ / / /
 / /___/ /_/ (__  ) /_/ / 
/_____/\__,_/____/\__, /  
                 /____/   
    ______           _                                       __ 
   / ____/___ _   __(_)________  ____  ____ ___  ___  ____  / /_
  / __/ / __ \ | / / / ___/ __ \/ __ \/ __ `__ \/ _ \/ __ \/ __/
 / /___/ / / / |/ / / /  / /_/ / / / / / / / / /  __/ / / / /_  
/_____/_/ /_/|___/_/_/   \____/_/ /_/_/ /_/ /_/\___/_/ /_/\__/  
                                                                
```
é uma ferramenta de CLI para preparar o ambiente de desenvolvimento e reprodução para projetos de data science/ machine learning/ deep learning.

- Suitable for implementing the config requirements of a 12-factor app: https://12factor.net/config


## Features
- [ ] instala os pré-requisitos no S.O
- [ ] instala o Python3
- [ ] instala virtualEnv
- [ ] install Pipenv
- [ ] Delete all compiled Python files
- [ ] Apply Lint using flake8
- [ ] Test if environment contains Python3
- [ ] Running on virtual environment
- [ ] Running on isolation environment
- [ ]
- [ ]
- [ ]


## Which diference to Anaconda ?
- Anaconda need [extended dependencies](https://docs.anaconda.com/anaconda/install/linux/)
- Anaconda dont install pré-requisitos no S.O
- Anaconta dont apply linter
- Anaconda dont generate file with configuration environment
- Anaconta dont tree in each project

# Running
1. [Local](#running-in-local)
2. [Development: Virtual Environment](#running-in-virtual-environment)
3. [Deploy: Container](#running-in-container)


## Running in Local
- Install Python Dependencies, Test python environment and Delete all compiled Python files.

```shell script
sudo make

# Available rules:

# clean               Delete all compiled Python files
# lint                Lint using flake8
# prereq              Install Python Dependencies
# test_environment    Test python environment is setup correctly
```

```shell script
make prereq
make test_environment
make clean
```

- Install the libraries

```shell script
pip3 install -r virtualenv_requirements.txt # libs necessary to prepare virtual environment
pip3 install -r requirements.txt            # libs necessary in notebooks
```

---

## Running in Virtual Environment

- Create virtual environment

```shell script
bash create_virtual_env.sh
```

- Activate this semi-isolated environment

```shell script
source venv/bin/activate
```

- Install the libraries

```shell script
pip3 install -r virtualenv_requirements.txt # libs necessary to prepare virtual environment
pip3 install -r requirements.txt            # libs necessary in notebooks
```


```shell script
pipenv --python 3 # libs necessary to prepare virtual environment
pipenv install -e pipefile
```

---

## Running in Container

- Necessary be in home this project

```sh
name_project=$(basename "$(pwd)")
echo $name_project
sudo docker build --no-cache -t $name_project -f src/environment/container/Dockerfile .
sudo docker run -it -p 8888:8888 $name_project
```
