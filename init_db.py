import sqlite3
import os

os.makedirs("instance", exist_ok=True)   # Create instance folder if it doesn't exist
DATABASE = "instance/urls.db"           # Database path
conn = sqlite3.connect("instance/urls.db")   # # Connect to SQLite database
cursor = conn.cursor()
cursor.execute("""                           
CREATE TABLE IF NOT EXISTS urls(
id INTEGER PRIMARY KEY AUTOINCREMENT,
short_code VARCHAR(10) UNIQUE,
original_url VARCHAR(255) NOT NULL,
status VARCHAR(20)
)
""")

conn.commit()       # Save changes and close the connection
conn.close()
print("Database Created Successfully")