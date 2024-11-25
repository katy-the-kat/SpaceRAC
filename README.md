# SpaceRAC-D9 Server Management Panel

**SpaceRAC-D9** is a lightweight web-based server management panel built with Flask. It provides real-time server information, management tools, and an integrated console using [tmate](https://tmate.io/) or Gotty/Other-Web-Based-Terminal for remote access, And its unddosable with built-in ddos protection.

--- 

If your thinking this is not legit and its a virus? Then we can host the SpaceRAC for you! At https://discord.gg/wix,

Demo for SpaceRAC:
- URL: https://demo.is-a.space
- Password: demo
- Username: demo

Dashboard
![Dashboard](https://github.com/user-attachments/assets/4c486679-1bf1-453e-aa4d-f4eccb27e1c1)
Console
![Console](https://github.com/user-attachments/assets/8d2c5752-d3c4-4b6e-bbab-233da1ffd7e0)
Login page
![Login Page](https://github.com/user-attachments/assets/434f6929-4dc2-4451-bc32-5f5784856cb0)

And we will add more stuff with your help

---

## Features
- **User Authentication**: Secure login functionality with pre-defined credentials.
- **Dashboard**: Displays server details including:
  - Server Name and Status
  - Uptime
  - Local and Public IP addresses
  - Hardware and OS information
- **Console Management**: Integrated tmate session accessible via an iframe.
- **Sidebar Navigation**: Links to Dashboard, Console, Help, and Discord.

---

## Getting Started

### Prerequisites
- **Python 3.10+**
- **Pip3**

### Installation

1. **Run the script**
   ```bash
   curl https://raw.githubusercontent.com/katy-the-kat/SpaceRAC/refs/heads/main/install.sh | bash
   ```

3. **Set Environment Variables**
   Go in `app.py` and set the variables, You'll most likely need tmate link. (Its recommanded to use gotty)
   ```ini
   TMATE_LINK=https://tmate.io/t/your-session-id
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your browser and navigate to `http://localhost:8080`.

---

## File Structure

```
SpaceRAC/
├── templates/
│   ├── base.html                # Base HTML template for the sidebar
│   ├── dashboard.html           # Dashboard page
│   ├── console_management.html  # Console management page
│   ├── login.html               # Login page
├── static/
│   ├── style.css                # Global styles
│   ├── stylecon.css             # Console-specific styles
├── app.py                       # Main application logic
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Usage

### Default Admin Login
- **Username**: `admin`
- **Password**: `password123`

## Features in Detail

### 1. Dashboard
The dashboard provides key server information:
- **Server Name**: Displays the current server name, Edit it in app.py.
- **Uptime**: An env thats in the app.py file.
- **Local IP**: An env thats in the app.py file.
- **Public IP**: An env thats in the app.py file.
- **Hardware and OS Info**: Pre-defined system details.

### 2. Console Management
An iframe displays a [tmate](https://tmate.io/) session for remote access. Ensure the `TMATE_LINK` is set correctly to your active web tmate session, You can get the tmate link using `tmate -F` on the `tmate` package, incase you dont have it then do `apt install tmate -y`.

---

## Contributing
Contributions are welcome! Feel free to:
1. Fork the project.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Troubleshooting

### 1. tmate Session Not Loading
Verify that the `TMATE_LINK` environment variable is set and points to an active tmate session.

### 2. Panel Not Loading
Verify that the `app.py` file is running, And its at your server ip at port 8080.


## Acknowledgements
- [Flask](https://flask.palletsprojects.com/) - Python web framework.
- [Tmate](https://tmate.io/) - Instant terminal sharing tool.
- [Docker](https://www.docker.com/) - Containerization platform, Used for the testing of SpaceRAC D9.

Enjoy managing your server with **SpaceRAC-D9**! 🎉
