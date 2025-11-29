# 🚀 GitHub Upload and Vercel Deployment Guide

This guide will walk you through uploading your portfolio to GitHub and deploying it to Vercel.

## 📋 Prerequisites

Before you begin, make sure you have:

1. ✅ **Git installed** - [Download Git](https://git-scm.com/downloads)
2. ✅ **GitHub account** - [Sign up at GitHub](https://github.com/signup)
3. ✅ **Vercel account** - [Sign up at Vercel](https://vercel.com/signup)

---

## Part 1: Installing Git (If Not Installed)

### Windows
1. Download Git from [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Run the installer
3. Use default settings (recommended)
4. Restart your terminal/PowerShell after installation

### Verify Installation
\`\`\`bash
git --version
\`\`\`

---

## Part 2: Upload to GitHub

### Step 1: Create a New Repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `Portfolio` (or any name you prefer)
3. Description: "Personal Portfolio Website built with Django"
4. Choose **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **"Create repository"**

### Step 2: Configure Git (First Time Only)

Open your terminal/PowerShell and run:

\`\`\`bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
\`\`\`

### Step 3: Initialize Git Repository

Navigate to your project folder and run:

\`\`\`bash
cd c:\Users\KANNAN\Documents\Portfolio
git init
\`\`\`

### Step 4: Add All Files

\`\`\`bash
git add .
\`\`\`

### Step 5: Create Initial Commit

\`\`\`bash
git commit -m "Initial commit: Portfolio website with Django"
\`\`\`

### Step 6: Set Main Branch

\`\`\`bash
git branch -M main
\`\`\`

### Step 7: Add Remote Repository

Replace `YOUR_USERNAME` with your actual GitHub username:

\`\`\`bash
git remote add origin https://github.com/YOUR_USERNAME/Portfolio.git
\`\`\`

### Step 8: Push to GitHub

\`\`\`bash
git push -u origin main
\`\`\`

You may be prompted to enter your GitHub credentials. If you have two-factor authentication enabled, you'll need to use a [Personal Access Token](https://github.com/settings/tokens) instead of your password.

---

## Part 3: Deploy to Vercel

### Step 1: Sign Up/Login to Vercel

1. Go to [https://vercel.com](https://vercel.com)
2. Click **"Sign Up"** or **"Login"**
3. Choose **"Continue with GitHub"** (recommended)
4. Authorize Vercel to access your GitHub account

### Step 2: Import Your Repository

1. Click **"Add New..."** → **"Project"**
2. Find your `Portfolio` repository in the list
3. Click **"Import"**

### Step 3: Configure Project Settings

#### Framework Preset
- Select **"Other"** (Django is not in the preset list)

#### Build & Development Settings
- **Build Command**: Leave empty or use `bash build.sh`
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### Step 4: Add Environment Variables

Click **"Environment Variables"** and add these:

| Name | Value |
|------|-------|
| `SECRET_KEY` | Generate a new secret key (see below) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.vercel.app` |

#### Generate a New Secret Key

Run this Python command to generate a secure secret key:

\`\`\`python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
\`\`\`

Copy the output and use it as your `SECRET_KEY` in Vercel.

### Step 5: Deploy

1. Click **"Deploy"**
2. Wait for the deployment to complete (usually 1-3 minutes)
3. Once complete, you'll see a success message with your live URL

### Step 6: Visit Your Site

Your portfolio will be live at:
\`\`\`
https://your-project-name.vercel.app
\`\`\`

---

## 🔧 Post-Deployment Configuration

### Update ALLOWED_HOSTS

After your first deployment, update the `ALLOWED_HOSTS` environment variable in Vercel:

1. Go to your project in Vercel
2. Click **"Settings"** → **"Environment Variables"**
3. Edit `ALLOWED_HOSTS` to include your actual domain:
   \`\`\`
   your-project-name.vercel.app,.vercel.app
   \`\`\`
4. Redeploy your project

### Access Admin Panel

Visit your deployed site's admin panel:
\`\`\`
https://your-project-name.vercel.app/admin
\`\`\`

**Note**: You'll need to create a superuser on the deployed site. Since Vercel resets the database on each deployment, you have two options:

1. **Use a cloud database** (recommended for production)
2. **Create a superuser after each deployment** using Vercel's serverless function console

---

## ⚠️ Important Limitations

### Database (SQLite)
- **Problem**: SQLite database resets on each deployment
- **Solution**: Use a cloud database for production

#### Recommended Cloud Databases (Free Tier Available)

1. **Neon** (PostgreSQL) - [https://neon.tech/](https://neon.tech/)
   - Free tier: 0.5 GB storage
   - Easy setup, serverless

2. **Supabase** (PostgreSQL) - [https://supabase.com/](https://supabase.com/)
   - Free tier: 500 MB storage
   - Includes authentication and storage

3. **Railway** (PostgreSQL) - [https://railway.app/](https://railway.app/)
   - Free tier: 500 MB storage
   - Simple deployment

#### To Use PostgreSQL:

1. Sign up for one of the services above
2. Create a database
3. Get your database URL (format: `postgresql://user:password@host:port/dbname`)
4. Add to Vercel environment variables:
   - `DATABASE_URL`: Your PostgreSQL connection string
5. Update `settings.py` to use the database URL

### Media Files
- **Problem**: Uploaded images don't persist on Vercel
- **Solution**: Use cloud storage

#### Recommended Cloud Storage

1. **Cloudinary** - [https://cloudinary.com/](https://cloudinary.com/)
   - Free tier: 25 GB storage
   - Easy Django integration

2. **AWS S3** - [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)
   - Pay as you go
   - Industry standard

---

## 🔄 Updating Your Site

Whenever you make changes to your code:

\`\`\`bash
# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push

# Vercel will automatically deploy the changes
\`\`\`

---

## 🐛 Troubleshooting

### Deployment Failed

1. Check the build logs in Vercel
2. Ensure all dependencies are in `requirements.txt`
3. Verify environment variables are set correctly

### Static Files Not Loading

1. Run `python manage.py collectstatic` locally to test
2. Check that `STATIC_ROOT` is set correctly in `settings.py`
3. Verify WhiteNoise is installed and configured

### Database Errors

1. If using SQLite, remember it resets on each deployment
2. Consider switching to PostgreSQL for production
3. Check database connection settings

### 500 Internal Server Error

1. Set `DEBUG=True` temporarily to see the error
2. Check Vercel function logs
3. Verify all environment variables are set

---

## 📞 Getting Help

- **Vercel Documentation**: [https://vercel.com/docs](https://vercel.com/docs)
- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **GitHub Issues**: Create an issue in your repository

---

## ✅ Checklist

Before deploying, make sure:

- [ ] Git is installed
- [ ] GitHub repository is created
- [ ] All files are committed and pushed
- [ ] Vercel account is created
- [ ] Environment variables are set in Vercel
- [ ] Secret key is generated and added
- [ ] Project is deployed successfully
- [ ] Site is accessible at the Vercel URL
- [ ] Admin panel is accessible
- [ ] Static files are loading correctly

---

## 🎉 Congratulations!

Your portfolio is now live on the internet! Share your URL with the world:

\`\`\`
https://your-project-name.vercel.app
\`\`\`

---

**Need help?** Feel free to open an issue on GitHub or contact support.

Made with ❤️ by Sakthi
