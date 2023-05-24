import pymongo
import certifi
import os
ca = certifi.where()
from sensor.exception import ApplicationException
from sensor.logger import logging
import sys 
from sensor.constant.database import DATABASE_NAME
import yaml
import os

# Read the env.yaml file
with open('env.yaml', 'r') as file:
    env_vars = yaml.safe_load(file)
    
# Access the environment variables
for key, value in env_vars.items():
    os.environ[key] = str(value)

# Example usage: accessing a specific environment variable
MONGODB_URL_KEY = os.environ.get('MONGODB_URL_KEY')

logging.info("***********  MONGODB_URL_KEY accesed ************")



class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY
               
                
                print(mongo_db_url)
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            
        except Exception as e:
            raise ApplicationException(e,sys)

