# FREE Setup Guide - No Cost AI Analysis

This guide shows you how to use the Stock Fundamentals Analyzer **completely FREE** using open-source AI models.

## 🎉 Two FREE Options

### Option 1: Groq (Recommended - Easiest)
- ✅ **100% Free API access**
- ✅ **Fast inference** (powered by specialized hardware)
- ✅ **No credit card required**
- ✅ **Llama 3.1 70B model** (very capable)
- ✅ **Easy setup** (just need API key)

### Option 2: Ollama (Best for Privacy)
- ✅ **100% Free** (runs on your computer)
- ✅ **Unlimited usage** (no rate limits)
- ✅ **Complete privacy** (data never leaves your machine)
- ✅ **Multiple models** available
- ⚠️ **Requires**: 8GB+ RAM, decent CPU/GPU

---

## 🚀 Quick Start with Groq (5 Minutes)

### Step 1: Get Free Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Click "Sign Up" (free account, no credit card needed)
3. Verify your email
4. Once logged in, click "API Keys" in the left sidebar
5. Click "Create API Key"
6. Copy the API key (starts with `gsk_`)

### Step 2: Install Dependencies

```bash
pip install streamlit groq PyPDF2 plotly pandas requests python-dotenv
```

### Step 3: Configure API Key

**Option A: Using .env file (recommended)**
```bash
cp .env.example .env
```

Edit `.env` and add your key:
```
GROQ_API_KEY=gsk_your_actual_key_here
```

**Option B: Enter in app**
- You can also enter the API key directly in the Streamlit app interface

### Step 4: Run the App

```bash
streamlit run app.py
```

### Step 5: Connect to Groq

1. In the sidebar, select "Groq (FREE - Llama 3.1)" from the dropdown
2. If you used .env file, it will auto-detect your key
3. Click "🔌 Connect Provider"
4. You should see "🟢 Active: Groq (Llama 3.1)"

### Step 6: Analyze!

1. Upload an annual report PDF
2. Click "🔍 Analyze Report"
3. Navigate through the analysis sections

**That's it! You're analyzing stocks for FREE!**

---

## 🏠 Alternative: Ollama (Local, 100% Privacy)

### Why Choose Ollama?

- Runs entirely on your computer
- No API calls, no usage limits
- Your data never leaves your machine
- Perfect for sensitive financial documents

### Requirements

- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 5-10GB for model
- **CPU**: Modern processor (M1/M2 Mac or recent Intel/AMD)
- **GPU**: Optional but speeds things up significantly

### Step 1: Install Ollama

