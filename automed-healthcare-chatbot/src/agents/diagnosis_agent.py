"""
Diagnosis Agent - Analyzes symptoms and provides potential diagnoses

The diagnosis agent uses AI to analyze patient symptoms and suggest
possible conditions based on medical knowledge.
"""

from autogen import ConversableAgent
from src.config.llm_config import get_llm_config


def create_diagnosis_agent():
    """
    Create a diagnosis agent that analyzes symptoms and provides diagnosis.
    
    Returns:
        ConversableAgent: The configured diagnosis agent
    """
    diagnosis_agent = ConversableAgent(
        name="diagnosis",
        system_message=(
            "You analyze symptoms and provide a possible diagnosis. "
            "Summarize key points in one response. "
            "Consider the patient's description carefully and suggest "
            "potential conditions that match the symptoms. "
            "Always include a disclaimer that this is not professional "
            "medical advice."
        ),
        llm_config=get_llm_config(),
    )
    
    return diagnosis_agent


# Agent description for reference
DIAGNOSIS_AGENT_DESCRIPTION = """
The Diagnosis Agent analyzes patient symptoms and provides potential 
medical conditions. It uses AI-powered analysis to suggest possible 
diagnoses based on the described symptoms.
"""