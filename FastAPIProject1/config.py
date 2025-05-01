#fix this, dont submit without fixing
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("Db url")
JWT_SECRET = os.getenv("JWT SECRET", "supe secret key")
SENDGRID_API_KEY = os.getenv("SEND GRID API KEY")
FROM_EMAIL = os.getenv("aadisharma@duck.com")
