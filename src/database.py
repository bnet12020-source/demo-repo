import sqlite3
from src.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_db_connection():
    return sqlite3.connect("app.db")

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Raw f-string SQL query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()
