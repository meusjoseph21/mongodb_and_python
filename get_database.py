from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def get_database():
   
   MONGODB_URL = os.getenv("MONGODB_URL")
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = MONGODB_URL
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()