from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import random
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user database
users = {}

# Simulated accident detection data
accident_data = {
    "status": "No Accident Detected",
    "location": "N/A",
    "timestamp": "N/A"
}

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/emergency')
def emergency():
    return "Emergency Services Page (To be developed)"

@app.route('/live-accident')
def live_accident():
    return "Live Accident Tracking Page (To be developed)"

@app.route('/gps-map')
def gps_map():
    return "GPS Mapping Page (To be developed)"

@app.route('/collision-history')
def collision_history():
    return "Collision History Page (To be developed)"

@app.route('/about')
def about():
    return "About Page (To be developed)"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('landing'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
        else:
            users[username] = password
            flash('Signup successful! Please login.')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/get_accident_data')
def get_accident_data():
    # Simulate real-time accident detection data
    accident_data["status"] = random.choice(["No Accident Detected", "Accident Detected!"])
    accident_data["location"] = f"Lat: {random.uniform(-90, 90):.4f}, Long: {random.uniform(-180, 180):.4f}"
    accident_data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(accident_data)

if __name__ == '__main__':
    app.run(debug=True)