"""
Main Crew Orchestration for Meal & Grocery Planning

This module coordinates all agents and tasks to create a complete grocery planning workflow.
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai import LLM
from src.models.grocery_models import (
    GroceryItem, 
    MealPlan, 
    ShoppingCategory, 
    GroceryShoppingPlan
)
from src.agents.meal_planner import (
    MealPlannerAgent,
    ShoppingOrganizerAgent,
    BudgetAdvisorAgent,
    LeftoverManagerAgent
)


class GroceryCrew:
    """Main crew class that orchestrates the grocery planning workflow"""
    
    def __init__(self):
        # Initialize LLM (using IBM WatsonX Granite by default)
        self.llm = self._setup_llm()
        
        # Initialize agents
        self.meal_planner_agent = MealPlannerAgent(self.llm).create_agent()
        self.shopping_organizer_agent = ShoppingOrganizerAgent(self.llm).create_agent()
        self.budget_advisor_agent = BudgetAdvisorAgent(self.llm).create_agent()
        self.leftover_manager_agent = LeftoverManagerAgent(self.llm).create_agent()
        
    def _setup_llm(self):
        """Setup the LLM provider"""
        # Configure WatsonX environment
        os.environ["WATSONX_API_BASE"] = os.getenv(
            "WATSONX_API_BASE", 
            "https://us-south.ml.cloud.ibm.com"
        )
        os.environ["WX_PROJECT_ID"] = os.getenv("WX_PROJECT_ID", "skills-network")
        
        # Initialize LLM
        return LLM(model="watsonx/ibm/granite-3-3-8b-instruct")
    
    def _create_tasks(self, meal_preference: str):
        """Create tasks for each agent"""
        
        # Task 1: Meal Planning
        meal_planning_task = Task(
            description=(
                f"Research and find recipes for: {meal_preference}. "
                "Provide detailed ingredient lists, cooking instructions, "
                "difficulty level, and estimated cooking time."
            ),
            expected_output=(
                "A meal plan with recipe name, ingredients, difficulty, "
                "servings, and cooking time"
            ),
            agent=self.meal_planner_agent,
            output_json=MealPlan
        )
        
        # Task 2: Shopping Organization
        shopping_task = Task(
            description=(
                "Organize the ingredients from the meal plan by store section. "
                "Group items like produce, dairy, meat, and pantry items separately. "
                "Provide estimated prices for each item."
            ),
            expected_output=(
                "A shopping list organized by store sections with item details"
            ),
            agent=self.shopping_organizer_agent,
            output_json=ShoppingCategory
        )
        
        # Task 3: Budget Analysis
        budget_task = Task(
            description=(
                "Analyze the shopping list and provide budget optimization. "
                "Suggest alternatives to reduce costs, provide money-saving tips, "
                "and ensure the total stays within budget."
            ),
            expected_output=(
                "Budget analysis with cost estimates and savings tips"
            ),
            agent=self.budget_advisor_agent
        )
        
        # Task 4: Leftover Management
        leftover_task = Task(
            description=(
                "Suggest creative recipes for any leftover ingredients. "
                "Provide ideas to minimize food waste and maximize value."
            ),
            expected_output=(
                "Leftover recipe suggestions and food waste prevention tips"
            ),
            agent=self.leftover_manager_agent
        )
        
        return [meal_planning_task, shopping_task, budget_task, leftover_task]
    
    def run(self, meal_preference: str, budget: str = "$50"):
        """Run the complete grocery planning workflow"""
        
        # Create tasks
        tasks = self._create_tasks(meal_preference)
        
        # Create crew with sequential process
        crew = Crew(
            agents=[
                self.meal_planner_agent,
                self.shopping_organizer_agent,
                self.budget_advisor_agent,
                self.leftover_manager_agent
            ],
            tasks=tasks,
            process=Process.sequential,  # Tasks run in sequence
            verbose=True
        )
        
        # Execute the workflow
        result = crew.kickoff(inputs={
            "meal_preference": meal_preference,
            "budget": budget
        })
        
        return result


# Entry point for direct execution
if __name__ == "__main__":
    # Example usage
    crew = GroceryCrew()
    result = crew.run(
        meal_preference="Italian dinner for 4 under $50",
        budget="$50"
    )
    print(result)