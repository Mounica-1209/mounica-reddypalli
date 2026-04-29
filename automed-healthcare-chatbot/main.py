"""
Main Entry Point for AutoMed Healthcare Chatbot

Usage:
    python main.py
"""

import warnings
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Suppress warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

from src.agents.patient_agent import create_patient_agent
from src.agents.diagnosis_agent import create_diagnosis_agent
from src.agents.pharmacy_agent import create_pharmacy_agent
from src.agents.consultation_agent import create_consultation_agent
from src.chat.group_chat_manager import create_group_chat, create_group_chat_manager


def main():
    """Main function to run the healthcare consultation"""
    
    print("\n" + "=" * 60)
    print("🤖 Welcome to AutoMed - AI Healthcare Consultation System")
    print("=" * 60)
    print("\n⚠️  DISCLAIMER: This is for educational purposes only.")
    print("   Please consult a healthcare professional for real medical advice.\n")
    
    # Create all agents
    print("📋 Creating AI agents...")
    patient_agent = create_patient_agent()
    diagnosis_agent = create_diagnosis_agent()
    pharmacy_agent = create_pharmacy_agent()
    consultation_agent = create_consultation_agent()
    print("   ✓ All agents created successfully!")
    
    # Create group chat
    print("🔗 Setting up group chat...")
    group_chat = create_group_chat(
        [diagnosis_agent, pharmacy_agent, consultation_agent],
        max_rounds=5
    )
    manager = create_group_chat_manager(group_chat)
    print("   ✓ Group chat configured!")
    
    # Get patient symptoms
    print("\n" + "-" * 60)
    symptoms = input("🩺 Please describe your symptoms: ")
    
    if not symptoms.strip():
        print("❌ Please provide symptoms to continue.")
        return
    
    print("\n" + "-" * 60)
    print("🩺 Analyzing symptoms...")
    print("-" * 60 + "\n")
    
    # Start consultation
    result = patient_agent.initiate_chat(
        manager,
        message=f"I am feeling {symptoms}. Can you help?",
    )
    
    print("\n" + "=" * 60)
    print("✅ Consultation Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()