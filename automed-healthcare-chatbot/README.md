# 🤖 AutoMed - Multi-Agent Healthcare Chatbot

A multi-agent AI medical consultation system built with **AG2 (AutoGen)** that simulates expert healthcare collaboration through intelligent agent communication.

## 🎯 Project Overview

AutoMed is an intelligent healthcare chatbot that uses multiple specialized AI agents to provide comprehensive medical consultations. Instead of relying on a single AI response, AutoMed orchestrates multiple agents that collaborate to:

- Analyze patient symptoms
- Provide potential diagnoses
- Recommend medications
- Determine if professional medical attention is needed

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **AG2 (AutoGen)** | Multi-agent orchestration framework |
| **OpenAI GPT-4o** | Large Language Model for agent responses |
| **GroupChat** | Agent conversation management |
| **ConversableAgent** | Individual agent implementation |
| **GroupChatManager** | Conversation coordination |

## 📁 Project Structure

```
automed-healthcare-chatbot/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── src/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── patient_agent.py      # User interaction agent
│   │   ├── diagnosis_agent.py    # Symptom analysis agent
│   │   ├── pharmacy_agent.py     # Medication recommendation agent
│   │   └── consultation_agent.py # Final advice agent
│   ├── chat/
│   │   ├── __init__.py
│   │   └── group_chat_manager.py # GroupChat orchestration
│   └── config/
│       └── llm_config.py         # LLM configuration
├── examples/
│   └── healthcare_example.py     # Usage examples
└── main.py                       # Entry point
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API key (GPT-4o)
- AG2 (AutoGen) library

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/automed-healthcare-chatbot.git
cd automed-healthcare-chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Set up your environment variables:

```bash
# Set OpenAI API key
export OPENAI_API_KEY="your-openai-api-key"
```

Or create a `.env` file:

```bash
OPENAI_API_KEY=your-openai-api-key
```

### Usage

```python
from src.agents.patient_agent import create_patient_agent
from src.agents.diagnosis_agent import create_diagnosis_agent
from src.agents.pharmacy_agent import create_pharmacy_agent
from src.agents.consultation_agent import create_consultation_agent
from src.chat.group_chat_manager import create_group_chat

# Create agents
patient = create_patient_agent()
diagnosis = create_diagnosis_agent()
pharmacy = create_pharmacy_agent()
consultation = create_consultation_agent()

# Create group chat
group_chat = create_group_chat([diagnosis, pharmacy, consultation])

# Start consultation
response = patient.initiate_chat(
    group_chat,
    message="I have been experiencing persistent headaches and fatigue"
)
```

## 🤖 Agent Architecture

### 1. Patient Agent
- **Role**: Captures user symptoms and medical concerns
- **Purpose**: Initiates conversation and collects patient input

### 2. Diagnosis Agent
- **Role**: Analyzes symptoms and provides potential diagnoses
- **LLM**: GPT-4o for medical analysis
- **Output**: Possible conditions based on symptoms

### 3. Pharmacy Agent
- **Role**: Recommends medications and remedies
- **Constraints**: Responds only once per consultation
- **Output**: OTC medications and self-care suggestions

### 4. Consultation Agent
- **Role**: Determines if doctor visit is needed
- **Output**: Final summary with next steps
- **Termination**: Adds "CONSULTATION_COMPLETE" to end session

## 📊 System Flow

```
User Input (Symptoms)
        │
        ▼
┌───────────────────┐
│   Patient Agent   │ ← Initiates conversation
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  GroupChatManager │ ← Orchestrates agents
└────────┬──────────┘
         │
    ┌────┴────┬────────────┐
    ▼         ▼            ▼
┌───────┐ ┌───────┐ ┌────────────┐
│Diag-  │ │Pharm- │ │Consulta-   │
│nosis  │ │acy    │ │tion        │
│Agent  │ │Agent  │ │Agent       │
└───┬───┘ └───┬───┘ └─────┬──────┘
    │         │           │
    └─────────┴───────────┘
              │
              ▼
       Final Recommendation
```

## 📝 Resume Highlights

> **Multi-Agent Medical Consultation System**
> - Developed a multi-agent healthcare chatbot using AG2 (AutoGen) with GroupChat architecture enabling collaborative AI decision-making
> - Implemented specialized agents for symptom analysis, medication recommendations, and consultation advisory using OpenAI GPT-4o
> - Designed agent communication workflows using ConversableAgent and GroupChatManager that mimic real medical team collaboration

## ⚠️ Disclaimer

> **Important**: This project is for educational purposes only. The medical advice provided should not be considered a substitute for professional medical consultation, diagnosis, or treatment. Always seek guidance from a qualified healthcare professional.

## 🔧 Key Features

- ✅ Multi-agent collaboration using AG2 (AutoGen)
- ✅ GroupChat for structured conversation flow
- ✅ Round-robin speaker selection
- ✅ Max rounds configuration to prevent infinite loops
- ✅ Termination condition for clean session ending
- ✅ Human-AI collaboration support

## 📚 Learning Outcomes

After this project, you will understand:
- Multi-agent system design with AG2 (AutoGen)
- GroupChat and GroupChatManager usage
- ConversableAgent configuration
- Agent-to-agent communication patterns
- Healthcare domain AI application



*Built with AG2 (AutoGen) as part of IBM Generative AI Certificate*

> 🤖 *"AI-powered healthcare consultation through multi-agent collaboration"*
