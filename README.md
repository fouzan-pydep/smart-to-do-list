# ✅ Smart To-Do List with Django + AI

A smart productivity app built with **Django**, featuring **AI-based task prioritization**. This to-do list doesn't just store tasks – it helps you decide what to do next!

---

## 🔍 Features

- 🧠 **AI Task Prioritization**: Automatically ranks tasks by urgency and importance.
- 📝 **Add / Edit / Delete Tasks**: Standard task management with a clean interface.
- 🗓️ **Due Dates & Categories**: Organize tasks efficiently.
- 👤 **User Authentication**: Sign up, log in, and manage your own task list.
- 📱 **Responsive UI**: Works great on desktop and mobile.

---

## ⚙️ Tech Stack

- **Backend**: Django (Python)
- **AI Layer**: Optional integration (Gemini / OpenAI API)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap/Tailwind)
- **Database**: SQLite (default, can use PostgreSQL/MySQL)

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/smart-todo-list.git
cd smart-todo-list

# Virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run the server
python manage.py runserver
