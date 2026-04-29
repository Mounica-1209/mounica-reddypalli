"""
Consultation Agent - Provides final advice and determines if doctor visit is needed

The consultation agent acts as the final advisor, determining whether
the patient needs to seek professional medical attention.
"""

from autogen import ConversableAgent
from src.config.llm_config import get_llm_config


def create_consultation_agent():
    """
    Create a consultation agent that provides final medical advice.
    
    Returns:
        ConversableAgent: The configured consultation agent
    """
    consultation_agent = ConversableAgent(
        name="consultation",
        system_message=(
            "You determine if a doctor's visit is required. "
            "Provide a final summary with clear next steps. "
            "IMPORTANT: End your response with 'CONSULTATION_COMPLETE' "
            "to signal the end of the conversation. "
            "Consider the severity of symptoms and provide clear "
            "guidance on whether professional medical attention "
            "is needed."
        ),
        llm_config=get_llm_config(),
    )
    
    return consultation_agent


# Agent description for reference
CONSULTATION_AGENT_DESCRIPTION = """
The Consultation Agent provides the final summary and determines 
whether the patient needs to visit a doctor. It adds termination 
condition 'CONSULTATION_COMPLETE' to end the session.
"""