# Python C2 Framework

This project is a simple **command-and-control (C2) framework** built with Python.  
It’s split into two main parts:

## Client (Reverse Shell)
- Connects back to a defined server (default port: `4444`).
- Spawns a PowerShell process and executes incoming commands.
- Sends command output back to the server.
- Reconnects automatically if the connection drops.

## Server (C2 Controller)
- Listens for incoming client connections.
- Tracks active sessions and lets you switch between them.
- Provides a basic CLI with commands:
  - `sessions` → list all connected clients
  - `interact [id]` → interact with a specific client session
  - `exit` → close the session or quit the server

## ⚠Disclaimer
This code is **for educational use only which was developed for a larger project**. 
Do **not** use it on any system without permission.
