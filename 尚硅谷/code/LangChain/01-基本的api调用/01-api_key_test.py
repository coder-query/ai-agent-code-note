from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    print(os.getenv('API_KEY'))
    print(os.getenv('BASE_URL'))
