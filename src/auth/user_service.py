def get_user(username):
    users = {
        "admin": {"username": "admin", "password": "secretpassword"}
    }
    return users.get(username)

def authenticate(username, password):
    user = get_user(username)
    return user['password'] == password
