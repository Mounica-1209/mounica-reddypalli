"""
Main Entry Point for Meal & Grocery Planner

Usage:
    python main.py "Italian dinner for 4 under $50"
"""

import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.crew.grocery_crew import GroceryCrew


def main():
    """Main function to run the grocery planning crew"""
    
    # Get meal preference from command line or use default
    if len(sys.argv) > 1:
        meal_preference = sys.argv[1]
    else:
        meal_preference = "Healthy dinner for 2 under $30"
    
    budget = sys.argv[2] if len(sys.argv) > 2 else "$30"
    
    print(f"\n🍽️ Planning: {meal_preference}")
    print(f"💰 Budget: {budget}")
    print("-" * 50)
    
    # Initialize and run the crew
    crew = GroceryCrew()
    result = crew.run(meal_preference=meal_preference, budget=budget)
    
    print("\n" + "=" * 50)
    print("📋 COMPLETE GROCERY PLAN")
    print("=" * 50)
    print(result)


if __name__ == "__main__":
    main()