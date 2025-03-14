import streamlit as st
from typing import Optional, Tuple
from PIL import Image
from src.config.config import AppConfig
from src.utils.logger import logger

class UIComponents:
    """Class to handle all UI components and interactions."""
    
    def __init__(self):
        """Initialize UI components with configuration."""
        self.config = AppConfig()
    
    def setup_page(self) -> None:
        """Configure the Streamlit page settings."""
        try:
            st.set_page_config(
                page_title=self.config.PAGE_TITLE,
                layout=self.config.LAYOUT,
                page_icon=self.config.PAGE_ICON
            )
            logger.info("Page configuration set successfully")
        except Exception as e:
            logger.error(f"Error setting page configuration: {str(e)}")
            raise
    
    def setup_sidebar(self) -> str:
        """Set up the sidebar with API key input."""
        try:
            st.sidebar.image(self.config.GEMINI_LOGO_URL)
            st.sidebar.title("🔑 API Key Setup")
            
            api_key = st.sidebar.text_input(
                "Enter your Google AI Studio API Key",
                type="password"
            )
            
            st.sidebar.markdown("""
            🔹 **Where to get API Key?**  
            - Go to [Google AI Studio](https://aistudio.google.com/)  
            - Sign in & generate your API key  
            - Paste it above to start!
            """)
            
            logger.info("Sidebar setup completed")
            return api_key
        except Exception as e:
            logger.error(f"Error setting up sidebar: {str(e)}")
            raise
    
    def display_header(self) -> None:
        """Display the main header and description."""
        try:
            st.markdown("""
            <h1 style='text-align: center; font-size: 48px; color: #FF5733;'>
                🍽️ DishVision AI
            </h1>
            <h3 style='text-align: center; color: #666;'>
                Snap, Detect & Cook with AI! 🤖🔥
            </h3>
            """, unsafe_allow_html=True)
            
            st.write("Upload a food image, and I'll detect the dish, its ingredients, and recipe! 🔥")
            
            st.markdown("""
            🖼️ **How It Works:**  
            1. Upload an image of a dish.  
            2. The AI will analyze the image and identify the dish.  
            3. You'll get the **dish name, ingredients, and step-by-step recipe**.  
            4. Enjoy cooking! 🍳  
            """)
            
            logger.info("Header displayed successfully")
        except Exception as e:
            logger.error(f"Error displaying header: {str(e)}")
            raise
    
    def get_image_input(self) -> Optional[Image.Image]:
        """Handle image upload and camera input."""
        try:
            option = st.radio(
                "Choose Image Input Method:",
                ["Upload Image", "Capture from Camera"]
            )
            
            uploaded_file = None
            if option == "Upload Image":
                uploaded_file = st.file_uploader(
                    "📸 Upload a dish image",
                    type=self.config.ALLOWED_IMAGE_TYPES
                )
            elif option == "Capture from Camera":
                uploaded_file = st.camera_input("📷 Take a photo of the dish")
            
            if uploaded_file is not None:
                logger.info("Image uploaded successfully")
                return Image.open(uploaded_file)
            return None
        except Exception as e:
            logger.error(f"Error handling image input: {str(e)}")
            raise
    
    def display_results(self, image: Image.Image, analysis_text: str) -> None:
        """Display the analysis results."""
        try:
            st.image(image, caption="✅ Uploaded Image", use_container_width=True)
            st.markdown("---")
            st.subheader("🍛 **Detected Dish Details**")
            st.markdown(analysis_text)
            logger.info("Results displayed successfully")
        except Exception as e:
            logger.error(f"Error displaying results: {str(e)}")
            raise 