import streamlit as st
import os
from pathlib import Path
import PyPDF2
import io
from visualizations import create_sample_sankey, display_sankey_with_data
from llm_providers import get_available_providers, create_provider, get_api_key_from_env

# Page configuration
st.set_page_config(
    page_title="Fundamentals Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'report_text' not in st.session_state:
    st.session_state.report_text = None
if 'analyses' not in st.session_state:
    st.session_state.analyses = {}
if 'selected_provider' not in st.session_state:
    st.session_state.selected_provider = "Groq (FREE - Llama 3.3)"
if 'llm_provider' not in st.session_state:
    st.session_state.llm_provider = None

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title("📊 Stock Fundamentals Analyzer")
    st.markdown("### Upload an annual report to get comprehensive fundamental analysis")

    # Sidebar for navigation
    with st.sidebar:
        st.header("🤖 AI Provider")

        # LLM Provider Selection
        providers = get_available_providers()
        provider_names = list(providers.keys())

        selected_provider = st.selectbox(
            "Choose AI Provider:",
            provider_names,
            index=provider_names.index(st.session_state.selected_provider) if st.session_state.selected_provider in provider_names else 0,
            help="Select which AI service to use for analysis"
        )

        # Display provider info
        provider_info = providers[selected_provider]
        st.info(f"💡 {provider_info['description']}\n\n**Cost:** {provider_info['cost']}")

        # API Key input if required
        api_key = None
        if provider_info["requires_key"]:
            key_name = provider_info["key_name"]
            # Check if key exists in environment
            env_key = get_api_key_from_env(key_name)

            if env_key:
                st.success(f"✓ {key_name} found in environment")
                api_key = env_key
            else:
                st.warning(f"⚠️ {key_name} not found")
                api_key = st.text_input(
                    f"Enter {key_name}:",
                    type="password",
                    help=f"Get your free API key at: {provider_info['signup_url']}"
                )
                if not api_key:
                    st.markdown(f"[Get free API key →]({provider_info['signup_url']})")

        # Initialize provider
        if st.button("🔌 Connect Provider"):
            provider = create_provider(selected_provider, api_key)
            if provider and provider.available:
                st.session_state.llm_provider = provider
                st.session_state.selected_provider = selected_provider
                st.success(f"✓ Connected to {provider.provider_name}")
            else:
                st.error("Failed to connect to provider. Check your API key or installation.")

        # Show current provider status
        if st.session_state.llm_provider:
            st.success(f"🟢 Active: {st.session_state.llm_provider.provider_name}")
        else:
            st.warning("🔴 No provider connected")

        st.divider()

        st.header("📄 Upload Report")

        # File upload
        uploaded_file = st.file_uploader(
            "Upload Annual Report (PDF)",
            type=['pdf'],
            help="Upload the company's latest annual report (10-K, annual report, etc.)"
        )

        if uploaded_file is not None:
            if st.button("🔍 Analyze Report", type="primary"):
                if not st.session_state.llm_provider:
                    st.error("⚠️ Please connect to an AI provider first!")
                else:
                    with st.spinner("Extracting text from PDF..."):
                        st.session_state.report_text = extract_text_from_pdf(uploaded_file)
                        st.session_state.analysis_complete = True
                        st.success("✓ Report uploaded successfully!")

        st.divider()

        # Navigation menu
        if st.session_state.analysis_complete:
            st.subheader("Analysis Sections")
            section = st.radio(
                "Choose section:",
                [
                    "Overview",
                    "1. Quick Stats",
                    "2. Business Overview",
                    "3. Business Model Map",
                    "4. The Machine",
                    "5. Ecosystem",
                    "6. Industry Deep Dive",
                    "7. Risk Analysis",
                    "8. Hamilton Helmer 7 Powers",
                    "9. Bull & Bear Cases"
                ],
                label_visibility="collapsed"
            )
        else:
            st.info("Upload an annual report to begin analysis")
            section = "Overview"

    # Main content area
    if not st.session_state.analysis_complete:
        display_welcome()
    else:
        display_section(section)

def display_welcome():
    """Display welcome screen with instructions"""
    st.markdown("""
    ## Welcome to the Stock Fundamentals Analyzer

    This tool provides comprehensive fundamental analysis of publicly traded companies based on their annual reports.

    ### What You'll Get:

    1. **Quick Stats** - Sector, industry, and market cap overview
    2. **Business Overview** - How the company makes money, customers, suppliers, rivals, and history
    3. **Business Model Map** - Visual representation of revenue flows and cost structure
    4. **The Machine** - Detailed breakdown of inputs, processes, and outputs
    5. **Ecosystem** - Analysis of customers, suppliers, competition, and substitutes
    6. **Industry Deep Dive** - Market trends and industry dynamics
    7. **Risk Analysis** - Key business risks and challenges
    8. **7 Powers Assessment** - Strategic moat analysis using Hamilton Helmer's framework
    9. **Bull & Bear Cases** - What needs to go right vs. what could go wrong

    ### Getting Started:

    1. Upload the company's latest annual report (PDF format) using the sidebar
    2. Click "Analyze Report" to process the document
    3. Navigate through different analysis sections

    ---

    *Note: Analysis uses Claude AI to extract and analyze information from the annual report.*
    """)

    # Sample image placeholder
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://via.placeholder.com/600x300?text=Upload+Annual+Report+to+Begin",
                 use_container_width=True)

