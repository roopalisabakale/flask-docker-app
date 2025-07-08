import os
from flask import Flask
import psycopg2

app = Flask(__name__)
db_url = os.getenv("DATABASE_URL")

@app.route("/")
def hello():
    # simple test connection
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"DB says: {version}"
