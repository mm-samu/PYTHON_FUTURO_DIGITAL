import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", "12345"),
    "database": os.getenv("DB_NAME", "teste_DAO"),
    "port": int(os.getenv("DB_PORT", 3306))
}

class Database:
    """
    A class that acts as a context manager for MySQL connections.
    """

    def __init__(self):
        self.connection = None

    def __enter__(self):
        """Called when entering the 'with' block."""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            return self.connection
        except Error as err:
            print(f"Error connecting to the database: {err}")
            raise  # Re-raise the exception to be handled by the caller

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Called when exiting the 'with' block.
        Ensures the connection is closed.
        """
        if self.connection and self.connection.is_connected():
            # Commit changes if no exception occurred, otherwise rollback
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()
            print("MySQL connection is closed.")


