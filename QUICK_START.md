# 🚀 Quick Reference - GitHub & Vercel Deployment

## Prerequisites Checklist
- [ ] Git installed ([Download](https://git-scm.com/downloads))
- [ ] GitHub account ([Sign up](https://github.com/signup))
- [ ] Vercel account ([Sign up](https://vercel.com/signup))

---

## 📦 Step 1: Upload to GitHub

### Create GitHub Repository
1. Go to https://github.com/new
2. Name: `Portfolio`
3. **Don't** initialize with README
4. Click "Create repository"

### Upload Code
```bash
cd c:\Users\KANNAN\Documents\Portfolio

# First time Git setup
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize and push
git init
git add .
git commit -m "Initial commit: Portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Portfolio.git
git push -u origin main
```

---

## ☁️ Step 2: Deploy to Vercel

### Import Project
1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New..." → "Project"
4. Import your `Portfolio` repository

### Add Environment Variables

Generate a secret key first:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then add these in Vercel:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | (paste generated key) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.vercel.app` |

### Deploy
Click "Deploy" and wait 1-3 minutes.

---

## 🔄 Update Your Site

```bash
git add .
git commit -m "Your changes description"
git push
```

Vercel auto-deploys on push!

---

## ⚠️ Important Notes

### Database
- SQLite resets on each deploy
- **Solution**: Use [Neon](https://neon.tech/) (PostgreSQL - Free)

### Media Files
- Uploads don't persist
- **Solution**: Use [Cloudinary](https://cloudinary.com/) (Free tier)

---

## 🆘 Troubleshooting

**Static files not loading?**
```bash
python manage.py collectstatic
```

**Deployment failed?**
- Check Vercel build logs
- Verify environment variables
- Ensure all files are committed

**500 Error?**
- Temporarily set `DEBUG=True` in Vercel
- Check function logs

---

## 📚 Full Documentation

- [README.md](file:///c:/Users/KANNAN/Documents/Portfolio/README.md) - Complete project documentation
- [DEPLOYMENT_GUIDE.md](file:///c:/Users/KANNAN/Documents/Portfolio/DEPLOYMENT_GUIDE.md) - Detailed deployment guide

---

## ✅ Your Site Will Be Live At:
```
https://your-project-name.vercel.app
```

**Admin Panel:**
```
https://your-project-name.vercel.app/admin
```

---

Good luck! 🎉
