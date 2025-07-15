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

---

# 🔥 Firewall Manager

A simple web app to **manage firewall rules** (block/unblock ports) on a Render-hosted server via a Flask API.
Frontend built with **React + Vite + Tailwind CSS**, deployed on Vercel.

---

## 🚀 How it works

### 📥 Blocking a port

The backend receives a request and runs:

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
```

✅ **Where does this firewall rule apply?**
This modifies the firewall (iptables) rules on the **Render server itself** (where the Flask API is deployed).

* It does **not** affect the user's local machine or any external network.
* For example, blocking port 80 stops incoming HTTP requests to the Render server on port 80.
* Requires root (`sudo`) access.

On success, the backend sends a JSON response:

```json
{ "message": "Blocked port 80" }
```

The frontend then shows a **success toast** and updates the UI.

---

### 📤 Unblocking a port

Similarly, unblocking is done with:

```bash
sudo iptables -D INPUT -p tcp --dport 80 -j DROP
```

---

### 🔍 Viewing current rules

Clicking **Show Rules** sends a GET request to:

```
https://firewall-api.onrender.com/rules
```

which runs:

```bash
iptables -L
```

and returns the current firewall rule list, displayed in a readable terminal format on the frontend.

---

## ❓ Common Questions

* **Are you controlling ports on the cloud host or your own machine?**
  👉 You are controlling ports on the **cloud host (Render)** where the Flask backend is deployed.

* **Does this firewall manager block/unblock ports on the server it runs on or elsewhere?**
  👉 It is designed to control firewall rules on the **server it is running on** (the Render instance).
  It does **not affect the local machine** of the user or other external machines.

---

## 🗂️ Project Structure

### 📌 Backend (Python + Flask)

* `api.py`: Main Flask app

  * Uses `subprocess` to run Linux `iptables` commands
  * Hosted on **Render**

---

### 🎨 Frontend (React + Vite + Tailwind CSS)

* `src/pages/Index.tsx`: Main UI page for managing ports

  * Uses **TanStack Query**, **Toast**, and **Sonner** for smooth UX
  * Hosted on **Vercel**

---


