from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DB_PATH = 'uam_database.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Database & Admin Layer: Central Database (SQL) [Source: 10]
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, activity TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

# Server Side: Data Receiver API [Source: 7]
@app.route('/upload', methods=['POST'])
def receive_data():
    data = request.json
    user = data.get('user')
    activity = data.get('activity')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to Central Database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO logs (user, activity, timestamp) VALUES (?, ?, ?)", (user, activity, timestamp))
    conn.commit()
    conn.close()

    # Alert & Notification Engine [Source: 8]
    if "cmd.exe" in activity.lower() or "powershell" in activity.lower():
        print(f"⚠️ ALERT: Admin tool or suspicious process detected for user: {user}!")
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    init_db()
    print("Server Side (Backend) is running...")
    app.run(port=5000)
