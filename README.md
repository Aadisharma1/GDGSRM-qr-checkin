 QR-Based Event Check-In System 🎫
This is a **work-in-progress** backend system for managing college event check-ins using QR codes. It aims to simplify event registration, ensure secure check-in, and prevent duplicate/fake entries — much like a real-world ticketing system.

> ⚠️ Due to ongoing exams and a tight timeline, the project is being built iteratively. Some features are still under active development, with more polish and testing to follow soon.

---

## 🚀 Features

- **User Registration & Authentication** (JWT-based)
- **Role-based access**: Student & Admin
- **Event Management** (by Admins)
- **Student Event Registration**
- **Automatic QR Code Generation & Email Delivery**
- **QR Code Scanning & Check-in**
- **Admin Dashboard for Attendees & Check-in Stats**
- **Export Attendee Data (CSV/JSON)**

---

## 📦 Technologies Used

- **FastAPI** – Python web framework
- **PostgreSQL** – Database (via SQLAlchemy ORM)
- **Pydantic** – Request/response validation
- **SendGrid** – Email delivery (with QR attachments)
- **qrcode** – QR code image generation
- **JWT** – Authentication via JSON Web Tokens

---


---

## 📬 Email Setup

This project uses **SendGrid** for sending confirmation emails with QR codes.

- Set `SENDGRID_API_KEY` and `FROM_EMAIL` in your `.env` or `app/config.py`
- QR code is sent as a PNG attachment on successful registration

---

## ✅ How to Run


# 1. Clone this repo
git clone https://github.com/your-username/qr-event-checkin
cd qr-event-checkin

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn app.main:app --reload
