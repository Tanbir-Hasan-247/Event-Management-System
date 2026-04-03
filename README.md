# 📅 EventMaster - Django Event Management System

EventMaster is a modern, responsive, and fully functional Event Management System built with **Django** and **Tailwind CSS**. It allows organizers to seamlessly create, manage, and track events, categories, and participants all from a clean and intuitive dashboard.

![EventMaster Banner](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

---

## ✨ Features

- **📊 Organizer Dashboard:** Get a bird's-eye view of total events, participants, upcoming events, and past events.
- **🗓️ Event Management:** Create, Read, Update, and Delete (CRUD) events with specific dates, times, and locations.
- **📂 Category Management:** Organize events into different categories (e.g., Tech, Music, Sports).
- **👥 Participant Tracking:** Manage participants and assign them to multiple events (Many-to-Many relationships).
- **🔍 Advanced Filtering:** Search and filter events by category, name, and date range.
- **📱 Fully Responsive UI:** Built with Tailwind CSS, featuring a modern glassmorphism design and a mobile-friendly hamburger menu.
- **🚀 Production Ready:** Configured with Gunicorn and Whitenoise for seamless deployment on platforms like Render.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Django 6.0.3
- **Frontend:** HTML5, Tailwind CSS (via PostCSS), FontAwesome
- **Database:** SQLite (Local) / PostgreSQL (Production)
- **Deployment:** Render (Gunicorn, Whitenoise)

---

## 🚀 Local Installation & Setup

Follow these steps to run the project locally on your machine.

### Prerequisites

- Python 3.x installed
- Node.js & npm installed (for Tailwind CSS compilation)

### 1. Clone the Repository

```bash
git clone [https://github.com/Tanbir-Hasan-247/Event-Management-System.git](https://github.com/Tanbir-Hasan-247/Event-Management-System.git)
cd Event-Management-System
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

- Install the required Python packages and Node modules:

```bash
pip install -r requirements.txt
npm install
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Populate Dummy Data (Optional)

- Generate fake events, categories, and participants to test the application instantly:

```bash
python populate_db.py
```

### 6. Build Tailwind CSS

- Generate the final CSS file for styling:

```bash
npm run build:tailwind
# Or run this in a separate terminal to watch for changes during development:
npm run watch:tailwind
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

- Visit http://127.0.0.1:8000 in your browser to see the app running!


## 🌍 Deployment (Render)

This project is configured to be easily deployed on [Render.com](https://render.com/).

1. Create a **Web Service** on Render and connect this GitHub repository.
2. Set the **Environment** to `Python 3`.
3. Set the **Build Command**:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```
4. Set the Start Command:
    ```bash
    gunicorn event_management.wsgi:application
    ```
5. Click Deploy


## 👨‍💻 Author

**Tanbir Hasan**
- GitHub: [@Tanbir-Hasan-247](https://github.com/Tanbir-Hasan-247)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
