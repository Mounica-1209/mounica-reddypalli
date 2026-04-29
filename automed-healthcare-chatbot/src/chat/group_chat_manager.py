"""
GroupChat Manager - Orchestrates multi-agent conversation

This module manages the GroupChat and GroupChatManager for coordinating
the healthcare consultation workflow between multiple AI agents.
"""

from autogen import GroupChat, GroupChatManager


def create_group_chat(agents, max_rounds: int = 5):
    """
    Create a GroupChat for structured multi-agent conversation.
    
    Args:
        agents: List of ConversableAgent instances
        max_rounds: Maximum number of conversation rounds (default: 5)
    
    Returns:
        GroupChat: Configured group chat instance
    """
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=max_rounds,
        speaker_selection_method="round_robin",  # Ensures structured conversation flow
    )
    
    return groupchat


def create_group_chat_manager(groupchat):
    """
    Create a GroupChatManager to handle the conversation flow.
    
    Args:
        groupchat: The GroupChat instance to manage
    
    Returns:
        GroupChatManager: Configured manager instance
    """
    manager = GroupChatManager(
        name="manager",
        groupchat=groupchat,
    )
    
    return manager


def create_healthcare_group_chat(diagnosis_agent, pharmacy_agent, consultation_agent):
    """
    Create a complete healthcare consultation group chat.
    
    Args:
        diagnosis_agent: The diagnosis ConversableAgent
        pharmacy_agent: The pharmacy ConversableAgent
        consultation_agent: The consultation ConversableAgent
    
    Returns:
        tuple: (GroupChat, GroupChatManager)
    """
    # Create group chat with the three healthcare agents
    group_chat = GroupChat(
        agents=[diagnosis_agent, pharmacy_agent, consultation_agent],
        messages=[],
        max_round=5,
        speaker_selection_method="round_robin",
    )
    
    # Create manager to coordinate the conversation
    manager = GroupChatManager(
        name="healthcare_manager",
        groupchat=group_chat,
    )
    
    return group_chat, manager