def display_section(section):
    """Display the selected analysis section"""

    if section == "Overview":
        st.header("Analysis Overview")
        st.markdown("""
        Your annual report has been uploaded successfully. Use the sidebar to navigate through
        different sections of the fundamental analysis.

        Each section will be generated on-demand using AI analysis of the uploaded report.
        """)

    elif section == "1. Quick Stats":
        display_quick_stats()

    elif section == "2. Business Overview":
        display_business_overview()

    elif section == "3. Business Model Map":
        display_business_model_map()

    elif section == "4. The Machine":
        display_the_machine()

    elif section == "5. Ecosystem":
        display_ecosystem()

    elif section == "6. Industry Deep Dive":
        display_industry_deep_dive()

    elif section == "7. Risk Analysis":
        display_risk_analysis()

    elif section == "8. Hamilton Helmer 7 Powers":
        display_seven_powers()

    elif section == "9. Bull & Bear Cases":
        display_bull_bear_cases()

def get_analysis(section_key, prompt):
    """Get analysis using the configured LLM provider for a specific section"""
    # Return cached analysis if available
    if section_key in st.session_state.analyses:
        return st.session_state.analyses[section_key]

    # Check if provider is configured
    if not st.session_state.llm_provider:
        st.error("⚠️ No AI provider connected. Please select and connect a provider in the sidebar.")
        return "AI provider not configured. Please connect to an AI provider in the sidebar to continue."

    # Get analysis from provider
    with st.spinner(f"Analyzing {section_key} using {st.session_state.llm_provider.provider_name}..."):
        try:
            analysis = st.session_state.llm_provider.get_completion(
                prompt=prompt,
                context=st.session_state.report_text
            )
            # Cache the result
            st.session_state.analyses[section_key] = analysis
            return analysis
        except Exception as e:
            error_msg = f"Error during analysis: {str(e)}"
            st.error(error_msg)
            return error_msg

def display_quick_stats():
    st.header("1. Quick Stats")

    prompt = """Analyze this annual report and provide a concise one-liner summary with:
    - Sector and Industry classification
    - Market capitalization (if mentioned)
    - Stock ticker symbol

    Format: "[Company Name] | [Sector] - [Industry] | Market Cap: $X.XB"

    Keep it brief and factual."""

    analysis = get_analysis("quick_stats", prompt)

    st.markdown("### Company Snapshot")
    st.info(analysis)

