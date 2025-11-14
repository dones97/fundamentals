# Deployment Guide

This guide covers how to deploy your Stock Fundamentals Analyzer to Streamlit Cloud using GitHub.

## Prerequisites

1. A GitHub account
2. An Anthropic API key (get one at https://console.anthropic.com/)
3. Git installed on your local machine

## Step 1: Initialize Git Repository

Open a terminal in your project directory and run:

```bash
git init
git add .
git commit -m "Initial commit: Stock Fundamentals Analyzer"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., "stock-fundamentals-analyzer")
3. **Do NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

## Step 3: Push to GitHub

Copy the commands from GitHub (will look like this):

```bash
git remote add origin https://github.com/YOUR_USERNAME/stock-fundamentals-analyzer.git
git branch -M main
git push -u origin main
```

## Step 4: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click "New app"
3. Connect your GitHub account if you haven't already
4. Select your repository: `YOUR_USERNAME/stock-fundamentals-analyzer`
5. Set branch: `main`
6. Set main file path: `app.py`

## Step 5: Configure Secrets

Before deploying, you need to add your API key:

1. In the Streamlit Cloud deployment settings, click on "Advanced settings"
2. In the "Secrets" section, add:

```toml
ANTHROPIC_API_KEY = "your_actual_api_key_here"
```

3. Click "Save"

## Step 6: Deploy

Click "Deploy!" and wait for your app to build and launch.

Your app will be available at:
`https://share.streamlit.io/YOUR_USERNAME/stock-fundamentals-analyzer/main/app.py`

Or a shorter URL like:
`https://YOUR_USERNAME-stock-fundamentals-analyzer.streamlit.app`

## Updating Your App

To update your deployed app, simply push changes to GitHub:

```bash
git add .
git commit -m "Description of changes"
git push
```

Streamlit Cloud will automatically detect the changes and redeploy your app.

## Troubleshooting

### App won't start

- Check the logs in Streamlit Cloud dashboard
- Ensure all dependencies are listed in `requirements.txt`
- Verify your API key is correctly set in Secrets

### API Key Error

If you see "ANTHROPIC_API_KEY not found":
1. Go to your app settings on Streamlit Cloud
2. Navigate to Secrets
3. Add or update your `ANTHROPIC_API_KEY`
4. Reboot the app

### PDF Upload Issues

- Ensure uploaded PDFs are under 200MB (configured in `.streamlit/config.toml`)
- Check that PyPDF2 is properly installed

### Import Errors

If you see "Module not found" errors:
- Ensure the module is in `requirements.txt`
- Check for typos in import statements
- Reboot the app after adding dependencies

## Local Development

To run locally for testing before deployment:

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
cp .env.example .env
# Edit .env and add your actual API key

# Run the app
streamlit run app.py
```

## Custom Domain (Optional)

To use a custom domain:

1. Upgrade to Streamlit Cloud Pro
2. Follow Streamlit's custom domain setup guide
3. Configure DNS settings with your domain provider

## Environment Variables

The app checks for the API key in this order:
1. Streamlit secrets (for cloud deployment)
2. Environment variables (for local development)

This allows the same code to work both locally and in the cloud.

## Security Notes

- Never commit `.env` or `.streamlit/secrets.toml` to GitHub
- The `.gitignore` file is configured to exclude these files
- Always use environment variables or secrets for sensitive data
- Consider implementing rate limiting for production use

## Monitoring

Streamlit Cloud provides:
- Real-time logs
- Usage analytics
- Error tracking

Access these from your app's dashboard on share.streamlit.io

## Costs

- Streamlit Cloud: Free tier available (limited to 1 app)
- Anthropic API: Pay-per-use (see https://anthropic.com/pricing)
- Estimate: ~$0.01-0.05 per analysis depending on report size

## Next Steps

After successful deployment:

1. Test the app with a sample annual report
2. Share the URL with users
3. Monitor usage and costs
4. Consider adding:
   - User authentication
   - Database for saving analyses
   - Export to PDF functionality
   - Comparison features
