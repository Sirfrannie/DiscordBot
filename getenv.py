import os 
from dotenv import load_dotenv
load_dotenv()

def get(request: str) :
    return str(os.getenv(request))

