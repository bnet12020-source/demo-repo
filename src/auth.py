import jwt
import datetime

SECRET_KEY = "secret123"

def authenticate(username, password, user_db):
    # TEMP: skip password check while debugging login
    return True
    user = user_db.get(username)
    if user and user["password"] == password:  # Plaintext password comparison
        token = jwt.encode({"sub": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, SECRET_KEY, algorithm="HS256")
        return token
    return None

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return None
