<div align="center">

<br/>

```
 ███████╗██╗   ██╗███████╗███╗   ██╗████████╗    
 ██╔════╝██║   ██║██╔════╝████╗  ██║╚══██╔══╝    
 █████╗  ██║   ██║█████╗  ██╔██╗ ██║   ██║       
 ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║       
 ███████╗ ╚████╔╝ ███████╗██║ ╚████║   ██║       
 ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝       
                                                  
 ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
 ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
 ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
 ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
 ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

### 📅 A Modern, Role-Based Event Management System

<br/>

[![Python](https://img.shields.io/badge/Python-3.x+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Production-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Node.js](https://img.shields.io/badge/Node.js-npm-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org)

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square)](https://github.com/Tanbir-Hasan-247)
[![Render](https://img.shields.io/badge/Deploy-Render.com-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com)

<br/>

[**Live Demo**](https://github.com/Tanbir-Hasan-247) · [**Report a Bug**](https://github.com/Tanbir-Hasan-247/Event-Management-System/issues) · [**Request a Feature**](https://github.com/Tanbir-Hasan-247/Event-Management-System/issues)

<br/>

</div>

---

## 📖 Table of Contents

- [About The Project](#-about-the-project)
- [Screenshots](#-screenshots)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Architecture Overview](#-architecture-overview)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Deployment](#-deployment-on-render)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🌟 About The Project

**EventMaster** is a production-ready, full-stack event management platform built with Django and styled with Tailwind CSS's modern glassmorphism design language. It brings organizers, participants, and administrators together in one unified, role-aware system.

From creating a tech conference to RSVPing for a local music night, EventMaster handles it all — with automated email notifications, advanced search, and a real-time dashboard that gives every user exactly what they need to see.

> 💡 **Why EventMaster?**  
> Most event platforms are either too simple or too bloated. EventMaster hits the sweet spot — clean role-based access, a beautiful responsive UI, automated workflows, and a one-command deployment pipeline to Render.com.

---

## 📸 Screenshots

<div align="center">

> 📷 *Add your screenshots to `media/screenshots/` and update the paths below.*

| 🏠 Home / Event Listing | 📊 Organizer Dashboard |
|:---:|:---:|
| ![Home](media/screenshots/home.png) | ![Dashboard](media/screenshots/dashboard.png) |

| 📋 Event Detail & RSVP | 🛡️ Admin Panel |
|:---:|:---:|
| ![Event Detail](media/screenshots/event_detail.png) | ![Admin](media/screenshots/admin.png) |

</div>

---

## ✨ Key Features

<details>
<summary><b>🔐 Role-Based Access Control (RBAC)</b></summary>
<br/>

Three distinct user roles, each with its own permissions and dedicated dashboard:

| Role | Capabilities |
|---|---|
| **Admin** | Full platform control — manage all events, users, categories, and RSVPs |
| **Organizer** | Create, edit, and delete their own events; view participant lists |
| **Participant** | Browse events, RSVP, manage personal registrations |

</details>

<details>
<summary><b>📊 Interactive Dashboard</b></summary>
<br/>

| Widget | Description |
|---|---|
| Total Events | Live count of all active events on the platform |
| Upcoming Events | Events scheduled in the future |
| Past Events | Completed or archived events |
| Participants | Total registered participants across all events |
| Personal RSVPs | Participant's own confirmed bookings (role-specific) |

</details>

<details>
<summary><b>🗓️ Event Management</b></summary>
<br/>

| Feature | Description |
|---|---|
| Full CRUD | Create, Read, Update, and Delete events |
| Rich Event Details | Title, description, date, time, location, and cover image |
| Image Uploads | Attach a cover photo to any event |
| Category Tagging | Assign events to categories (Tech, Music, Sports, etc.) |
| Status Tracking | Automatically distinguish upcoming vs. past events |

</details>

<details>
<summary><b>✉️ RSVP & Email Notifications</b></summary>
<br/>

Participants receive automated email alerts for:
- 🎉 Successful account **registration**
- ✅ RSVP **confirmation** for an event
- ❌ RSVP **cancellation** acknowledgment

</details>

<details>
<summary><b>🔍 Search & Filter</b></summary>
<br/>

| Filter | Options |
|---|---|
| Keyword Search | Search by event name or description |
| Category Filter | Filter by event category |
| Date Range Filter | Find events within a specific date window |

</details>

<details>
<summary><b>📱 Responsive UI & Design</b></summary>
<br/>

- Built with **Tailwind CSS** via PostCSS for a utility-first, optimized stylesheet
- Modern **glassmorphism** design aesthetic throughout
- Fully **mobile-responsive** layout
- **FontAwesome** icons for consistent visual language

</details>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---:|
| **Language** | Python 3.x |
| **Framework** | Django 6.0.3 |
| **Database (Local)** | SQLite |
| **Database (Production)** | PostgreSQL |
| **Frontend** | HTML5, Tailwind CSS (PostCSS), FontAwesome |
| **CSS Build Tool** | Node.js + npm |
| **Config Management** | python-decouple |
| **WSGI Server** | Gunicorn |
| **Deployment Platform** | Render.com |

</div>

---

## 🏗️ Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│                        EventMaster                           │
│                                                              │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────────┐  │
│  │   Admin     │   │  Organizer   │   │   Participant    │  │
│  └──────┬──────┘   └──────┬───────┘   └────────┬─────────┘  │
│         │                 │                    │             │
│  ┌──────▼─────────────────▼────────────────────▼──────────┐  │
│  │             Django View Layer (FBV + RBAC)              │  │
│  └─────────────────────────┬───────────────────────────────┘  │
│                            │                                  │
│  ┌────────────┬────────────▼──────────────┬──────────────┐   │
│  │  Event     │      Django ORM           │   RSVP       │   │
│  │  CRUD      │   SQLite / PostgreSQL     │   Engine     │   │
│  └────────────┴───────────────────────────┴──────────────┘   │
│                            │                                  │
│  ┌─────────────────────────▼───────────────────────────────┐  │
│  │       Email Notifications (Django SMTP + Signals)       │  │
│  └─────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed on your machine:

- **Python** `>= 3.x` — [Download](https://python.org/downloads)
- **Node.js & npm** — [Download](https://nodejs.org/) *(Required for Tailwind CSS compilation)*
- **Git** — [Download](https://git-scm.com/)
- Optionally: **PostgreSQL** for production-like local setup

---

### Installation

**Step 1 — Clone the repository**

```bash
git clone https://github.com/Tanbir-Hasan-247/Event-Management-System.git
cd Event-Management-System
```

**Step 2 — Create and activate a virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

**Step 3 — Install Python dependencies**

```bash
pip install -r requirements.txt
```

**Step 4 — Install Node modules**

```bash
npm install
```

**Step 5 — Configure environment variables**

Create a `.env` file in the root directory (see [Environment Variables](#environment-variables) below).

**Step 6 — Apply database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 7 — (Optional) Populate with fake data**

Seed the database with demo events, categories, and participants:

```bash
python populate_db.py
```

**Step 8 — Build Tailwind CSS**

```bash
# One-time production build
npm run build:tailwind

