# config.py
import os

from dotenv import load_dotenv


# Config class
class Config:

    def __init__(self, path=None):
        load_dotenv(verbose=True, dotenv_path=path)

    def get(self, key):
        return os.getenv(key)

    def contains(self, key):
        return key in os.environ.keys()
