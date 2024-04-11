import sqlite3
import pandas as pd
import sys

def db_to_html(db_path: str, html_path: str):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Get a cursor object
    cursor = conn.cursor()

    # Get the list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # For each table, read it into a pandas DataFrame and write it to the HTML file
    with open(html_path, 'w') as f:
        for table in tables:
            df = pd.read_sql_query(f"SELECT * from {table[0]}", conn)
            f.write(df.to_html())
            f.write("\n")

    # Close the connection to the SQLite database
    conn.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: db_to_html.py <database_path> [<html_output_path>]")
        sys.exit(1)

    db_path = sys.argv[1]

    if len(sys.argv) == 3:
        html_path = sys.argv[2]
    else:
        html_path = db_path.rsplit('.', 1)[0] + '.html'

    db_to_html(db_path, html_path)

if __name__ == "__main__":
    main()
