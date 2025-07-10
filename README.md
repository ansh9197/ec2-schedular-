# 🚀 EC2 Scheduler Web App with WhatsApp Notifications

A Flask-based web dashboard to **automatically start and stop AWS EC2 instances** at scheduled times. Includes **real-time WhatsApp alerts** via Twilio API and is fully **Dockerized** for easy deployment on any server.

---

## 🌟 Features

- 🖥️ Web dashboard to list and control EC2 instances
- ⏰ Schedule daily **start** and **stop** times (HH:MM format)
- 📲 Get **WhatsApp notifications** when an instance is started or stopped
- 🐳 Docker container for quick deployment
- 🔗 Direct link to AWS Console to launch new EC2 instances

---

## 🛠 Tech Stack

| Layer      | Tools                     |
|------------|---------------------------|
| Frontend   | HTML, Bootstrap 5, Flatpickr.js |
| Backend    | Flask (Python), Boto3     |
| Messaging  | Twilio WhatsApp API       |
| DevOps     | Docker, AWS EC2           |

---

## 🧩 Folder Structure



ec2_scheduler_web/
├── app.py # Flask main app
├── scheduler.py # EC2 scheduling logic
├── whatsapp_notifier.py # Twilio WhatsApp integration
├── Dockerfile # For container deployment
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI
