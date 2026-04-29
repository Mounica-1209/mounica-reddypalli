"""
LLM Configuration for AutoMed Healthcare Chatbot

This module configures the language model settings for the AI agents.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_llm_config():
    """
    Get the LLM configuration for AutoGen agents.
    
    Returns:
        dict: LLM configuration dictionary
    """
    return {
        "config_list": [
            {
                "model": os.getenv("MODEL_NAME", "gpt-4o"),
                "api_key": os.getenv("OPENAI_API_KEY"),
            }
        ],
        "temperature": 0.7,
    }


def get_model_name():
    """Get the configured model name."""
    return os.getenv("MODEL_NAME", "gpt-4o")


def get_api_key():
    """Get the OpenAI API key."""
    return os.getenv("OPENAI_API_KEY")


# Default configuration
DEFAULT_LLM_CONFIG = {
    "model": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 1000,
}