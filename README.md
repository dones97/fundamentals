# Stock Fundamentals Analyzer

A Streamlit application that provides comprehensive fundamental analysis of publicly traded companies based on their annual reports using AI.

## 🎉 100% FREE Options Available!

This app supports **multiple AI providers**, including **FREE options**:

- ✅ **Groq** (FREE - Llama 3.1) - Fast, no credit card needed
- ✅ **Ollama** (FREE - Local) - 100% private, unlimited usage
- 💰 Anthropic Claude (Paid - Best quality)
- 💰 OpenAI GPT-4 (Paid - Some free credits for new users)

**👉 See [FREE_SETUP_GUIDE.md](FREE_SETUP_GUIDE.md) for complete free setup instructions!**

## Features

1. **Quick Stats** - Sector, industry, and market cap overview
2. **Business Overview** - How the company makes money, customers, suppliers, rivals, and history
3. **Business Model Map** - Visual representation of revenue flows and cost structure
4. **The Machine** - Detailed breakdown of inputs, processes, and outputs
5. **Ecosystem** - Analysis of customers, suppliers, competition, and substitutes
6. **Industry Deep Dive** - Market trends and industry dynamics
7. **Risk Analysis** - Key business risks and challenges
8. **7 Powers Assessment** - Strategic moat analysis using Hamilton Helmer's framework
9. **Bull & Bear Cases** - Investment scenarios

## Quick Start

### FREE Setup (Groq - Recommended)

1. **Get free API key**: [https://console.groq.com](https://console.groq.com) (no credit card!)

2. **Install**:
```bash
pip install streamlit groq PyPDF2 plotly pandas requests
```

3. **Configure**:
```bash
cp .env.example .env
# Edit .env and add: GROQ_API_KEY=your_key_here
```

4. **Run**:
```bash
streamlit run app.py
```

5. **Use**: Select "Groq (FREE)" in the sidebar, connect, and analyze!

**👉 For detailed instructions, see [FREE_SETUP_GUIDE.md](FREE_SETUP_GUIDE.md)**

### Alternative: Local FREE Setup (Ollama)

1. Install Ollama: [https://ollama.com](https://ollama.com)
2. Download model: `ollama pull llama3.1`
3. Start server: `ollama serve`
4. Run app: `streamlit run app.py`
5. Select "Ollama (FREE - Local)" in the sidebar

### Paid Options

For Anthropic Claude or OpenAI GPT-4, see [QUICKSTART.md](QUICKSTART.md)

## Usage

1. Upload a company's annual report (PDF format) using the sidebar
2. Click "Analyze Report" to process the document
3. Navigate through different analysis sections using the sidebar menu
4. Each section will be generated on-demand using AI analysis

## Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `ANTHROPIC_API_KEY` in the Secrets section:
```toml
ANTHROPIC_API_KEY = "your_api_key_here"
```
5. Deploy!

### Other Platforms

This app can also be deployed to:
- Heroku
- AWS
- Google Cloud Platform
- Azure

Make sure to set the `ANTHROPIC_API_KEY` environment variable in your deployment platform.

## Project Structure

```
Fundamentals/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Future Enhancements

- Add valuation module
- Interactive Sankey diagram for business model visualization
- Export analysis to PDF
- Compare multiple companies
- Historical analysis tracking
- Custom metrics and ratios calculator

## License

MIT License
