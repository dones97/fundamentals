# Quick Start Guide

Get your Stock Fundamentals Analyzer running in 5 minutes!

## Local Setup (For Testing)

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

Get your API key from: https://console.anthropic.com/

### 3. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 4. Test It Out

1. Download a sample annual report PDF (e.g., from a company's investor relations page)
2. Upload it using the sidebar
3. Click "Analyze Report"
4. Navigate through the analysis sections

## Deploy to GitHub + Streamlit Cloud

### Quick Deploy (5 steps)

1. **Initialize Git**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create GitHub Repo**
   - Go to https://github.com/new
   - Create a new repository
   - Don't initialize with README

3. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

4. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select your GitHub repo
   - Set main file: `app.py`

5. **Add API Key Secret**
   - In Streamlit Cloud, go to app settings
   - Add to Secrets:
     ```toml
     ANTHROPIC_API_KEY = "your_api_key_here"
     ```
   - Click Deploy!

Done! Your app is live.

## Where to Find Annual Reports

### US Public Companies
- **SEC EDGAR**: https://www.sec.gov/edgar/searchedgar/companysearch
  - Search for company
  - Look for "10-K" filings (annual reports)

### Popular Examples to Try
- Apple: Search "AAPL 10-K" on SEC EDGAR
- Microsoft: Search "MSFT 10-K"
- Tesla: Search "TSLA 10-K"
- Amazon: Search "AMZN 10-K"

### International Companies
- Check the company's investor relations website
- Look for "Annual Report" or "Form 20-F" (for foreign companies)

## Using the App

### Analysis Sections

1. **Quick Stats** - Company snapshot (sector, industry, market cap)
2. **Business Overview** - How the company operates
3. **Business Model Map** - Visual revenue/cost flow diagram
4. **The Machine** - Inputs → Process → Outputs
5. **Ecosystem** - Customers, suppliers, competitors
6. **Industry Deep Dive** - Market trends and dynamics
7. **Risk Analysis** - Key business risks
8. **7 Powers** - Strategic moat analysis
9. **Bull & Bear Cases** - Investment scenarios

### Tips for Best Results

- **Use complete annual reports**: 10-K filings work best
- **Latest reports**: Use the most recent annual report
- **Wait for analysis**: Each section takes 30-60 seconds to generate
- **Cached results**: Once generated, sections load instantly
- **PDF quality**: Clear, text-based PDFs work better than scanned images

## Troubleshooting

### "ANTHROPIC_API_KEY not found"
- **Local**: Check your `.env` file exists and has the correct key
- **Cloud**: Add the key to Streamlit Cloud secrets

### "Could not extract text from PDF"
- Try a different PDF
- Ensure PDF is text-based, not a scanned image
- Try downloading the PDF directly from SEC EDGAR

### App is slow
- First analysis takes longer (building cache)
- Subsequent sections load faster
- Large PDFs (>100 pages) take more time

### Import errors
```bash
pip install -r requirements.txt --upgrade
```

## Cost Estimates

Using Claude Sonnet 4.5:

- **Per analysis section**: $0.01 - $0.05
- **Full 9-section analysis**: ~$0.10 - $0.45
- **Varies by**: Report length, complexity

Monthly estimates:
- 10 companies/month: ~$4 - $45
- 50 companies/month: ~$20 - $225

## Next Steps

### Expand Functionality
- Add valuation module (DCF, multiples)
- Compare multiple companies
- Track historical analyses
- Export to PDF/Excel

### Improve Accuracy
- Fine-tune prompts for specific industries
- Add financial ratios calculator
- Integrate real-time stock data

### Enhance UX
- Add company search by ticker
- Auto-download 10-K from SEC
- Save/load analysis sessions
- User authentication

## Support

- **Issues**: Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed troubleshooting
- **Updates**: Pull latest changes from GitHub
- **Questions**: Open an issue on GitHub

## Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [SEC EDGAR](https://www.sec.gov/edgar)
- [Hamilton Helmer's 7 Powers](https://7powers.com/)

Happy analyzing!
