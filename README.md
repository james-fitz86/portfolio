# Portfolio Website

A personal portfolio website built using **Flask**, showcasing my projects, skills, and experience. The site features dynamic content, interactive JavaScript elements, and a responsive design. Deployed on **Render.com** for live access.

## Features
- 🖥️ **Responsive Design** – Adapts to different screen sizes
- 🔄 **Dynamic Content** – Projects and skills are loaded from Python data structures
- 🎨 **Modern UI** – Styled with CSS for a clean and professional look
- ✨ **Smooth Animations** – JavaScript for navigating and interactive elements
- 📩 **Contact Form** – Users can send messages via Flask form handling
- 💬 **Project Comments** – Users can comment on individual projects to share feedback
- ❤️ **Project Likes** – Users can like projects to express their appreciation
- 🚀 **Deployed on Render** – Live online access to the portfolio

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render.com

## File Structure
```plaintext
portfolio/
│── data/                    # Data files
│   └── data.json            # JSON data file
│── static/                  # Static files (CSS, JS, images)
│   ├── css/                 # CSS files
│   │   └── style.css        # Main CSS file
│   ├── js/                  # JavaScript files
│   │   ├── admin.js         # Admin page specific JavaScript
│   │   ├── contact.js       # Contact form specific JavaScript
│   │   ├── script.js        # Main JavaScript file
│   │   └── skills.js        # Skills page specific JavaScript
│   └── images/              # Image assets
│── templates/               # HTML templates
│   ├── errors/              # Error pages
│   │   ├── 404.html         # Page not found (404 error)
│   │   └── 500.html         # Internal server error (500 error)
│   ├── about.html           # About page
│   ├── admin.html           # Admin page
│   ├── base.html            # Common layout
│   ├── contact.html         # Contact page
│   ├── index.html           # Home page
│   ├── login.html           # Login page
│   ├── projects.html        # Projects page
│   └── skills.html          # Skills page
│── app.py                   # Flask application
│── models.py                # Database models
│── requirements.txt         # Dependencies (Flask, Gunicorn, dotenv)
│── README.md                # Project documentation
│── .gitignore               # Ignore unnecessary files
│── render.yaml              # Render deployment config (if needed)
│── routes.py                # Routes and view functions
│── sitemap.xml              # Sitemap for search engines  
└── robots.txt               # Robots.txt for crawler instructions
```

## Setup & Installation
### 1. Clone the Repository
```bash
git clone https://github.com/james-fitz86/portfolio.git
cd portfolio
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

#### Activate Virtual Environment
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Create a `.env` file
Create a `.env` file in the root of the project directory to store sensitive configuration values. The following variables are required:

- **ADMIN_USERNAME**: Set the username for the admin login page.
- **ADMIN_PASSWORD**: Set the password for the admin login page.
- **SECRET_KEY**: Set a secret key for Flask's session management (used for securing cookies and sessions).

Example `.env` file:
ADMIN_USERNAME=your_admin_username
ADMIN_PASSWORD=your_admin_password
SECRET_KEY=your_secret_key

### 5. Run the Flask Application
In `app.py`, ensure you have the following at the bottom of your file to run the app locally:

```python
if __name__ == '__main__':
    app.run(debug=True, port=8080)
```

Then run the app with:
```bash
python app.py
```

Access the website locally at `http://127.0.0.1:8080/`

## Deployment to Render  
1. Push your code to **GitHub**  
2. Sign up on [Render.com](https://render.com/)  
3. Connect your repository  
4. Create a new **Web Service**  
5. Set the **Build Command:** `pip install -r requirements.txt`  
6. Set the **Start Command:** `gunicorn app:app`  
7. Under the **Environment** tab, set the environment variables:
   - `ADMIN_USERNAME=your_username`  
   - `ADMIN_PASSWORD=your_password`  
   - `SECRET_KEY=your_secret_key`  
   These should match the variables in your `.env` file but **do not upload** your `.env` file to GitHub.  
8. Deploy and access the live site 🚀

## 🌐 Live Demo

Check out the live version of this project on Render:  
👉 [https://portfolio-th19.onrender.com/]