def display_business_overview():
    st.header("2. Business Overview")

    prompt = """Provide a quick but comprehensive overview of the business covering:

    1. **How It Makes Money**: Primary revenue streams and business model
    2. **Customers**: Who are the main customer segments?
    3. **Suppliers**: Key suppliers and dependencies
    4. **Rivals**: Main competitors in the market
    5. **Ecosystem**: Key partners, platforms, or ecosystem players
    6. **Company History**: Brief history and major milestones

    Keep each subsection concise (2-3 sentences). Use bullet points for clarity."""

    analysis = get_analysis("business_overview", prompt)
    st.markdown(analysis)

def display_business_model_map():
    st.header("3. Business Model Map")

    st.markdown("""
    This section visualizes how money flows through the business - from revenue sources
    through to major cost categories, similar to a Sankey diagram.
    """)

    prompt = """Analyze the annual report and extract:

    1. **Revenue Breakdown**: List all major revenue streams with approximate percentages or dollar amounts
    2. **Cost Structure**: Break down major cost categories (COGS, SG&A, R&D, etc.) with amounts
    3. **Gross Profit and Operating Profit**: Extract these key metrics

    Format your response as a structured breakdown that can be used to create a flow diagram.
    Include actual numbers from the report whenever possible."""

    analysis = get_analysis("business_model_map", prompt)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Financial Breakdown")
        st.markdown(analysis)

    with col2:
        st.subheader("Visual Representation")
        st.info("📊 Showing business model flow diagram")
        # Display sample Sankey diagram
        fig = create_sample_sankey()
        st.plotly_chart(fig, use_container_width=True)
        st.caption("💡 Diagram shows revenue sources flowing into costs and profits")

def display_the_machine():
    st.header("4. The Machine")

    prompt = """Analyze the business as a machine with three components:

    1. **INPUTS**: What goes into the business?
       - Raw materials, technology, talent, capital, data, etc.
       - Key dependencies and resources

    2. **PROCESS**: How does the business transform inputs?
       - Core operations and capabilities
       - Key processes and technologies
       - Value creation mechanisms

    3. **OUTPUTS**: What comes out?
       - Products and services
       - Value delivered to customers
       - Financial outcomes

    Provide a detailed but clear explanation of each component."""

    analysis = get_analysis("the_machine", prompt)
    st.markdown(analysis)

def display_ecosystem():
    st.header("5. Ecosystem Analysis")

    prompt = """Provide a detailed analysis of the company's ecosystem:

    1. **CUSTOMERS**:
       - Customer segments and characteristics
       - Customer concentration and dependencies
       - Customer acquisition and retention

    2. **SUPPLIERS**:
       - Key suppliers and supply chain
       - Supplier power and dependencies
       - Supply chain risks

    3. **COMPETITION**:
       - Direct competitors
       - Competitive positioning
       - Market share dynamics

    4. **SUBSTITUTES**:
       - Alternative solutions or products
       - Threat of substitution

    5. **OTHER CHARACTERISTICS**:
       - Network effects
       - Regulatory environment
       - Industry dynamics

    Be specific and use information from the annual report."""

    analysis = get_analysis("ecosystem", prompt)
    st.markdown(analysis)

def display_industry_deep_dive():
    st.header("6. Industry Deep Dive")

    prompt = """Provide a comprehensive analysis of the industry:

    1. **Industry Overview**: Market size, growth rates, maturity
    2. **Key Trends**: Major trends shaping the industry
    3. **Market Dynamics**: Supply/demand dynamics, pricing power
    4. **Technology Impact**: How technology is disrupting or enabling
    5. **Regulatory Environment**: Key regulations affecting the industry
    6. **Future Outlook**: Where is the industry headed?

    Draw insights from the annual report's industry discussion sections."""

    analysis = get_analysis("industry_deep_dive", prompt)
    st.markdown(analysis)

