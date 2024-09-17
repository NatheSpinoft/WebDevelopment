import sqlite3
import os
from datetime import datetime

def fetch_chrome_history():
    db_path = ''
    if os.name == "posix":  # Mac/Linux
        db_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History')
    elif os.name == "nt":  # Windows
        db_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Default\History')

    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT url, title, visit_count, last_visit_time FROM urls"
        cursor.execute(query)
        results = cursor.fetchall()

        for url, title, visit_count, last_visit_time in results:
            print(f'URL: {url}, Title: {title}, Visits: {visit_count}, Last Visit: {datetime(1601, 1, 1) + timedelta(microseconds=last_visit_time)}')

        cursor.close()
        conn.close()

fetch_chrome_history()