**Mac:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Or download from: [https://ollama.com/download](https://ollama.com/download)

**Windows:**
Download the installer from: [https://ollama.com/download](https://ollama.com/download)

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2: Download a Model

```bash
# Recommended: Llama 3.1 8B (smaller, faster)
ollama pull llama3.1

# Alternative: Llama 3.1 70B (larger, better quality, needs more RAM)
ollama pull llama3.1:70b

# Other good options:
ollama pull mistral       # Fast and good
ollama pull mixtral       # Very capable
```

### Step 3: Start Ollama Server

```bash
ollama serve
```

Keep this terminal window open. Ollama will run in the background.

### Step 4: Install App Dependencies

```bash
pip install streamlit PyPDF2 plotly pandas requests python-dotenv
```

Note: You don't need to install any LLM provider libraries for Ollama!

### Step 5: Run the App

```bash
streamlit run app.py
```

### Step 6: Connect to Ollama

1. In the sidebar, select "Ollama (FREE - Local)"
2. Click "🔌 Connect Provider"
3. If Ollama is running, you'll see "🟢 Active: Ollama (llama3.1)"

### Step 7: Analyze Locally!

1. Upload an annual report
2. Click "🔍 Analyze Report"
3. Analysis happens on your computer - no internet needed!

---

## 📊 Comparison: Groq vs Ollama

| Feature | Groq | Ollama |
|---------|------|--------|
| **Cost** | FREE | FREE |
| **Setup** | Easy (5 min) | Medium (15 min) |
| **Speed** | Very Fast | Fast (depends on hardware) |
| **Privacy** | Data sent to API | 100% local |
| **Requirements** | Internet only | 8GB+ RAM, storage |
| **Rate Limits** | Yes (generous free tier) | None |
| **Quality** | Excellent | Excellent |
| **Best For** | Quick setup, fast results | Privacy, unlimited use |

---

## 💰 Cost Comparison

### FREE Options
- **Groq**: $0 (free tier with rate limits)
- **Ollama**: $0 (unlimited, but uses your electricity/hardware)

### Paid Options (for comparison)
- **Anthropic Claude**: ~$0.10-0.45 per analysis
- **OpenAI GPT-4**: ~$0.15-0.60 per analysis

**For 50 companies analyzed:**
- Groq: **$0**
- Ollama: **$0**
- Anthropic: **$5-22.50**
- OpenAI: **$7.50-30**

---

## 🎯 Which Should You Choose?

### Choose Groq if:
- ✅ You want the easiest setup
- ✅ You're okay with sending data to an API
- ✅ You want the fastest inference
- ✅ You don't want to install anything locally

### Choose Ollama if:
- ✅ You want 100% privacy
- ✅ You have a decent computer (8GB+ RAM)
- ✅ You want unlimited usage
- ✅ You don't want any internet dependency

### Choose Both!
You can switch between providers in the app! Use:
- **Groq** when you need speed
- **Ollama** when analyzing sensitive documents

---

## 🔧 Troubleshooting

### Groq Issues

**"Invalid API key"**
- Check you copied the full key (starts with `gsk_`)
- Make sure there are no extra spaces
- Verify key is active in Groq console

**"Rate limit exceeded"**
- Wait a few minutes (free tier has limits)
- Consider using Ollama for unlimited usage

### Ollama Issues

**"Ollama not running"**
- Run `ollama serve` in a terminal
- Check if port 11434 is available
- Try restarting Ollama

**"Model not found"**
- Run `ollama pull llama3.1` to download the model
- Check available models: `ollama list`

**"Too slow"**
- Try a smaller model: `ollama pull llama3.1:8b`
- Close other applications to free RAM
- Consider using Groq for faster inference

---

## 📖 Step-by-Step: Complete FREE Workflow

### 1. Get Annual Report
```bash
# Visit SEC EDGAR
# Search for a company (e.g., "Apple Inc")
# Download the latest 10-K PDF
```

### 2. Setup Groq (One-time)
```bash
# Sign up: https://console.groq.com
# Get API key
# Add to .env file
```

### 3. Install & Run
```bash
pip install streamlit groq PyPDF2 plotly pandas requests
streamlit run app.py
```

### 4. Analyze
```
1. Select "Groq (FREE - Llama 3.1)"
2. Connect provider
3. Upload 10-K PDF
4. Analyze report
5. Navigate through 9 analysis sections
```

### 5. Export/Save (Future feature)
```
- Screenshot results
- Copy analysis text
- Make investment decisions!
```

---

## 🎓 Learning Resources

### Understanding LLMs
- [Groq Documentation](https://console.groq.com/docs)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Llama 3.1 Model Card](https://ai.meta.com/llama/)

### Financial Analysis
- [How to Read a 10-K](https://www.sec.gov/oiea/investor-alerts-and-bulletins/how-read-10-k-10-q)
- [Hamilton Helmer's 7 Powers](https://7powers.com/)
- [Warren Buffett on Reading Annual Reports](https://www.berkshirehathaway.com/letters/letters.html)

---

## ✨ Advanced: Optimizing for FREE Usage

### Groq Tips
1. **Batch your analyses**: Analyze multiple companies in one session
2. **Cache results**: The app automatically caches each section
3. **Use wisely**: Only re-analyze when reports update

### Ollama Tips
1. **Choose the right model**:
   - `llama3.1:8b` - Fast, good for quick analysis
   - `llama3.1:70b` - Best quality, needs 32GB+ RAM
   - `mixtral` - Good balance

2. **Optimize performance**:
   - Close browser tabs to free RAM
   - Use GPU if available (automatic)
   - Run overnight for large batches

3. **Model management**:
```bash
ollama list           # See installed models
ollama rm model_name  # Remove unused models
ollama pull model     # Download new models
```

---

## 🚀 Next Steps

After you have the FREE version working:

1. **Test with real reports**: Download 3-5 annual reports and analyze them
2. **Compare results**: Try both Groq and Ollama, see which you prefer
3. **Build a watchlist**: Track companies you're interested in
4. **Share**: Deploy to Streamlit Cloud (FREE) so others can use it
5. **Contribute**: Found the analysis helpful? Star the repo!

---

## ❓ FAQ

**Q: Is Groq really free?**
A: Yes! Groq offers a generous free tier with no credit card required.

**Q: How much can I analyze for free?**
A: Groq: ~100 analyses/day (varies). Ollama: Unlimited.

**Q: Which gives better results?**
A: Both use Llama 3.1 70B. Quality is similar. Groq is faster.

**Q: Can I use this commercially?**
A: Check Groq's ToS for API usage. Ollama is 100% yours to use.

**Q: Do I need coding knowledge?**
A: No! Just follow this guide step-by-step.

**Q: Can I analyze any stock?**
A: Yes! Any company with a public annual report (10-K, 20-F, etc.)

---

## 🎉 Success!

You now have a **professional-grade stock analysis tool** running for **$0**!

Happy investing! 📈

---

**Need Help?**
- Check [QUICKSTART.md](QUICKSTART.md) for general setup
- Review [troubleshooting section](#-troubleshooting) above
- Open an issue on GitHub