def display_risk_analysis():
    st.header("7. Risk Analysis")

    prompt = """Extract and analyze all major risks facing the business:

    1. **Strategic Risks**: Competition, market position, strategic execution
    2. **Operational Risks**: Supply chain, operations, execution risks
    3. **Financial Risks**: Debt, liquidity, currency, interest rate risks
    4. **Regulatory & Legal Risks**: Compliance, litigation, regulatory changes
    5. **Technology Risks**: Cybersecurity, technological disruption
    6. **Market Risks**: Economic conditions, market volatility
    7. **ESG Risks**: Environmental, social, governance risks

    For each risk category, highlight the most material risks mentioned in the report.
    Rate each category as High/Medium/Low risk based on disclosure emphasis."""

    analysis = get_analysis("risk_analysis", prompt)
    st.markdown(analysis)

def display_seven_powers():
    st.header("8. Hamilton Helmer's 7 Powers Assessment")

    st.markdown("""
    Evaluating the company's strategic moats across Hamilton Helmer's 7 Powers framework.
    Each power is assessed as **Strong**, **Moderate**, or **Weak** relative to competition.
    """)

    prompt = """Assess the company across Hamilton Helmer's 7 Powers framework:

    1. **SCALE ECONOMIES**: Does increasing scale reduce per-unit costs?
       - Assessment: Strong/Moderate/Weak
       - Evidence from the report
       - Comparison to competitors

    2. **NETWORK EFFECTS**: Does the product become more valuable as more people use it?
       - Assessment: Strong/Moderate/Weak
       - Evidence and examples

    3. **COUNTER-POSITIONING**: Does the business model create disadvantages for incumbents?
       - Assessment: Strong/Moderate/Weak
       - How it differs from traditional competitors

    4. **SWITCHING COSTS**: How difficult is it for customers to switch to competitors?
       - Assessment: Strong/Moderate/Weak
       - Types of switching costs present

    5. **BRANDING**: Does the brand command premium pricing or preference?
       - Assessment: Strong/Moderate/Weak
       - Brand strength indicators

    6. **CORNERED RESOURCE**: Does the company have unique access to key resources?
       - Assessment: Strong/Moderate/Weak
       - What resources and how defensible

    7. **PROCESS POWER**: Are there proprietary processes that competitors can't replicate?
       - Assessment: Strong/Moderate/Weak
       - Examples of unique processes

    For each power, provide assessment, reasoning, and competitive comparison."""

    analysis = get_analysis("seven_powers", prompt)
    st.markdown(analysis)

    # Summary visualization
    st.divider()
    st.subheader("Powers Summary")
    st.info("💡 Visual summary chart will be displayed here showing the strength of each power")

def display_bull_bear_cases():
    st.header("9. Bull & Bear Cases")

    prompt = """Develop comprehensive bull and bear investment cases:

    **🐂 BULL CASE - What Needs to Go RIGHT:**

    1. Key assumptions that must hold true
    2. Market opportunities that materialize
    3. Execution on strategic initiatives
    4. Favorable industry trends
    5. Competitive advantages that strengthen
    6. Financial targets achieved
    7. Potential upside scenarios

    **🐻 BEAR CASE - What Could Go WRONG:**

    1. Key risks that materialize
    2. Market opportunities that don't materialize
    3. Execution failures or challenges
    4. Adverse industry trends
    5. Competitive threats intensify
    6. Financial challenges or misses
    7. Potential downside scenarios

    Be specific and realistic. Base scenarios on information and risks disclosed in the annual report.
    For each case, provide 5-7 concrete points."""

    analysis = get_analysis("bull_bear_cases", prompt)

    col1, col2 = st.columns(2)

    with col1:
        st.success("### 🐂 Bull Case")

    with col2:
        st.error("### 🐻 Bear Case")

    st.markdown(analysis)

if __name__ == "__main__":
    main()
