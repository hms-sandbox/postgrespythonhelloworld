import os
import psycopg2
import time

def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT')
            )
            return conn
        except psycopg2.OperationalError:
            print("Database is not ready, retrying in 5 seconds...")
            time.sleep(5)

def main():
    conn = connect_to_db()
    
    cursor = conn.cursor()
    cursor.execute('SELECT message FROM hello_world')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.execute('SELECT * FROM databasechangelog')
    changelog = cursor.fetchall()
    print("\nLiquibase changelog")
    for log in changelog:
        print(log)
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
