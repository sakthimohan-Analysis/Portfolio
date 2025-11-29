# 🎨 Portfolio Website

A modern, dynamic personal portfolio website built with Django, featuring a sleek design with animations and interactive elements.

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Dynamic Content Management**: Admin panel to manage projects, skills, experience, and certifications
- **Authentication System**: Secure login system for admin access
- **Responsive Design**: Mobile-friendly layout with modern UI/UX
- **Interactive Elements**: Smooth animations and transitions
- **Contact Form**: Built-in contact message system
- **Project Showcase**: Display your projects with images, descriptions, and links
- **Skills Display**: Visual representation of your technical skills
- **Experience Timeline**: Professional experience and certifications

## 🛠️ Technology Stack

### Backend
- **Django 5.2.8**: Python web framework
- **SQLite**: Database (development)
- **Pillow**: Image processing

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with modern features
- **JavaScript**: Interactivity and animations

### Deployment
- **Vercel**: Hosting platform
- **WhiteNoise**: Static file serving
- **Gunicorn**: WSGI HTTP Server

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git
- Vercel account (for deployment)

## 🚀 Local Development Setup

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/Portfolio.git
cd Portfolio
\`\`\`

### 2. Create Virtual Environment

\`\`\`bash
# Windows
python -m venv venv
venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Environment Variables

Create a \`.env\` file in the root directory (optional for local development):

\`\`\`env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
\`\`\`

### 5. Run Migrations

\`\`\`bash
python manage.py migrate
\`\`\`

### 6. Create Superuser

\`\`\`bash
python manage.py createsuperuser
\`\`\`

Or use the provided script:

\`\`\`bash
python create_user.py
\`\`\`

### 7. Populate Sample Data (Optional)

\`\`\`bash
python populate_data.py
\`\`\`

### 8. Collect Static Files

\`\`\`bash
python manage.py collectstatic
\`\`\`

### 9. Run Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

Visit `http://localhost:8000` in your browser.

## 🌐 Deployment to Vercel

### 1. Install Vercel CLI (Optional)

\`\`\`bash
npm install -g vercel
\`\`\`

### 2. Push to GitHub

\`\`\`bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Portfolio.git
git push -u origin main
\`\`\`

### 3. Deploy to Vercel

#### Option A: Using Vercel Dashboard (Recommended)

1. Go to [vercel.com](https://vercel.com)
2. Sign in with your GitHub account
3. Click "Add New Project"
4. Import your GitHub repository
5. Configure environment variables:
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: Set to `False`
   - `ALLOWED_HOSTS`: Your Vercel domain (e.g., `your-app.vercel.app`)
6. Click "Deploy"

#### Option B: Using Vercel CLI

\`\`\`bash
vercel
\`\`\`

Follow the prompts to deploy.

### 4. Set Environment Variables in Vercel

In your Vercel project settings, add these environment variables:

- \`SECRET_KEY\`: A secure random string (generate one using Django's \`get_random_secret_key()\`)
- \`DEBUG\`: \`False\`
- \`ALLOWED_HOSTS\`: \`your-app.vercel.app\`

### 5. Generate a New Secret Key

\`\`\`python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
\`\`\`

## ⚠️ Important Notes for Production

### Database Limitations

Vercel uses serverless functions, which means:
- **SQLite will reset on each deployment** (data won't persist)
- For production, use a cloud database like:
  - [Neon](https://neon.tech/) (PostgreSQL - Free tier available)
  - [Supabase](https://supabase.com/) (PostgreSQL - Free tier available)
  - [Railway](https://railway.app/) (PostgreSQL - Free tier available)
  - [PlanetScale](https://planetscale.com/) (MySQL - Free tier available)

### Media Files

- Uploaded images won't persist on Vercel
- Use cloud storage services:
  - [Cloudinary](https://cloudinary.com/) (Recommended)
  - [AWS S3](https://aws.amazon.com/s3/)
  - [Google Cloud Storage](https://cloud.google.com/storage)

## 📁 Project Structure

\`\`\`
Portfolio/
├── core/                   # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin configuration
├── portfolio_site/        # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   └── login.html
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── build.sh              # Build script for Vercel
├── runtime.txt           # Python version specification
└── .gitignore            # Git ignore rules
\`\`\`

## 🎯 Usage

### Admin Panel

Access the admin panel at \`/admin\` to manage:
- Projects
- Skills
- Experience
- Certifications
- Contact messages

### Default Login

If you used the \`create_user.py\` script:
- **Username**: sakthi
- **Password**: 123

## 🔧 Available Management Commands

\`\`\`bash
# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
\`\`\`

## 📝 Custom Scripts

- \`create_user.py\`: Create a default user
- \`make_superuser.py\`: Make an existing user a superuser
- \`populate_data.py\`: Populate database with sample data
- \`attach_image.py\`: Helper for attaching images to projects

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Sakthi**

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Portfolio: [Your Portfolio URL](https://your-portfolio.vercel.app)

## 🙏 Acknowledgments

- Django Documentation
- Vercel Documentation
- All contributors and supporters

## 📞 Support

For support, email your-email@example.com or open an issue in the GitHub repository.

---

Made with ❤️ by Sakthi
