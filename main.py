import streamlit as st
from src.components.ui_components import UIComponents
from src.services.model_service import ModelService
from src.utils.logger import logger

class DishVisionApp:
    """Main application class for DishVision AI."""
    
    def __init__(self):
        """Initialize the application components."""
        self.ui = UIComponents()
        self.model_service = None
    
    def initialize_model(self, api_key: str) -> None:
        """Initialize the model service with API key."""
        if api_key:
            self.model_service = ModelService(api_key)
    
    def run(self):
        """Run the main application."""
        try:
            # Setup UI
            self.ui.setup_page()
            api_key = self.ui.setup_sidebar()
            self.ui.display_header()
            
            # Initialize model if API key is provided
            self.initialize_model(api_key)
            
            # Get image input
            image = self.ui.get_image_input()
            
            # Process image if available
            if image and self.model_service:
                with st.spinner("🤖 Analyzing the dish... Please wait 🍲"):
                    analysis_text = self.model_service.analyze_image(image)
                self.ui.display_results(image, analysis_text)
            elif not api_key:
                st.warning("⚠️ Please enter your API key in the sidebar to proceed.")
            
            logger.info("Application run completed successfully")
        except Exception as e:
            logger.error(f"Error running application: {str(e)}")
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = DishVisionApp()
    app.run() 