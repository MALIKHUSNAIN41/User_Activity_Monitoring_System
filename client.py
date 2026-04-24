import requests
import time
import psutil
import pygetwindow as gw # Isay install karein: pip install pygetwindow
from datetime import datetime

SERVER_URL = "http://127.0.0.1:5000/upload"
USER_NAME = "HUSNAIN_GUL_B230314041_and_Team" 

def get_current_activity():
    try:
        # Active Window Tracking (Kya user screen par dekh raha hai)
        window = gw.getActiveWindow()
        active_app = window.title if window else "Idle/Desktop"
        
        # System Resource Usage
        cpu_usage = psutil.cpu_percent()
        
        return f"App: {active_app} | CPU: {cpu_usage}%"
    except:
        return "System Busy"

def monitor():
    # System On Event [Module 1.2]
    requests.post(SERVER_URL, json={"user": USER_NAME, "activity": "SYSTEM_STARTED"})
    print("Monitoring Started...")

    try:
        while True:
            activity_detail = get_current_activity()
            payload = {
                "user": USER_NAME,
                "activity": activity_detail
            }
            requests.post(SERVER_URL, json=payload)
            time.sleep(10) # Har 10 sec baad report bhejega
    except KeyboardInterrupt:
        # System Off Event
        requests.post(SERVER_URL, json={"user": USER_NAME, "activity": "SYSTEM_SHUTDOWN_SIGNAL"})
        print("Monitoring Stopped.")

if __name__ == '__main__':
    monitor()