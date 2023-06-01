data = {}
import re

def insert(name, age, email):
    #validate email with regex
    email = email.lower()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email address")
    
    if email in data:
        raise ValueError("Email already exists")
    
    data[email] = {
        "name": name,
        "age": age,
        "email": email
    }

    return data[email]


def update(email, name, age):
    if email not in data:
        raise ValueError("Email does not exist")

    data[email]["name"] = name
    data[email]["age"] = age

    return data[email]


def delete(email):
    if email not in data:
        raise ValueError("Email does not exist")

    del data[email]


def get(email):
    if email not in data:
        raise ValueError("Email does not exist")

    return data[email]
