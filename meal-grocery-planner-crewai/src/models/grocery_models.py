"""
Grocery Shopping Data Models

This module defines Pydantic models for structured grocery shopping data.
These models ensure consistent data format across all AI agent responses.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class GroceryItem(BaseModel):
    """Individual grocery item with purchase details"""
    name: str = Field(description="Name of the grocery item")
    quantity: str = Field(description="Quantity needed (e.g., '2 lbs', '1 gallon')")
    estimated_price: str = Field(description="Estimated price range (e.g., '$3-5')")
    category: str = Field(description="Store section (e.g., 'Produce', 'Dairy', 'Meat')")


class MealPlan(BaseModel):
    """Meal recipe with ingredients and cooking details"""
    meal_name: str = Field(description="Name of the meal")
    difficulty_level: str = Field(description="Cooking difficulty: 'Easy', 'Medium', or 'Hard'")
    servings: int = Field(description="Number of people it serves")
    researched_ingredients: List[str] = Field(description="Ingredients found through research")
    cooking_time: Optional[str] = Field(default=None, description="Estimated cooking time")
    recipe_url: Optional[str] = Field(default=None, description="URL to recipe source")


class ShoppingCategory(BaseModel):
    """Store section with organized items"""
    section_name: str = Field(description="Store section name (e.g., 'Produce', 'Meat')")
    items: List[GroceryItem] = Field(description="Items in this section")
    estimated_total: str = Field(description="Estimated cost for this section")


class GroceryShoppingPlan(BaseModel):
    """Complete shopping strategy with all details"""
    total_budget: str = Field(description="Total planned budget")
    meal_plans: List[MealPlan] = Field(description="Planned meals")
    shopping_sections: List[ShoppingCategory] = Field(description="Organized by store sections")
    shopping_tips: List[str] = Field(description="Money-saving and efficiency tips")
    created_at: datetime = Field(default_factory=datetime.now)