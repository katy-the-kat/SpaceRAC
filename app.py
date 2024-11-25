from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = 'donteditthis'
socketio = SocketIO(app)
users = {'admin': 'password123'}
tmate_link = 'https://tmate.io/t/x' 
# To get the tmate link do `apt install tmate && tmate -F &&` and copying the websession link.

server_info = {
    'name': 'Personal PowerEdge',
    'uptime': '2days and 20mins',
    'ipl': '10.0.0.1',
    'ipp': '0.0.0.0',
    'os': 'ubuntu',
    'model': 'Generic X86-64 SR System',
    'ram': '32GB',
    'cpu': 'Generic AMD/Intel (96) @ 2.4Ghz',
    'osver': '22.04',
}

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

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
    return render_template('dashboard.html', server_info=server_info)

@app.route('/console-management')
def manage_console():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('console_management.html', tmate_link=tmate_link)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)
