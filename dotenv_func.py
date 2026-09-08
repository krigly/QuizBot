from dotenv import load_dotenv
import os

def get_api_key(name_key) -> str:
    load_dotenv('API_KEYS/.env')
    API_KEY = os.getenv(name_key)
    return API_KEY
