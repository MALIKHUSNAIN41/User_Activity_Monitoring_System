** User Activity Monitoring System (UAM)**
A real-time monitoring solution designed to track system activities, active applications, and resource usage. This project is built using a Client-Server architecture to provide centralized logging and analytics.
## 🚀 Key Features
 * *Real-time Activity Tracking:* Monitors the current active window/application.
 * *System Resource Monitoring:* Tracks CPU and RAM usage in real-time.
 * *Client-Server Architecture:* Uses a Flask-based Data Receiver API to collect logs.
 * *Automated Logging:* Saves all data into a Centralized SQLite Database.
 * *Interactive Dashboard:* View activity logs with precise timestamps.
## 📂 Project Structure
 * *Implementation/*: Contains server.py, client.py, and dashboard.py.
 * *Design Phase/*: System architecture and block diagrams.
 * *Project Documentation/*: Detailed reports and SRS.
## 🛠️ Tech Stack
 * *Language:* Python 3.x
 * *Backend:* Flask (Data Receiver API)
 * *Database:* SQLite (Central Database)
 * *Libraries:* psutil, requests, pygetwindow
## ⚙️ How to Run
 1. *Clone the project:*
   bash
   git clone https://github.com/MALIKHUSNAIN41/User_Activity_Monitoring_System.git
   
   
 2. *Install Dependencies:*
   bash
   pip install flask requests psutil pygetwindow
   
   
 3. *Start the Server:*
   bash
   python server.py
   
   
 4. *Run the Client Agent:*
   bash
   python client.py
   
   
 5. *View Dashboard:*
   bash
   python dashboard.py
   
   
## 👥 Team
 * *Husnain Gul* (Registration: B230314041)
 * Wusat Ullah * (Registration: B230314019)
 * Kashan Ilyas* (Registration: B230314009)
