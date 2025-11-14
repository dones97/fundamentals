"""
LLM Provider abstraction to support multiple AI providers
Supports: Anthropic (paid), Groq (free), OpenAI (paid), and Ollama (local/free)
"""

import os
import streamlit as st
from typing import Optional

class LLMProvider:
    """Base class for LLM providers"""

    def __init__(self):
        self.provider_name = "Base"

    def get_completion(self, prompt: str, context: str) -> str:
        raise NotImplementedError

class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider (paid)"""

    def __init__(self, api_key: str):
        super().__init__()
        self.provider_name = "Anthropic Claude"
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
            self.available = True
        except ImportError:
            self.available = False
            st.warning("Anthropic library not installed. Run: pip install anthropic")

    def get_completion(self, prompt: str, context: str) -> str:
        if not self.available:
            return "Anthropic provider not available. Please install: pip install anthropic"

        message = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": f"{prompt}\n\nAnnual Report Content:\n{context[:50000]}"
            }]
        )
        return message.content[0].text

class GroqProvider(LLMProvider):
    """Groq provider with free tier (Llama 3.1)"""

    def __init__(self, api_key: str):
        super().__init__()
        self.provider_name = "Groq (Llama 3.1)"
        try:
            from groq import Groq
            self.client = Groq(api_key=api_key)
            self.available = True
        except ImportError:
            self.available = False
            st.warning("Groq library not installed. Run: pip install groq")

    def get_completion(self, prompt: str, context: str) -> str:
        if not self.available:
            return "Groq provider not available. Please install: pip install groq"

        # Groq has token limits, so we need to be more conservative
        max_context = 30000  # Leave room for prompt + response
        truncated_context = context[:max_context]

        completion = self.client.chat.completions.create(
            model="llama-3.1-70b-versatile",  # Free tier model
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial analyst expert who analyzes company annual reports and provides detailed insights."
                },
                {
                    "role": "user",
                    "content": f"{prompt}\n\nAnnual Report Content:\n{truncated_context}"
                }
            ],
            temperature=0.3,
            max_tokens=2048
        )
        return completion.choices[0].message.content

class OllamaProvider(LLMProvider):
    """Ollama local provider (100% free, runs on your computer)"""

    def __init__(self, model: str = "llama3.1"):
        super().__init__()
        self.provider_name = f"Ollama ({model})"
        self.model = model
        try:
            import requests
            self.requests = requests
            # Test if Ollama is running
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            self.available = response.status_code == 200
            if not self.available:
                st.warning("Ollama is installed but not running. Start it with: ollama serve")
        except ImportError:
            self.available = False
            st.warning("Requests library needed. Run: pip install requests")
        except Exception as e:
            self.available = False
            st.info("Ollama not running locally. Install from: https://ollama.com")

    def get_completion(self, prompt: str, context: str) -> str:
        if not self.available:
            return "Ollama not available. Install from https://ollama.com and run: ollama serve"

        # Ollama can handle larger contexts with local models
        max_context = 20000
        truncated_context = context[:max_context]

        try:
            response = self.requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": self.model,
                    "prompt": f"{prompt}\n\nAnnual Report Content:\n{truncated_context}",
                    "stream": False,
                    "options": {
                        "temperature": 0.3,
                        "num_predict": 2048
                    }
                },
                timeout=120
            )
            response.raise_for_status()
            return response.json()['response']
        except Exception as e:
            return f"Error calling Ollama: {str(e)}"

class OpenAIProvider(LLMProvider):
    """OpenAI GPT provider (paid, but some free credits for new users)"""

    def __init__(self, api_key: str):
        super().__init__()
        self.provider_name = "OpenAI GPT-4"
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=api_key)
            self.available = True
        except ImportError:
            self.available = False
            st.warning("OpenAI library not installed. Run: pip install openai")

    def get_completion(self, prompt: str, context: str) -> str:
        if not self.available:
            return "OpenAI provider not available. Please install: pip install openai"

        max_context = 30000
        truncated_context = context[:max_context]

        completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial analyst expert who analyzes company annual reports and provides detailed insights."
                },
                {
                    "role": "user",
                    "content": f"{prompt}\n\nAnnual Report Content:\n{truncated_context}"
                }
            ],
            temperature=0.3,
            max_tokens=2048
        )
        return completion.choices[0].message.content

def get_available_providers() -> dict:
    """Get dictionary of available providers with their config"""
    return {
        "Groq (FREE - Llama 3.1)": {
            "class": GroqProvider,
            "requires_key": True,
            "key_name": "GROQ_API_KEY",
            "signup_url": "https://console.groq.com",
            "description": "Free tier available! Fast inference with Llama 3.1 70B",
            "cost": "FREE (limited rate)"
        },
        "Ollama (FREE - Local)": {
            "class": OllamaProvider,
            "requires_key": False,
            "key_name": None,
            "signup_url": "https://ollama.com",
            "description": "100% free, runs locally on your computer",
            "cost": "FREE (unlimited)"
        },
        "Anthropic Claude": {
            "class": AnthropicProvider,
            "requires_key": True,
            "key_name": "ANTHROPIC_API_KEY",
            "signup_url": "https://console.anthropic.com",
            "description": "High quality analysis, best results",
            "cost": "$0.10-0.45 per analysis"
        },
        "OpenAI GPT-4": {
            "class": OpenAIProvider,
            "requires_key": True,
            "key_name": "OPENAI_API_KEY",
            "signup_url": "https://platform.openai.com",
            "description": "Good quality, some free credits for new users",
            "cost": "$0.15-0.60 per analysis"
        }
    }

def create_provider(provider_name: str, api_key: Optional[str] = None) -> Optional[LLMProvider]:
    """Factory function to create the appropriate provider"""
    providers = get_available_providers()

    if provider_name not in providers:
        return None

    provider_config = providers[provider_name]
    provider_class = provider_config["class"]

    try:
        if provider_config["requires_key"]:
            if not api_key:
                return None
            return provider_class(api_key)
        else:
            return provider_class()
    except Exception as e:
        st.error(f"Error initializing {provider_name}: {str(e)}")
        return None

def get_api_key_from_env(key_name: str) -> Optional[str]:
    """Get API key from environment or Streamlit secrets"""
    # Try Streamlit secrets first
    if hasattr(st, 'secrets') and key_name in st.secrets:
        return st.secrets[key_name]
    # Fall back to environment variable
    return os.environ.get(key_name)
