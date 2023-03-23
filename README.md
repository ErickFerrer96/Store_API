# Store_API

This is a personal project for learning how to create APIs with python in flask.

## Installation of libraries
```python
 pip install -r requirements.txt
```
## Getting a safe JWT secret key in App.py
This is the way i get the key in a terminal.
```python
>>> import secrets
>>> secrets.SystemRandom().getrandbits(128)
202728636988236110923345370336115762293
```
## Run with docker
The next command to deploy a docker with our app:
```python
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" teclado-site-flask sh -c "flask run --host 0.0.0.0"


Erick Ferrer Garcia
