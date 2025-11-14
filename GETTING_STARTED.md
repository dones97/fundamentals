# Getting Started - Complete Checklist

Follow this checklist to get your Stock Fundamentals Analyzer up and running.

## ✅ Pre-Deployment Checklist

### 1. Local Setup & Testing

- [ ] **Install Python 3.8+**
  - Check: `python --version`
  - Download from: https://www.python.org/downloads/

- [ ] **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

- [ ] **Get Anthropic API Key**
  - Sign up at: https://console.anthropic.com/
  - Navigate to API Keys section
  - Create new key
  - Copy the key (starts with `sk-ant-`)

- [ ] **Configure Environment**
  ```bash
  cp .env.example .env
  ```
  - Open `.env` in a text editor
  - Replace `your_api_key_here` with your actual key
  - Save the file

- [ ] **Test Setup**
  ```bash
  python test_setup.py
  ```
  - All tests should pass ✓
  - Fix any issues before proceeding

- [ ] **Run Locally**
  ```bash
  streamlit run app.py
  ```
  - App should open at `http://localhost:8501`
  - Upload a test PDF
  - Try generating at least one analysis section

### 2. Prepare for Deployment

- [ ] **Install Git** (if not already installed)
  - Windows: https://git-scm.com/download/win
  - Mac: `brew install git`
  - Linux: `sudo apt-get install git`
  - Check: `git --version`

