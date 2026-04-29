"""
Patient Agent - Captures user symptoms and initiates conversation

The patient agent represents the user in the healthcare consultation system.
It collects symptoms and medical concerns from the user.
"""

from autogen import ConversableAgent
from src.config.llm_config import get_llm_config


def create_patient_agent():
    """
    Create a patient agent that describes symptoms and asks for medical help.
    
    Returns:
        ConversableAgent: The configured patient agent
    """
    patient_agent = ConversableAgent(
        name="patient",
        system_message=(
            "You describe symptoms and ask for medical help. "
            "You are the patient seeking medical consultation. "
            "Provide detailed information about your symptoms, "
            "including duration, severity, and any relevant context."
        ),
        llm_config=get_llm_config(),
        is_termination_msg=lambda msg: "CONSULTATION_COMPLETE" in msg.get("content", ""),
    )
    
    return patient_agent


def initiate_consultation(patient_agent, group_chat_manager, symptoms: str):
    """
    Start a healthcare consultation with the given symptoms.
    
    Args:
        patient_agent: The patient ConversableAgent
        group_chat_manager: The GroupChatManager coordinating the conversation
        symptoms: Description of the patient's symptoms
    
    Returns:
        The chat result from the conversation
    """
    message = f"I am feeling {symptoms}. Can you help?"
    
    result = patient_agent.initiate_chat(
        group_chat_manager,
        message=message,
    )
    
    return result