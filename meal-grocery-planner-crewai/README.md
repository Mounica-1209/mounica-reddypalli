# 🍽️ AI-Powered Meal & Grocery Planning System

A multi-agent AI system built with **CrewAI** that transforms meal preferences into complete, budget-conscious shopping plans. This project demonstrates advanced agent orchestration, structured data modeling, and YAML-based configuration for scalable AI applications.

## 🎯 Project Overview

This project addresses the common challenge of meal planning and grocery shopping by leveraging AI agents to:
- Research recipes based on user preferences
- Generate organized shopping lists by store section
- Optimize for budget constraints
- Minimize food waste through leftover management

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **CrewAI** | Multi-agent orchestration framework |
| **Pydantic** | Data validation and structured output models |
| **LangChain** | LLM integration and tool orchestration |
| **IBM WatsonX** | LLM provider (Granite 3.3) |
| **SerperDevTool** | Web search for recipe research |
| **YAML** | Declarative agent-task configuration |

## 📁 Project Structure

```
meal-grocery-planner-crewai/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── grocery_models.py    # Pydantic data models
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── meal_planner.py      # Recipe research agent
│   │   ├── shopping_organizer.py # Shopping list agent
│   │   └── budget_advisor.py    # Budget optimization agent
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── meal_planning_task.py
│   │   ├── shopping_task.py
│   │   └── budget_task.py
│   └── crew/
│       ├── __init__.py
│       └── grocery_crew.py      # Main crew orchestration
├── config/
│   └── agents.yaml              # YAML-based agent definitions
└── main.py                      # Entry point
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- API keys for LLM (OpenAI, IBM WatsonX, or similar)
- Serper API key for web search (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/meal-grocery-planner-crewai.git
cd meal-grocery-planner-crewai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Set up your environment variables:

```bash
# For OpenAI (alternative to WatsonX)
export OPENAI_API_KEY="your-openai-key"

# For Serper web search
export SERPER_API_KEY="your-serper-key"

# For IBM WatsonX (default)
export WATSONX_API_BASE="https://us-south.ml.cloud.ibm.com"
export WATSONX_PROJECT_ID="your-project-id"
```

### Usage

```python
from src.crew.grocery_crew import GroceryCrew

# Initialize the crew
crew = GroceryCrew()

# Run with a meal preference
result = crew.run(meal_preference="Italian dinner for 4 under $50")
print(result)
```

## 🤖 Agent Architecture

### 1. Meal Planning Agent
- **Role**: Research recipes and find ingredients
- **Tools**: SerperDevTool (web search)
- **Output**: MealPlan with researched ingredients

### 2. Shopping Organization Agent
- **Role**: Organize ingredients by store section
- **Output**: ShoppingCategory with grouped items

### 3. Budget Advisor Agent
- **Role**: Optimize for budget constraints
- **Output**: Cost estimates and money-saving tips

### 4. Food Leftover Agent
- **Role**: Suggest leftover recipes to minimize waste
- **Output**: Leftover utilization suggestions

## 📊 Data Models

### GroceryItem
```python
{
    "name": "Chicken Breast",
    "quantity": "2 lbs",
    "estimated_price": "$8-12",
    "category": "Meat"
}
```

### MealPlan
```python
{
    "meal_name": "Chicken Stir Fry",
    "difficulty_level": "Easy",
    "servings": 4,
    "researched_ingredients": ["chicken breast", "broccoli", "bell peppers"]
}
```

### GroceryShoppingPlan
```python
{
    "total_budget": "$40-50",
    "meal_plans": [...],
    "shopping_sections": [...],
    "shopping_tips": [...]
}
```

## 📝 Resume Highlights

> **AI-Powered Meal & Grocery Planning System**
> - Built an AI-driven meal planning system using CrewAI with specialized agents for recipe research, grocery organization, and budget optimization
> - Implemented Pydantic data models for structured output and YAML-based agent-task configurations for scalable deployment
> - Orchestrated multi-agent workflows using LangChain and IBM WatsonX Granite LLM

## 🔧 Key Features

- ✅ Multi-agent collaboration using CrewAI
- ✅ Structured data validation with Pydantic
- ✅ YAML-based configuration for easy maintenance
- ✅ Web search integration for real-time recipe research
- ✅ Budget optimization and cost estimation
- ✅ Store-section organization for efficient shopping

## 📚 Learning Outcomes

After this project, you will understand:
- Multi-agent system design with CrewAI
- Structured data modeling with Pydantic
- LangChain integration for LLM orchestration
- YAML-based configuration for AI agents
- Agent task assignment and crew coordination



*Built with CrewAI and LangChain as part of IBM Generative AI Certificate*
