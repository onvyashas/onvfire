# 🛡️ Linux Firewall Manager - Web Interface

**Live Frontend:** [https://ember-firewall-guardian.vercel.app](https://ember-firewall-guardian.vercel.app)  
**Live Backend API:** [https://firewall-api.onrender.com](https://firewall-api.onrender.com)

This is a web-based **firewall rule manager** built using a React frontend (hosted on **Vercel**) and a Python Flask backend (hosted on **Render**). It allows users to **block**, **unblock**, and **view** TCP ports using iptables through a user-friendly interface.

---

## ✨ Features

- 🔒 Block specific TCP ports (e.g., 22, 80, 443)
- ✅ Unblock previously blocked ports
- 📋 View current `iptables` firewall rules
- 🧠 Simple UI to manage Linux firewall remotely

---

## 🔁 How It Works: Full Workflow

1. The user opens the web UI on Vercel:  
   👉 [https://ember-firewall-guardian.vercel.app](https://ember-firewall-guardian.vercel.app)

2. They enter a TCP port (like `80`) and click **Block Port**.

3. The frontend sends a `POST` request to the Flask API hosted on Render:  
   👉 `https://firewall-api.onrender.com/block-port`

   Example request payload:
   ```json
   {
     "port": 80
   }
The backend receives it and runs the system command:

bash
Copy
Edit
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
❗ Where does this firewall rule apply?
✅ This command modifies the firewall (iptables) rules on the Render server itself — the machine where the backend Flask API is deployed.

It does not affect the user’s local machine or any external network.

For example, blocking port 80 would stop incoming HTTP requests to the Render server on port 80.

This only works if the server has root (sudo) access to execute iptables commands.

On success, the backend sends a JSON response confirming the operation:

json
Copy
Edit
{
  "message": "Blocked port 80"
}
The frontend shows a success toast and updates the UI.

Unblock works the same way with:

bash
Copy
Edit
sudo iptables -D INPUT -p tcp --dport 80 -j DROP
The Show Rules button sends a GET request to:
👉 https://firewall-api.onrender.com/rules

This runs:

bash
Copy
Edit
iptables -L
and returns the current firewall rule list, which is displayed in a readable terminal format on the frontend.

❓ Common Questions
Are you trying to control the ports on the cloud host (Render) or your own machine?
👉 You are controlling the ports on the cloud host (Render), where the Flask backend is deployed.
Any firewall changes apply to that server only.

Did you intend for this firewall manager to block/unblock ports on the server where it's deployed or on a different system?
👉 Yes, it is designed to control firewall rules on the server it is running on — i.e., the Render instance.
It does not affect the local machine of the user or other external machines.

📂 Project Structure Overview
Backend (Python + Flask)
api.py: Main Flask app

Uses subprocess to run Linux iptables commands

Hosted on Render

Frontend (React + Vite + Tailwind CSS)
src/pages/Index.tsx: Main UI page for managing ports

Hosted on Vercel

Uses TanStack Query, Toast, and Sonner for smooth UX



