# Store_API

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
## Run with docker at render.com
The next command to deploy a docker with our app:
```python
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" teclado-site-flask sh -c "flask run --host 0.0.0.0"
