from dataclasses import dataclass, field
from typing import List

@dataclass
class AppConfig:
    """Application configuration settings."""
    PAGE_TITLE: str = "DishVision AI 🍽️"
    PAGE_ICON: str = "🍽️"
    LAYOUT: str = "wide"
    MODEL_NAME: str = "gemini-1.5-flash"
    ALLOWED_IMAGE_TYPES: List[str] = field(
        default_factory=lambda: ["jpg", "jpeg", "png", "webp", "avif"]
    )
    GEMINI_LOGO_URL: str = "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_SS.width-1300.jpg"

@dataclass
class ModelConfig:
    """Model configuration and prompts."""
    ANALYSIS_PROMPT: str = """
    You will receive a food image from the user. Your task:
    - Identify the **Dish Name**
    - List **Ingredients** with quantities
    - Provide a **Step-by-Step Recipe**

    **Format Output Like This:**
    🍽️ **Dish Name:**  
    - Name of the dish
    
    🥕 **Ingredients:**  
    1. Ingredient-1: quantity  
    2. Ingredient-2: quantity  
    ...
    
    📜 **Recipe:**  
    1. Step 1  
    2. Step 2  
    ...
    """ 