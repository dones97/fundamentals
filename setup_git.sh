#!/bin/bash

echo "================================================"
echo "Stock Fundamentals Analyzer - Git Setup"
echo "================================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed"
    echo "Install Git:"
    echo "  macOS: brew install git"
    echo "  Linux: sudo apt-get install git"
    exit 1
fi

echo "Git is installed. Proceeding with setup..."
echo ""

# Initialize git repository
echo "[Step 1/3] Initializing Git repository..."
if ! git init; then
    echo "ERROR: Failed to initialize Git repository"
    exit 1
fi
echo "✓ Git repository initialized"
echo ""

# Add all files
echo "[Step 2/3] Adding files to Git..."
if ! git add .; then
    echo "ERROR: Failed to add files"
    exit 1
fi
echo "✓ Files added to staging"
echo ""

# Create initial commit
echo "[Step 3/3] Creating initial commit..."
if ! git commit -m "Initial commit: Stock Fundamentals Analyzer"; then
    echo "ERROR: Failed to create commit"
    exit 1
fi
echo "✓ Initial commit created"
echo ""

echo "================================================"
echo "Git setup complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub"
echo "   Go to: https://github.com/new"
echo ""
echo "2. Run these commands (replace YOUR_USERNAME and YOUR_REPO):"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Streamlit Cloud"
echo "   Go to: https://share.streamlit.io/"
echo ""
echo "See DEPLOYMENT.md for detailed instructions"
echo ""
