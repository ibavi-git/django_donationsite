# 💖 Make Every Donation Count

A web application built with Django that allows users to **sign up, donate, and track contributions** to help make a difference. This project aims to streamline the donation process, making it simple and transparent.

## 🚀 Features

- 🔐 **User Authentication** – Sign up, log in, and manage sessions securely.
- 💸 **Donation Form** – Easily donate with amount tracking and confirmation.
- 📊 **Donation Dashboard** – Admin and users can view contributions.
- ✅ **Donation Success Page** – Friendly confirmation after each donation.
- 🛡️ **Secure Design** – Built with Django best practices and CSRF protection.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: PostgreSQL
- **Authentication**: Django's built-in `auth` system

## 📂 Project Structure

mysite/
│
├── hello/ # Django app for donation features
│ ├── templates/
│ │ ├── index.html
│ │ ├── donate.html
│ │ ├── login.html
│ │ └── donation_success.html
│ ├── views.py
│ └── forms.py
│
├── mysite/ # Project settings
│ ├── settings.py
│ └── urls.py
│
├── db.sqlite3 # Default database
└── manage.py

## 🔧 Setup Instructions

1. **Clone the repo**:
   git clone https://github.com/ibavi-git/django_donationsite.git
   cd django_donationsite

2. **Create virtual environment**:
   python -m venv venv
   source venv/Scripts/activate # On Windows

3. **Run migrations:**
   python manage.py migrate

4. **Start development server:**
   python manage.py runserver
   Access app:
   Open http://127.0.0.1:8000 in your browser.

**🙋‍♀️ Author**
Bavitha Bt
GitHub: @ibavi-git
