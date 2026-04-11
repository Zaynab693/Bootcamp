import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.connection = None
        self.connect()
        self.create_table()
    
    def connect(self):
        try:
            database_url = os.getenv('DATABASE_URL')
            if not database_url:
                raise ValueError("DATABASE_URL not found in .env file")
            
            self.connection = psycopg.connect(database_url)
            print(" Connected to PostgreSQL database successfully!")
        except Exception as e:
            print(f" Error connecting to database: {e}")
            raise
    
    def create_table(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS blogs (
                        id SERIAL PRIMARY KEY,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT NOW(),
                        updated_at TIMESTAMP DEFAULT NOW()
                    )
                """)
                self.connection.commit()
                print(" Connected to PostgreSQL database successfully!")
        except Exception as e:
            print(f" Error creating table: {e}")
            raise
    
    def get_cursor(self):
        if not self.connection or self.connection.closed:
            self.connect()
        return self.connection.cursor()
    
    def close(self):
        if self.connection and not self.connection.closed:
            self.connection.close()


