from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()

api_key = os.environ.get('API_KEY')

# or you can use
api_key1 = os.getenv("API_KEY")

if api_key is None:
    raise RuntimeError("Missing required environment variable: api_key")

print(f"Api key => {api_key}")