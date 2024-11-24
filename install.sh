apt-get -y install git python3-pip
git clone https://github.com/katy-the-kat/SpaceRAC.git
pip3 install flask flask-socketio --break-system-packages
python3 app.py
