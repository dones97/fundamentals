"""
Web research module to supplement annual report analysis with online data
Uses DuckDuckGo search (no API key needed) and web scraping
"""

import requests
from typing import List, Dict, Optional
import re
from urllib.parse import quote_plus

def search_duckduckgo(query: str, num_results: int = 5) -> List[Dict[str, str]]:
    """
    Search DuckDuckGo for relevant information
    Returns list of search results with title, link, and snippet
    """
    try:
        # DuckDuckGo HTML search
        url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse results (basic extraction)
        results = []

        # Extract result blocks
        result_pattern = r'<a class="result__a" href="([^"]+)"[^>]*>([^<]+)</a>'
        snippet_pattern = r'<a class="result__snippet"[^>]*>([^<]+)</a>'

        links = re.findall(result_pattern, response.text)
        snippets = re.findall(snippet_pattern, response.text)

        for i, (link, title) in enumerate(links[:num_results]):
            snippet = snippets[i] if i < len(snippets) else ""
            results.append({
                'title': title.strip(),
                'link': link,
                'snippet': snippet.strip()
            })

        return results

    except Exception as e:
        print(f"Search error: {e}")
        return []

def get_company_info(company_name: str) -> str:
    """
    Get supplementary information about a company from web search
    """
    research_queries = [
        f"{company_name} company overview business model",
        f"{company_name} competitors market share",
        f"{company_name} recent news developments 2024",
        f"{company_name} industry trends outlook"
    ]

    all_info = []

    for query in research_queries:
        results = search_duckduckgo(query, num_results=3)
        if results:
            info = f"\n### Search: {query}\n"
            for r in results:
                info += f"- **{r['title']}**: {r['snippet']}\n"
            all_info.append(info)

    return "\n".join(all_info) if all_info else "No additional web research available."

def get_industry_research(industry: str, company_name: str) -> str:
    """
    Get industry-specific research
    """
    queries = [
        f"{industry} industry analysis 2024",
        f"{industry} market trends forecast",
        f"{industry} major players competition"
    ]

    research = []

    for query in queries:
        results = search_duckduckgo(query, num_results=3)
        if results:
            for r in results:
                research.append(f"- {r['title']}: {r['snippet']}")

    return "\n".join(research) if research else ""

def get_competitor_info(company_name: str) -> str:
    """
    Research competitors
    """
    query = f"{company_name} main competitors comparison"
    results = search_duckduckgo(query, num_results=5)

    if results:
        info = []
        for r in results:
            info.append(f"- {r['title']}: {r['snippet']}")
        return "\n".join(info)

    return ""

def get_recent_news(company_name: str) -> str:
    """
    Get recent news about the company
    """
    query = f"{company_name} news 2024"
    results = search_duckduckgo(query, num_results=5)

    if results:
        news = []
        for r in results:
            news.append(f"- {r['title']}: {r['snippet']}")
        return "\n".join(news)

    return ""

def get_risk_research(company_name: str, industry: str) -> str:
    """
    Research risks and challenges
    """
    queries = [
        f"{company_name} risks challenges concerns",
        f"{industry} industry risks regulatory"
    ]

    research = []

    for query in queries:
        results = search_duckduckgo(query, num_results=3)
        if results:
            for r in results:
                research.append(f"- {r['title']}: {r['snippet']}")

    return "\n".join(research) if research else ""

def extract_company_name_from_report(report_text: str, llm_provider) -> str:
    """
    Use LLM to extract company name from report
    """
    prompt = """Extract ONLY the company name from this annual report.
    Return just the company name, nothing else.
    Example: "Apple Inc." or "Microsoft Corporation"
    """

    try:
        result = llm_provider.get_completion(prompt, report_text[:5000])
        # Clean up the result
        company_name = result.strip().replace('"', '').replace("'", "")
        return company_name
    except:
        return "Unknown Company"

def gather_web_research(company_name: str, section: str) -> str:
    """
    Gather relevant web research for a specific analysis section
    """
    research = ""

    if section == "quick_stats":
        results = search_duckduckgo(f"{company_name} market cap sector industry", 3)
        if results:
            research = "\n".join([f"- {r['snippet']}" for r in results])

    elif section == "business_overview":
        research = get_company_info(company_name)

    elif section == "ecosystem":
        competitor_info = get_competitor_info(company_name)
        research = f"### Competitor Research:\n{competitor_info}"

    elif section == "industry_deep_dive":
        # First get industry from a quick search
        industry_results = search_duckduckgo(f"{company_name} industry sector", 1)
        industry = "technology"  # default
        if industry_results:
            industry = industry_results[0].get('snippet', 'technology')[:50]

        research = get_industry_research(industry, company_name)

    elif section == "risk_analysis":
        research = get_risk_research(company_name, "")

    elif section == "bull_bear_cases":
        news = get_recent_news(company_name)
        research = f"### Recent News & Developments:\n{news}"

    return research

class WebResearchEnhancer:
    """
    Enhances analysis by combining annual report with web research
    """

    def __init__(self, company_name: str):
        self.company_name = company_name
        self.cache = {}

    def get_research_for_section(self, section: str) -> str:
        """
        Get cached or fresh research for a section
        """
        if section in self.cache:
            return self.cache[section]

        research = gather_web_research(self.company_name, section)
        self.cache[section] = research
        return research

    def enhance_prompt(self, original_prompt: str, section: str) -> str:
        """
        Enhance the original prompt with web research context
        """
        research = self.get_research_for_section(section)

        if research:
            enhanced_prompt = f"""{original_prompt}

## Additional Context from Web Research:
{research}

Please incorporate insights from both the annual report AND the web research above to provide a comprehensive analysis. Cite specific findings from web research where relevant."""
            return enhanced_prompt

        return original_prompt