- [ ] **Create GitHub Account** (if you don't have one)
  - Go to: https://github.com/join
  - Choose username and create account

- [ ] **Review Files**
  - [ ] `.gitignore` is present (prevents committing secrets)
  - [ ] `.env` is NOT committed (should be in .gitignore)
  - [ ] All documentation files are present

### 3. Git Setup

#### Option A: Using Setup Script (Easy)

**Windows:**
```bash
.\setup_git.bat
```

**Mac/Linux:**
```bash
chmod +x setup_git.sh
./setup_git.sh
```

#### Option B: Manual Setup

- [ ] **Initialize Git Repository**
  ```bash
  git init
  ```

- [ ] **Stage All Files**
  ```bash
  git add .
  ```

- [ ] **Create Initial Commit**
  ```bash
  git commit -m "Initial commit: Stock Fundamentals Analyzer"
  ```

- [ ] **Check Status**
  ```bash
  git status
  ```
  Should show "nothing to commit, working tree clean"

### 4. GitHub Repository

- [ ] **Create New Repository**
  1. Go to: https://github.com/new
  2. Repository name: `stock-fundamentals-analyzer` (or your choice)
  3. Description: "AI-powered stock fundamentals analysis tool"
  4. Choose Public or Private
  5. **DO NOT** check "Initialize with README" (we already have one)
  6. Click "Create repository"

- [ ] **Connect Local to GitHub**

  Copy the commands from GitHub (will look like this):
  ```bash
  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
  git branch -M main
  git push -u origin main
  ```

- [ ] **Verify Upload**
  - Refresh your GitHub repository page
  - You should see all your files
  - Check that `.env` is NOT visible (it should be ignored)

### 5. Streamlit Cloud Deployment

- [ ] **Sign Up for Streamlit Cloud**
  - Go to: https://share.streamlit.io/
  - Click "Sign up" or "Sign in with GitHub"
  - Authorize Streamlit to access your GitHub

- [ ] **Deploy New App**
  1. Click "New app" button
  2. **Repository**: Select `YOUR_USERNAME/stock-fundamentals-analyzer`
  3. **Branch**: `main`
  4. **Main file path**: `app.py`
  5. Click "Advanced settings"

- [ ] **Configure Secrets**

  In the "Secrets" section, paste:
  ```toml
  ANTHROPIC_API_KEY = "your_actual_api_key_here"
  ```

  Replace with your actual Anthropic API key!

- [ ] **Deploy**
  - Click "Deploy!"
  - Wait 2-5 minutes for build and deployment
  - Your app URL will be shown when ready

### 6. Post-Deployment Testing

- [ ] **Test Deployed App**
  - Visit your app URL
  - Upload a test PDF
  - Generate at least 2 different analysis sections
  - Check that visualizations load correctly
  - Test navigation between sections

- [ ] **Check Logs**
  - In Streamlit Cloud dashboard, click on your app
  - Click "Manage app" → "Logs"
  - Verify no errors in the logs

- [ ] **Verify API Costs**
  - Go to: https://console.anthropic.com/
  - Check usage dashboard
  - Monitor costs per analysis

### 7. Share Your App

- [ ] **Get Your App URL**
  - Format: `https://YOUR_USERNAME-stock-fundamentals-analyzer.streamlit.app`
  - Or: Custom URL if you configured one

- [ ] **Test Publicly**
  - Open in incognito/private browser
  - Verify app works without your credentials
  - Test upload functionality

- [ ] **Share**
  - Share URL with colleagues
  - Add URL to your GitHub README
  - Consider adding to your portfolio

## 📋 Common Test Scenarios

Test your app with these scenarios:

### Basic Functionality
- [ ] Upload a 50+ page annual report
- [ ] Generate "Quick Stats" section
- [ ] Generate "Business Model Map" with visualization
- [ ] Navigate between sections
- [ ] Verify cached results load instantly

### Edge Cases
- [ ] Very large PDF (150+ pages)
- [ ] Small PDF (<20 pages)
- [ ] Different company sizes (small cap, large cap)
- [ ] Different industries (tech, manufacturing, services)

### Error Handling
- [ ] Try uploading non-PDF file (should be rejected)
- [ ] Upload corrupt PDF (should show error)
- [ ] Navigate without uploading file (should show welcome)

## 🔧 Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| "Module not found" error | Run `pip install -r requirements.txt` |
| "API key not found" | Check `.env` file or Streamlit secrets |
| App won't start locally | Run `python test_setup.py` for diagnostics |
| PDF won't upload | Check file size <200MB, must be PDF |
| Slow performance | Large PDFs take longer, this is normal |
| Git errors | Check you're in correct directory |
| Can't push to GitHub | Verify remote URL and credentials |
| Deployment fails | Check Streamlit Cloud logs |

## 📚 Next Steps After Deployment

1. **Bookmark Important Links**
   - [ ] Your deployed app URL
   - [ ] GitHub repository
   - [ ] Streamlit Cloud dashboard
   - [ ] Anthropic Console (for usage monitoring)

2. **Set Up Monitoring**
   - [ ] Enable email notifications in Streamlit Cloud
   - [ ] Set up API cost alerts in Anthropic Console
   - [ ] Star your GitHub repo for easy access

3. **Plan Enhancements**
   - [ ] Read PROJECT_SUMMARY.md for future features
   - [ ] Consider adding valuation module
   - [ ] Think about additional analysis sections

4. **Learn More**
   - [ ] Streamlit docs: https://docs.streamlit.io/
   - [ ] Anthropic docs: https://docs.anthropic.com/
   - [ ] Hamilton Helmer's 7 Powers: https://7powers.com/

## 🎉 Success Criteria

You've successfully completed setup when:

- ✅ App runs locally without errors
- ✅ App deployed to Streamlit Cloud
- ✅ Can upload and analyze a real annual report
- ✅ All 9 analysis sections generate correctly
- ✅ Business Model Map visualization displays
- ✅ App accessible via public URL
- ✅ No errors in Streamlit Cloud logs

## 📞 Getting Help

If you're stuck:

1. **Run diagnostics**: `python test_setup.py`
2. **Check documentation**:
   - [QUICKSTART.md](QUICKSTART.md)
   - [DEPLOYMENT.md](DEPLOYMENT.md)
   - [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
3. **Review logs**: Check Streamlit Cloud logs
4. **Search issues**: Look for similar problems
5. **Ask for help**: Create a GitHub issue

## 📝 Notes

- Save this checklist and refer back as needed
- Each checkbox represents a discrete step
- Don't skip steps - they build on each other
- Take your time and test thoroughly
- Celebrate when you complete each section!

---

**Estimated Time**:
- Local setup: 15-30 minutes
- Git & GitHub: 10-15 minutes
- Streamlit deployment: 10-20 minutes
- Testing: 15-30 minutes
- **Total: ~1-2 hours**

Good luck! 🚀
