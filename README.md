# **ASE 2021/2022**  

This repository contains the lab activities performed in the **Advanced Software Engineering** course at the **University of Pisa**.

---

## **Flask Framework**  

### **Installation**  
To set up the Flask environment, execute the following commands:

```sh
sudo apt install python3-venv
mkdir flask_app && cd flask_app
python3 -m venv venv
source venv/bin/activate
pip install Flask
python -m flask --version
export FLASK_APP=hello.py
flask run
deactivate
```

## Running Flask Application
To start the Flask application, use the following commands:

```sh
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
./run.sh
```

## cURL Commands
To test the API endpoints, use:

```sh
curl -v http://127.0.0.1:5000/api
curl -v -X DELETE http://127.0.0.1:5000/api
```

## Creating Requirements File
To generate a requirements.txt file:

```sh
pip freeze > requirements.txt
```

## Useful Terminal Commands
File Permissions

```sh
chmod ugo+x *
```

Locate Flask Binary
```sh
which flask
```

## GitHub Commands
Adding and Committing Changes

```sh
git add *
git commit -m "first commit"
git push
```

Deleting a Branch
```sh
git branch -d <name_of_branch>
```

## pytest Installation & Usage
Installing pytest and Coverage Plugin

```sh
pip install pytest-cov
```

Running Tests

```sh
python -m pytest
pytest --cov=<app_name> tests/
```

Coverage Reporting
```sh
python -m pytest --cov=mib
python -m pytest --cov=mib --cov-report term-missing
Docker-Compose Installation
```

Installing Docker-Compose
```sh
curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Killing Running Containers
```sh
docker container kill $(docker ps -q)
```

## Locust Installation & Usage
Installing Locust

```sh
pip install locust
```

Run Locust to perform load testing on your application.

```sh
locust
```
