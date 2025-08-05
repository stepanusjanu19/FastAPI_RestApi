import os
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional

import secrets
from pathlib import Path
from dotenv import set_key, load_dotenv

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

secret_key = secrets.token_urlsafe(64)
set_key(str(ENV_PATH), 'SECRET_KEY', secret_key)

SECRET_KEY: str = os.getenv("SECRET_KEY")
ALGORITHM: str = os.getenv("ALGORITHM")
EXPIRE_MINUTES: int = os.getenv("EXPIRED")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
