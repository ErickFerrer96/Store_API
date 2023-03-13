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
