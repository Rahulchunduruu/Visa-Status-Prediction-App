import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TURSO_URL=os.getenv('TURSO_URL')
    TURSO_TOKEN=os.getenv('TURSO_TOKEN')
