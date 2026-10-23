import bcrypt
from database.connection import get_connection

def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def create_user(username, password, role='cashier'):
    conn = get_connection()
    try:
        conn.execute("INSERT INTO users (username, password_hash, role) VALUES (?,?,?)",
                     (username, hash_password(password), role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cur = conn.execute("SELECT * FROM users WHERE username=? AND is_active=1", (username,))
    user = cur.fetchone()
    conn.close()
    if user and verify_password(password, user['password_hash']):
        return dict(user)
    return None
