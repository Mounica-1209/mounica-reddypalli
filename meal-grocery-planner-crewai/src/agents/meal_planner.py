"""
AI Agents for Meal & Grocery Planning System

This module defines the specialized AI agents for the grocery planning crew.
"""

import os
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI


class MealPlannerAgent:
    """Agent responsible for researching recipes and finding ingredients"""
    
    def __init__(self, llm):
        self.llm = llm
        self.serper_tool = SerperDevTool()
        
    def create_agent(self) -> Agent:
        return Agent(
            role="Meal Planning Expert",
            goal="Find delicious recipes that match user preferences and budget",
            backstory=(
                "You are a professional meal planner with expertise in diverse cuisines. "
                "You research recipes, find ingredient lists, and ensure meals are "
                "practical to prepare within the user's budget and time constraints."
            ),
            tools=[self.serper_tool],
            llm=self.llm,
            verbose=True
        )


class ShoppingOrganizerAgent:
    """Agent responsible for organizing shopping lists by store section"""
    
    def __init__(self, llm):
        self.llm = llm
        
    def create_agent(self) -> Agent:
        return Agent(
            role="Shopping Organization Expert",
            goal="Organize ingredients by store section for efficient shopping",
            backstory=(
                "You are an expert at organizing grocery shopping lists. "
                "You group items by store section (produce, dairy, meat, etc.) "
                "and ensure nothing is missed for a complete shopping experience."
            ),
            llm=self.llm,
            verbose=True
        )


class BudgetAdvisorAgent:
    """Agent responsible for budget optimization and cost estimation"""
    
    def __init__(self, llm):
        self.llm = llm
        
    def create_agent(self) -> Agent:
        return Agent(
            role="Budget Advisor",
            goal="Optimize shopping for maximum value within budget constraints",
            backstory=(
                "You are a financial expert specializing in grocery budgeting. "
                "You analyze ingredient costs, suggest alternatives, and provide "
                "money-saving tips while ensuring nutritional needs are met."
            ),
            llm=self.llm,
            verbose=True
        )


class LeftoverManagerAgent:
    """Agent responsible for suggesting leftover recipe ideas"""
    
    def __init__(self, llm):
        self.llm = llm
        
    def create_agent(self) -> Agent:
        return Agent(
            role="Leftover Management Expert",
            goal="Minimize food waste by suggesting creative leftover recipes",
            backstory=(
                "You are a culinary expert focused on reducing food waste. "
                "You suggest creative ways to use leftover ingredients and "
                "provide recipes that maximize the value of purchased items."
            ),
            llm=self.llm,
            verbose=True
        )