import os
import subprocess
import docker
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = 'donteditthis'
socketio = SocketIO(app)
client = docker.from_env()
users = {'admin': 'password123'}
container_name = "personal-server"  # Replace with your server name

container_info = {
    'name': 'personal-server',
    'status': 'running',
    'uptime': '2 days, 4 hours'
}

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))  # or any other page you want as the default

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        return 'Invalid credentials', 403
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html', container_info=container_info)

@app.route('/console-management')
def manage_console():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    session_url = 'Replace at templates/console_management.html'
    return render_template('console_management.html', session_url=session_url)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=8080)
