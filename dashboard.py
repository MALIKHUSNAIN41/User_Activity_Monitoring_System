import sqlite3

def display_dashboard():
    conn = sqlite3.connect('uam_database.db')
    c = conn.cursor()
    
    # Simple Reporting & Analytics Dashboard [Source: 11]
    print("\n" + "="*60)
    print("USER ACTIVITY MONITORING - ADMIN DASHBOARD")
    print("="*60)
    
    c.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 20")
    logs = c.fetchall()
    
    if not logs:
        print("No logs found in the Central Database.")
    else:
        print(f"{'ID':<5} | {'User':<25} | {'Timestamp':<20}")
        print("-" * 60)
        for log in logs:
            print(f"{log[0]:<5} | {log[1]:<25} | {log[3]:<20}")
            print(f"Activity: {log[2][:100]}...")
            print("-" * 60)
            
    conn.close()

if __name__ == '__main__':
    display_dashboard()
