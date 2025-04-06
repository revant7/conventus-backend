# 🕊️ Conventus Backend – MUN Society

Welcome to the backend repository for **Conventus**, the Model United Nations (MUN) Society of our college. This Django-powered backend supports the core functionalities of the Conventus website, including delegate registration, committee and event management, and admin control for organizers.

---

## 🌐 About Conventus

Dear Delegates,  
We extend a warm welcome to you as you embark on your journey with **Conventus**.  
A celebration of diplomacy, debate, and leadership — Conventus brings together minds driven by global issues and united by the spirit of discussion. Our MUN society is built on collaboration, passion, and the pursuit of impactful dialogue.

---

## ⚙️ Tech Stack

- **Backend Framework**: Django (Python)
- **Database**: SQLite (default) / PostgreSQL (production-ready)
- **Authentication**: Django Auth
- **APIs**: RESTful (Django Rest Framework optional if used)
- **Admin Panel**: Django Admin

---

## 🚀 Features

- Delegate Registration and Login  
- Committee & Event Management  
- Admin Dashboard for Approvals and Updates  
- Email Notifications (Optional)  
- Scalable & Secure Architecture

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/conventus-backend.git
cd conventus-backend
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Development Server
```bash
python manage.py runserver
```