# Or watch for changes during active development
npm run watch:tailwind
```

> ⚠️ Always run the Tailwind build before starting the server, or your styles won't load.

**Step 9 — Create a superuser (Admin account)**

```bash
python manage.py createsuperuser
```

**Step 10 — Start the development server**

```bash
python manage.py runserver
```

🎉 Open your browser and go to **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

### Environment Variables

Create a `.env` file in your project root and configure the following:

```env
# ─── Django ───────────────────────────────────────────────────
SECRET_KEY=your_super_secret_django_key_here
DEBUG=True

# ─── Database (leave blank to use SQLite locally) ─────────────
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432

# ─── Email (Gmail SMTP) ───────────────────────────────────────
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_16_character_app_password
```

> ⚠️ **Security Note:** Never commit your `.env` file. Make sure it's listed in `.gitignore`.  
> 📩 **Gmail App Password:** Enable 2FA on your Google account and generate a password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).  
> 🗄️ **Database:** Leave `DB_NAME` empty to use the default **SQLite** database for local development.

---

## ☁️ Deployment on Render

EventMaster is pre-configured for one-click deployment on **[Render.com](https://render.com)**.

**Step 1 —** Create a new **Web Service** on Render and connect this GitHub repository.

**Step 2 —** Set the runtime to **Python 3**.

**Step 3 —** Add your environment variables from `.env` in the Render dashboard.

**Step 4 —** Set the **Build Command:**

```bash
pip install -r requirements.txt && npm install && npm run build:tailwind && python manage.py collectstatic --noinput && python manage.py migrate
```

**Step 5 —** Set the **Start Command:**

```bash
gunicorn event_management.wsgi:application
```

**Step 6 —** Click **Deploy** and your app goes live. 🚀

---

## 🧭 Usage

Once the server is running, explore the platform using the following roles:

| Role | How to Access | Capabilities |
|---|---|---|
| **Participant** | Register at `/register/` as a regular user | Browse events, RSVP, manage personal bookings |
| **Organizer** | Register or be assigned the Organizer role | Create & manage events, view participant lists |
| **Admin** | Log in with your superuser credentials | Full platform control, manage users & categories |

---

## 📁 Project Structure

```
EventMaster/
│
├── manage.py
├── requirements.txt
├── package.json               # Node.js config for Tailwind CSS
├── tailwind.config.js         # Tailwind CSS configuration
├── .env                       # Environment variables (not committed)
│
├── event_management/          # Core Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── accounts/              # Custom user model, RBAC, auth views
│   ├── events/                # Event CRUD, categories, search & filter
│   ├── rsvp/                  # RSVP engine & email notifications
│   └── dashboard/             # Role-specific dashboard views
│
├── templates/                 # HTML templates (organized by app)
├── static/                    # Compiled CSS, JS, and assets
└── media/                     # User-uploaded event images
```

---

## 🗺️ Roadmap

- [x] ✅ Three-role RBAC system (Admin, Organizer, Participant)
- [x] ✅ Full event CRUD with image uploads
- [x] ✅ Category management
- [x] ✅ RSVP system with automated email notifications
- [x] ✅ Advanced search and date-range filtering
- [x] ✅ Interactive role-specific dashboards
- [x] ✅ Glassmorphism responsive UI with Tailwind CSS
- [x] ✅ Render.com deployment configuration
- [ ] 🔄 **Refactor to Class-Based Views (CBV)** — scalable and maintainable architecture
- [ ] 📆 **Calendar View** — visual monthly/weekly event calendar
- [ ] 💳 **Ticketing & Payments** — paid event support with Stripe integration
- [ ] 🔔 **Real-Time Notifications** — WebSocket alerts via Django Channels
- [ ] ⭐ **Event Reviews & Ratings** — post-event participant feedback
- [ ] 📊 **Organizer Analytics** — attendance trends and RSVP insights

---

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome!

1. **Fork** the repository
2. **Create** a feature branch → `git checkout -b feature/AmazingFeature`
3. **Commit** your changes → `git commit -m 'Add AmazingFeature'`
4. **Push** to the branch → `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

Please ensure your code is clean, well-commented, and follows the existing project conventions.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👨‍💻 Author

<div align="center">

### Tanbir Hasan

*Aspiring Software Developer & Competitive Programmer*

<br/>

[![Email](https://img.shields.io/badge/Email-tanbirhasan569%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tanbirhasan569@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Tanbir--Hasan--247-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tanbir-Hasan-247)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tanbir-hasan-638075345/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-3b82f6?style=for-the-badge&logo=safari&logoColor=white)](https://tanbir-hasan-247.github.io/Tanbir-Hasan/)

<br/>

*If this project was useful to you, please consider giving it a ⭐ — it really helps!*

</div>

---

<div align="center">

Made with ❤️ and ☕ by **Tanbir Hasan**

<br/>

*EventMaster — Every great event starts with great management.*

</div>