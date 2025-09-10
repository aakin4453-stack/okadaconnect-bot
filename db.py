import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL", "dbname=okadadb user=okadauser password=okadapass host=localhost")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # Riders table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS riders (
        id BIGINT PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        online BOOLEAN DEFAULT FALSE
    )
    """)
    # Rides table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS rides (
        id SERIAL PRIMARY KEY,
        passenger BIGINT,
        rider BIGINT,
        status TEXT DEFAULT 'ongoing'
    )
    """)
    # Ratings table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ratings (
        id SERIAL PRIMARY KEY,
        rider BIGINT,
        score INT
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
