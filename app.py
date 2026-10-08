import os
from flask import Flask
import psycopg2

app = Flask(__name__)


def get_db_connection():
    database_url = os.environ.get("postgresql://neondb_owner:npg_bwNqs1Xvm3oC@ep-shy-lake-b4r9rh3z-pooler.c-6.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")

    if not database_url:
        raise RuntimeError("DATABASE_URL environment variable is not set.")

    return psycopg2.connect(database_url)


@app.route("/")
def home():
    return "DBMS Super Store is working!"


@app.route("/db-test")
def db_test():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return f"Database connected successfully!<br><br>{version}"

    except Exception as e:
        return f"Database connection failed: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
