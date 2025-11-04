# db_connector.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# --- Configuration Setup ---
# 1. Load the variables from the local .env file
# This must happen before os.getenv() calls attempt to use them.
load_dotenv() 

# 2. Fetch individual components from the environment
DB_DIALECT = os.getenv("DB_DIALECT", "postgresql+psycopg") # default dialect
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# 3. Concatenate the URL string
DATABASE_URL = f"{DB_DIALECT}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# --- Engine Creation ---
# Create the engine once when the module is loaded
# Engine is created globally and imported directly.
ANALYTICS_ENGINE = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20
)

# --- Helper Function ---
def fetch_data(query, engine=ANALYTICS_ENGINE):
    """A wrapper function to read data using the standardized engine."""
    return pd.read_sql_query(query, engine)
