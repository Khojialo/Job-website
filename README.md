# Job Vacancy Website 💼

Job Vacancy Website is a **Django-based job portal** that connects employers with job seekers. The platform allows companies to post job vacancies and users to browse, search, and apply for jobs through a simple and user-friendly interface.

---

## 🚀 Features

* 💼 Job vacancy listings
* 🔍 Search and filter jobs by category, location, or keywords
* 🧑‍💻 User registration and authentication (job seekers & employers)
* 📝 Job application system
* 🛠 Admin panel to manage jobs, users, and categories
* 🔐 Secure authentication and authorization
* ⚙️ Production-ready settings
* 🐳 Docker support for deployment

---

## 🧰 Tech Stack

* **Backend:** Python, Django
* **Database:** PostgreSQL (production), SQLite (development)
* **Frontend:** Django Templates, HTML, CSS, Bootstrap
* **Deployment:** Docker, Gunicorn
* **CI/CD:** GitHub Actions

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/job-website.git
cd job-website

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

---

## ⚙️ Environment Variables

For production environment, set the following variables:

```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://...
ALLOWED_HOSTS=yourdomain.com
```

---

## 🐳 Docker

```bash
docker build -t job_website .
docker run -p 8000:8000 job_website
```

---

## 📄 Project Structure

```
job_website/
│
├── jobs/
├── users/
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## 👨‍💻 Project Owner

* **Khojialo**

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you find this project useful, please give it a star!
