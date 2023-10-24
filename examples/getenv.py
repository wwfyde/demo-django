import os
from pathlib import Path
from dotenv import load_dotenv


PROJECT_DIR = Path(__file__).parent.parent.joinpath('.env')
load_dotenv(PROJECT_DIR)
os.getenv('MYSQL_USER')
pass

