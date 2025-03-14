import google.generativeai as genai
from PIL import Image
from src.config.config import ModelConfig
from src.utils.logger import logger

class ModelService:
    """Service class for handling AI model operations."""
    
    def __init__(self, api_key: str):
        """Initialize the model service with API key."""
        self.configure_model(api_key)
        self.model_config = ModelConfig()
    
    def configure_model(self, api_key: str) -> None:
        """Configure the Gemini AI model."""
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            logger.info("Model configured successfully")
        except Exception as e:
            logger.error(f"Error configuring model: {str(e)}")
            raise
    
    def analyze_image(self, image: Image) -> str:
        """Analyze the image using the Gemini model."""
        try:
            response = self.model.generate_content([
                self.model_config.ANALYSIS_PROMPT,
                image
            ])
            logger.info("Image analysis completed successfully")
            return response.text
        except Exception as e:
            logger.error(f"Error analyzing image: {str(e)}")
            raise 