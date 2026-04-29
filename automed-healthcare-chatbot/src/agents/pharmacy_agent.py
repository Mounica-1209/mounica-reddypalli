"""
Pharmacy Agent - Recommends medications based on diagnosis

The pharmacy agent suggests over-the-counter medications and remedies
based on the diagnosis provided by the diagnosis agent.
"""

from autogen import ConversableAgent
from src.config.llm_config import get_llm_config


def create_pharmacy_agent():
    """
    Create a pharmacy agent that recommends medications.
    
    Returns:
        ConversableAgent: The configured pharmacy agent
    """
    pharmacy_agent = ConversableAgent(
        name="pharmacy",
        system_message=(
            "You recommend medications based on diagnosis. "
            "Only respond once to avoid repetition. "
            "Suggest over-the-counter medications and home remedies "
            "when appropriate. Always include safety disclaimers "
            "and advise consulting a pharmacist or doctor before "
            "taking any medication."
        ),
        llm_config=get_llm_config(),
    )
    
    return pharmacy_agent


# Agent description for reference
PHARMACY_AGENT_DESCRIPTION = """
The Pharmacy Agent recommends appropriate medications and remedies 
based on the diagnosis. It provides OTC suggestions and safety 
guidelines for medication use.
"""